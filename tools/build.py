#!/usr/bin/env python3
"""Stage 2: download every framework's minified stylesheet into css/.

Rules implemented here (from the task):
  * official source, never a CSS CDN: raw.githubusercontent.com (the git repo)
    or the project's own website / official npm tarball;
  * latest GitHub release, falling back to the default branch;
  * one *.min.css per framework (no .gz);
  * Materia and Pure are local hand-written files and are left alone.

Projects that only publish unminified CSS upstream are minified locally with
esbuild, recorded in frameworks.json as `"minified": "esbuild"`.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from collect import ROOT, TMP, http_get  # noqa: E402

CSS_DIR = ROOT / "css"
TOOLS = TMP / "minify"
ESBUILD = TOOLS / "node_modules" / "esbuild" / "bin" / "esbuild"
SASS = TOOLS / "node_modules" / "sass" / "sass.js"

# The node on PATH here is v8 and cannot run esbuild/sass; prefer the bundled one.
_NODE_CANDIDATES = [
    os.environ.get("DSH_NODE", ""),
    r"C:\Users\Administrator\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\node\bin\node.exe",
    "node",
]
NODE = next((p for p in _NODE_CANDIDATES if p and (p == "node" or Path(p).exists())), "node")

# slug -> list of (output file name, source, minify?)
#   ("gh", "path/in/repo.css")   raw.githubusercontent at the release ref
#   ("url", "https://...")       official site / archived official file
#   ("npm", "package", "path")   official npm tarball
#   ("sass", "entry.scss")       compiled from the repo's own sources
#   ("local", "css/x.css")       hand-maintained, never downloaded
SPEC: dict[str, list[tuple[str, tuple, bool]]] = {
    "almond": [("almond.min.css", ("gh", "dist/almond.min.css"), False)],
    "attricss": [("attricss.min.css", ("gh", "themes/midnight-green.css"), True)],
    "awsm": [("awsm.min.css", ("npm", "awsm.css", "dist/awsm.min.css"), False)],
    "axist": [("axist.min.css", ("gh", "src/index.css"), True)],
    "bahunya": [("bahunya.min.css", ("gh", "dist/bahunya.min.css"), False)],
    "bamboo": [("bamboo.min.css", ("gh", "dist/bamboo.min.css"), False)],
    "barecss": [("barecss.min.css", ("gh", "css/bare.min.css"), False)],
    "basiccss": [("basiccss.min.css", ("gh", "css/basic.min.css"), False)],
    "blades": [("blades.min.css", ("gh", "css/blades.min.css"), False)],
    "bolt": [("bolt.min.css", ("gh", "bolt.min.css"), False)],
    "bullframe": [("bullframe.min.css", ("gh", "dist/css/bullframe-classless.min.css"), False)],
    "chimeracss": [("chimeracss.min.css", ("gh", "chimera-css/build/chimera.css"), True)],
    "chota": [("chota.min.css", ("gh", "dist/chota.min.css"), False)],
    "classlesscss": [("classlesscss.min.css", ("gh", "docs/classless.css"), True)],
    "concrete": [("concrete.min.css", ("gh", "concrete.min.css"), False)],
    "devcss": [("devcss.min.css", ("gh", "dev.css"), True)],
    "downstyler": [("downstyler.min.css", ("gh", "downstyler.css"), True)],
    "fylgja": [
        ("fylgja-tokens.min.css", ("gh", "tokens/css/index.min.css"), False),
        ("fylgja-base.min.css", ("gh", "base/index.min.css"), False),
        ("fylgja-theme.min.css", ("gh", "base/theme.css"), True),
        ("fylgja-control.min.css", ("gh", "base/form-class-less.css"), True),
        ("fylgja-utilities.min.css", ("gh", "utilities/index.min.css"), False),
    ],
    "holiday": [("holiday.min.css", ("gh", "dist/holiday.css"), True)],
    "latex": [("latex.min.css", ("gh", "latex.css"), True)],
    "magick": [("magick.min.css", ("gh", "magick.min.css"), False)],
    "markdownair": [("markdownair.min.css", ("gh", "css/air.css"), True)],
    "markdownmodest": [("markdownmodest.min.css", ("gh", "css/modest.css"), True)],
    "markdownretro": [("markdownretro.min.css", ("gh", "css/retro.css"), True)],
    "markdownsplendor": [("markdownsplendor.min.css", ("gh", "css/splendor.min.css"), False)],
    "marx": [("marx.min.css", ("gh", "css/marx.min.css"), False)],
    "mercury": [("mercury.min.css", ("gh", "dist/mercury.min.css"), False)],
    "micss": [("micss.min.css", ("gh", "mi.css/style.css"), True)],
    "minicss": [("minicss.min.css", ("gh", "dist/mini-default.min.css"), False)],
    "mvp": [("mvp.min.css", ("gh", "mvp.css"), True)],
    "newcss": [("newcss.min.css", ("gh", "new.css"), True)],
    "nimble": [("nimble.min.css", ("url", "https://leftium.github.io/nimble.css/dist/nimble.css"), True)],
    "noclass": [("noclass.min.css", ("gh", "docs/css/no-class.min.css"), False)],
    "pico": [("pico.min.css", ("gh", "css/pico.classless.min.css"), False)],
    "picnic": [("picnic.min.css", ("gh", "picnic.min.css"), False)],
    "ridge": [("ridge.min.css", ("gh", "ridge.css"), True)],
    "sakura": [("sakura.min.css", ("gh", "css/sakura.css"), True)],
    "shadcn": [("shadcn.min.css", ("gh", "dist/shadcn-classless.css"), True)],
    "simple": [("simple.min.css", ("gh", "simple.min.css"), False)],
    "spcss": [("spcss.min.css", ("gh", "sp.min.css"), False)],
    "stylecss": [("stylecss.min.css", ("url", "https://ungoldman.com/style.css/site.css"), True)],
    # Original repo vasanthv/stylize.css is deleted; last public GitHub copy is a fork.
    "stylize": [("stylize.min.css", ("url", "https://raw.githubusercontent.com/gadenbuie/stylize.css/master/stylize.min.css"), False)],
    "sumi": [("sumi.min.css", ("gh", "sumi.min.css"), False)],
    "tacit": [("tacit.min.css", ("gh", "dist/tacit-css.min.css"), False)],
    "tinycss": [("tinycss.min.css", ("gh", "dist/tiny.css"), True)],
    "ttycss": [("ttycss.min.css", ("gh", "full.css"), True)],
    "tufte": [("tufte.min.css", ("gh", "tufte.min.css"), False)],
    "w3ccore": [("w3ccore.min.css", ("url", "https://www.w3.org/StyleSheets/Core/Swiss"), True)],
    "water": [("water.min.css", ("url", "https://watercss.kognise.dev/water.css/water.min.css"), False)],
    "wing": [("wing.min.css", ("gh", "dist/wing.min.css"), False)],
    "writ": [("writ.min.css", ("gh", "writ.min.css"), False)],
    "yorha": [("yorha.min.css", ("gh", "dist/yorha.min.css"), False)],
    "barrel": [("barrel.min.css", ("gh", "css/barrel.css"), True)],
    "matcha": [("matcha.min.css", ("url", "https://matcha.mizu.sh/matcha.css"), True)],
    "milligram": [("milligram.min.css", ("gh", "dist/milligram.min.css"), False)],
    "missing": [("missing.min.css", ("url", "https://missing.style/dist/missing.css"), True)],
    "mono": [("mono.min.css", ("gh", "mono.css"), True)],
    "sasszero": [("sasszero.min.css", ("sass", ["sass-zero/base", "sass-zero/utilities", "sass-zero/breadboard"]), True)],
    # Local, hand-maintained files: size only, no download.
    "materia": [("materia.css", ("local", "css/materia.css"), False)],
    "pure": [("pure.classless.css", ("local", "css/pure.classless.css"), False)],
}


def fetch(source: tuple, meta: dict) -> bytes:
    kind = source[0]
    if kind == "gh":
        url = f"https://raw.githubusercontent.com/{meta['github']}/{meta['ref']}/{source[1]}"
        try:
            return http_get(url, proxy=False)
        except Exception:  # noqa: BLE001
            return http_get(url, proxy=True)
    if kind == "url":
        try:
            return http_get(source[1], proxy=True)
        except Exception:  # noqa: BLE001
            return http_get(source[1], proxy=False)
    if kind == "npm":
        return fetch_npm(source[1], source[2])
    raise ValueError(kind)


def fetch_npm(pkg: str, member: str) -> bytes:
    reg = json.loads(http_get(f"https://registry.npmjs.org/{pkg}", proxy=True))
    tarball = reg["versions"][reg["dist-tags"]["latest"]]["dist"]["tarball"]
    blob = http_get(tarball, proxy=True)
    with tempfile.TemporaryFile() as fh:
        fh.write(blob)
        fh.seek(0)
        with tarfile.open(fileobj=fh, mode="r:gz") as tar:
            for info in tar.getmembers():
                if info.name.split("/", 1)[-1] == member:
                    return tar.extractfile(info).read()
    raise FileNotFoundError(f"{pkg}: {member} not in tarball")


def build_sass(entries: list[str], meta: dict) -> bytes:
    """Compile the project's own entry points (official `*= require` order)."""
    repo_dir = TMP / "repos" / meta["slug"]
    subprocess.run(["git", "-C", str(repo_dir), "checkout", "--quiet", "HEAD", "--", "."],
                   check=True, capture_output=True, text=True, timeout=300)
    assets = repo_dir / "app" / "assets" / "stylesheets"
    entry_file = TMP / "sasszero-entry.scss"
    entry_file.write_text("".join(f'@import "{name}";\n' for name in entries), encoding="utf-8")
    out = TMP / "sasszero.css"
    proc = subprocess.run(
        [NODE, str(SASS), "--no-source-map", f"--load-path={assets}", str(entry_file), str(out)],
        cwd=repo_dir, capture_output=True, text=True, env=dict(os.environ),
    )
    if proc.returncode != 0:
        raise RuntimeError(f"sass failed: {proc.stderr.strip()[:500]}")
    return out.read_bytes()


