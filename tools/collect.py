#!/usr/bin/env python3
"""Stage 1: collect metadata (latest release, tree, stars) for every project.

Reads  data/projects.toml  (copy of dbohdan/classless-css/data/projects.toml)
plus the extra projects, and writes  .tmp/meta.json  with, for each project:

    slug, title, kind, github, website, demo, stars, ref, tag, commit,
    min_css: [paths of *.min.css found at that ref]

Nothing is downloaded here; the CSS choice is reviewed before stage 2.
"""
from __future__ import annotations

import concurrent.futures as futures
import json
import os
import re
import shutil
import subprocess
import sys
import time
import tomllib
import urllib.parse
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TMP = ROOT / ".tmp"
REPOS = TMP / "repos"
PROXY = "http://127.0.0.1:1080"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"

# dbohdan title -> slug used on this page / in css filenames
SLUGS = {
    "Almond.CSS": "almond",
    "attriCSS": "attricss",
    "awsm.css": "awsm",
    "axist": "axist",
    "Bahunya": "bahunya",
    "Bamboo CSS": "bamboo",
    "BareCSS": "barecss",
    "Basic.css": "basiccss",
    "Bolt.css": "bolt",
    "Blades": "blades",
    "bullframe.css": "bullframe",
    "ChimeraCSS": "chimeracss",
    "Classless.css": "classlesscss",
    "concrete.css": "concrete",
    "dev.css": "devcss",
    "Downstyler": "downstyler",
    "Fylgja": "fylgja",
    "holiday.css": "holiday",
    "LatexCSS": "latex",
    "magick.css": "magick",
    "Markdown CSS — Air": "markdownair",
    "Markdown CSS — Modest": "markdownmodest",
    "Markdown CSS — Retro": "markdownretro",
    "Markdown CSS — Splendor": "markdownsplendor",
    "Marx": "marx",
    "MercuryCSS": "mercury",
    "mi.css": "micss",
    "MVP.css": "mvp",
    "new.css": "newcss",
    "nimble.css": "nimble",
    "no-class.css": "noclass",
    "Pico.css": "pico",
    "ridge.css": "ridge",
    "sakura": "sakura",
    "shadcn-classless (Nandaleio)": "shadcn",
    "Simple.css": "simple",
    "SPCSS": "spcss",
    "style.css": "stylecss",
    "Stylize.css": "stylize",
    "tacit": "tacit",
    "Tiny.css": "tinycss",
    "tty.css": "ttycss",
    "Tufte CSS": "tufte",
    "W3C Core Styles": "w3ccore",
    "water.css": "water",
    "Writ": "writ",
    "YoRHa": "yorha",
    "Barrel.css": "barrel",
    "Chota": "chota",
    "matcha.css": "matcha",
    "Milligram": "milligram",
    "mini.css": "minicss",
    "mono": "mono",
    "Picnic CSS": "picnic",
    "SASS-ZERO (Breadboard)": "sasszero",
    "Wing": "wing",
}

# Projects that are not in dbohdan's list (or are handled locally).
EXTRAS = [
    # slug, title, github, website
    ("sumi", "Sumi.css", "vladocar/Sumi.css", "https://github.com/vladocar/Sumi.css"),
    ("missing", "Missing.css", "bigskysoftware/missing", "https://missing.style/"),
    # Local, hand-maintained stylesheets: never downloaded.
    ("materia", "Materia (local)", "", "https://github.com/jojo-joo/classless-form"),
    ("pure", "Pure Classless (local)", "", "https://github.com/jojo-joo/classless-form"),
]


# --------------------------------------------------------------------------- #
# HTTP helpers
# --------------------------------------------------------------------------- #
def _opener(proxy: bool):
    handlers = []
    if proxy:
        handlers.append(urllib.request.ProxyHandler({"http": PROXY, "https": PROXY}))
    return urllib.request.build_opener(*handlers)


def http_get(url: str, *, proxy: bool = True, timeout: int = 60, tries: int = 4) -> bytes:
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with _opener(proxy).open(req, timeout=timeout) as resp:
                return resp.read()
        except Exception as exc:  # noqa: BLE001 - network is flaky, retry everything
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise last  # type: ignore[misc]


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: D401
        return None


def latest_release_tag(repo: str) -> str | None:
    """Tag of the latest *GitHub release*, via the /releases/latest redirect."""
    url = f"https://github.com/{repo}/releases/latest"
    for proxy in (True, False):
        for attempt in range(3):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA})
                opener = urllib.request.build_opener(
                    urllib.request.ProxyHandler({"http": PROXY, "https": PROXY}) if proxy else urllib.request.ProxyHandler({}),
                    _NoRedirect(),
                )
                try:
                    with opener.open(req, timeout=40) as resp:
                        return None
                except urllib.error.HTTPError as err:
                    if err.code in (301, 302, 303, 307, 308):
                        loc = err.headers.get("Location", "")
                        m = re.search(r"/releases/tag/([^/?#]+)", loc)
                        return urllib.parse.unquote(m.group(1)) if m else None
                    if err.code == 404:
                        return None
                    raise
            except Exception:  # noqa: BLE001
                time.sleep(1.5 * (attempt + 1))
    return None


def github_stars(repo: str) -> int | None:
    html = http_get(f"https://github.com/{repo}", proxy=True, timeout=60).decode("utf-8", "replace")
    m = re.search(r'"stargazerCount":(\d+)', html)
    return int(m.group(1)) if m else None


# --------------------------------------------------------------------------- #
# Git helpers
# --------------------------------------------------------------------------- #
def run(args: list[str], cwd: Path | None = None, timeout: int = 180) -> str:
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    proc = subprocess.run(
        args, cwd=cwd, env=env, capture_output=True, text=True, timeout=timeout
    )
    if proc.returncode != 0:
        raise RuntimeError(f"{' '.join(args)} -> {proc.returncode}: {proc.stderr.strip()[:400]}")
    return proc.stdout


def clone_tree(slug: str, repo: str, ref: str | None) -> tuple[str, str, list[str]]:
    """Shallow partial clone (trees only), return (commit, date, file paths)."""
    dest = REPOS / slug
    if dest.exists():
        shutil.rmtree(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    args = ["git", "clone", "--quiet", "--no-checkout", "--filter=blob:none", "--depth", "1"]
    if ref:
        args += ["--branch", ref]
    args += [f"https://github.com/{repo}.git", str(dest)]
    run(args)
    commit = run(["git", "-C", str(dest), "rev-parse", "HEAD"]).strip()
    date = run(["git", "-C", str(dest), "log", "-1", "--format=%cs"]).strip()
    paths = run(["git", "-C", str(dest), "ls-tree", "-r", "--name-only", "HEAD"]).splitlines()
    return commit, date, paths


def default_branch(repo: str) -> str:
    out = run(["git", "ls-remote", "--symref", f"https://github.com/{repo}.git", "HEAD"])
    m = re.search(r"ref: refs/heads/(\S+)\s+HEAD", out)
    return m.group(1) if m else "master"


# --------------------------------------------------------------------------- #
# Project list
# --------------------------------------------------------------------------- #
def load_projects() -> list[dict]:
    toml_path = ROOT / "data" / "projects.toml"
    data = tomllib.loads(toml_path.read_text(encoding="utf-8"))
    projects = []
    # tomllib keeps the file order.
    for title, meta in data.items():
        slug = SLUGS.get(title)
        if slug is None:
            print(f"!! no slug for {title!r}", file=sys.stderr)
            continue
        projects.append(
            {
                "slug": slug,
                "title": title,
                "github": meta.get("github", ""),
                "website": meta.get("website", ""),
                "demo": meta.get("demo", ""),
                "tags": meta.get("tags", []),
            }
        )
    for slug, title, github, website in EXTRAS:
        projects.append(
            {
                "slug": slug,
                "title": title,
                "github": github,
                "website": website,
                "demo": "",
                "tags": ["local"] if not github else ["extra"],
            }
        )
    return projects


def collect(project: dict) -> dict:
    slug = project["slug"]
    repo = project["github"]
    kind = project["tags"][0] if project["tags"] else "classless"
    out = dict(project, kind=kind, stars=None, ref=None, tag=None,
               commit=None, date=None, min_css=[], error=None)

    if slug in ("materia", "pure"):
        out["local"] = True
        return out
    if not repo:
        return out
    try:
        tag = latest_release_tag(repo)
        ref = tag or default_branch(repo)
        commit, date, paths = clone_tree(slug, repo, tag)
        out.update(ref=ref, tag=tag, commit=commit, date=date)
        out["min_css"] = [p for p in paths if p.endswith(".min.css")]
        out["min_css"].sort(key=lambda p: (p.count("/"), len(p), p))
        if not out["min_css"]:
            out["all_css"] = [p for p in paths if p.endswith(".css")][:40]
        out["stars"] = github_stars(repo)
    except Exception as exc:  # noqa: BLE001
        out["error"] = f"{type(exc).__name__}: {exc}"[:500]
    return out


def main() -> None:
    projects = load_projects()
    REPOS.mkdir(parents=True, exist_ok=True)
    results: list[dict] = []
    with futures.ThreadPoolExecutor(max_workers=5) as pool:
        for res in pool.map(collect, projects):
            results.append(res)
            status = "ok" if not res["error"] else "ERR"
            print(f"[{status}] {res['slug']:<16} {res.get('tag') or res.get('ref') or '-'}", flush=True)
    (TMP / "meta.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\nwrote {TMP / 'meta.json'}")


if __name__ == "__main__":
    main()