def minify_css(data: bytes) -> bytes:
    with tempfile.TemporaryDirectory() as tmp:
        src, dst = Path(tmp) / "in.css", Path(tmp) / "out.css"
        src.write_bytes(data)
        proc = subprocess.run(
            [NODE, str(ESBUILD), str(src), "--minify", "--log-level=error", f"--outfile={dst}"],
            capture_output=True, text=True,
        )
        if proc.returncode != 0:
            raise RuntimeError(f"esbuild failed: {proc.stderr.strip()[:500]}")
        return dst.read_bytes()


def main() -> None:
    metas = {p["slug"]: p for p in json.loads((TMP / "meta.json").read_text(encoding="utf-8"))}
    only = set(sys.argv[1:])
    CSS_DIR.mkdir(exist_ok=True)
    records = []
    for slug, entries in SPEC.items():
        if only and slug not in only:
            continue
        meta = metas[slug]
        for name, source, do_minify in entries:
            rec = {"slug": slug, "file": name, "source": source[0], "minified": None, "error": None}
            try:
                if source[0] == "local":
                    data = (CSS_DIR / name).read_bytes()
                elif source[0] == "sass":
                    data = build_sass(source[1], meta)
                else:
                    data = fetch(source, meta)
                if len(data) < 200:
                    raise ValueError(f"suspiciously small payload ({len(data)} bytes)")
                if do_minify:
                    data = minify_css(data)
                    rec["minified"] = "esbuild"
                    (CSS_DIR / name).write_bytes(data)
                elif source[0] != "local":
                    (CSS_DIR / name).write_bytes(data)
                rec["bytes"] = len(data)
                print(f"[ok ] {slug:<16} {name:<26} {len(data):>7} B  ({source[0]})", flush=True)
            except Exception as exc:  # noqa: BLE001
                rec["error"] = f"{type(exc).__name__}: {exc}"[:400]
                print(f"[ERR] {slug:<16} {name:<26} {rec['error']}", flush=True)
            records.append(rec)
    out_path = TMP / "downloaded.json"
    if only and out_path.exists():
        previous = json.loads(out_path.read_text(encoding="utf-8"))
        fresh = {(r["slug"], r["file"]): r for r in records}
        merged = [fresh.get((r["slug"], r["file"]), r) for r in previous]
        seen = {(r["slug"], r["file"]) for r in previous}
        merged += [r for r in records if (r["slug"], r["file"]) not in seen]
        records = merged
    out_path.write_text(json.dumps(records, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()

