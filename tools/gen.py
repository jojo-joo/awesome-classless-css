#!/usr/bin/env python3
"""Stage 3: generate the page data, index.html block and the markdown table.

Outputs
  css/fylgja.min.css   the five official Fylgja packages, concatenated in the
                       documented load order (one stylesheet per framework)
  frameworks.json      the source of truth: title, project URL, stars, version,
                       file, bytes, upstream origin
  index.html           regenerated `const frameworks = {...}` block + meta line
  readme.md            markdown table of every framework
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS = ROOT / "css"
TMP = ROOT / ".tmp"

FYLGJA_ORDER = [
    "fylgja-tokens.min.css",
    "fylgja-base.min.css",
    "fylgja-theme.min.css",
    "fylgja-control.min.css",
    "fylgja-utilities.min.css",
]

# Project homepage overrides / notes for sources that are gone or npm-only.
HOMEPAGE = {
    "awsm": "https://www.npmjs.com/package/awsm.css",
    "stylize": "https://github.com/gadenbuie/stylize.css",
    "w3ccore": "https://www.w3.org/StyleSheets/Core/Overview",
}
NOTE = {
    "awsm": "原官网与 GitHub 仓库均已下线，取自官方 npm 包 awsm.css@3.0.7 的 dist/awsm.min.css",
    "stylize": "原仓库 vasanthv/stylize.css 已删除，取自最后公开的 GitHub fork（stylize.min.css 原文件）",
    "w3ccore": "W3C Core Styles 无 .min 构建，取官方 Swiss 主题并由本地 esbuild 压缩",
    "materia": "本地开发的样式表，不下载",
    "pure": "本地开发的样式表，不下载",
    "fylgja": "官方 5 个包按 tokens → base → theme → form-class-less → utilities 顺序拼接",
    "sasszero": "官方仓库只有 SCSS，按 README 的 base → utilities → breadboard 顺序用 dart-sass 编译",
}
# For sources with no tag/commit of their own (deleted repos, npm-only, W3C).
VERSION_OVERRIDE = {"awsm": "v3.0.7", "stylize": "v1.0.1", "w3ccore": "1998"}


def human(n: int) -> str:
    return f"{n / 1024:.1f} KB" if n >= 1024 else f"{n} B"


def main() -> None:
    metas = {p["slug"]: p for p in json.loads((TMP / "meta.json").read_text(encoding="utf-8"))}
    dl = {r["slug"]: r for r in json.loads((TMP / "downloaded.json").read_text(encoding="utf-8")) if not r["error"]}

    # Fylgja: 5 official packages -> one stylesheet in the documented order.
    parts = [CSS / name for name in FYLGJA_ORDER]
    missing = [p.name for p in parts if not p.exists()]
    if missing:
        raise SystemExit(f"missing fylgja parts: {missing}")
    combined = b"\n".join(p.read_bytes() for p in parts)
    (CSS / "fylgja.min.css").write_bytes(combined)

    rows = []
    for slug, meta in metas.items():
        if slug not in dl:
            raise SystemExit(f"no download record for {slug}")
        file = "fylgja.min.css" if slug == "fylgja" else dl[slug]["file"]
        size = (CSS / file).stat().st_size
        tag = meta.get("tag")
        if slug in VERSION_OVERRIDE:
            version = VERSION_OVERRIDE[slug]
        elif tag:
            version = tag if tag.startswith("v") else f"v{tag}"
        elif meta.get("local"):
            version = "local"
        else:
            version = f"{meta['ref']}@{str(meta['commit'])[:7]}"
        homepage = HOMEPAGE.get(slug) or (
            f"https://github.com/{meta['github']}" if meta["github"] else meta.get("website") or meta.get("demo", "")
        )
        rows.append(
            {
                "slug": slug,
                "title": meta["title"],
                "kind": meta["kind"],
                "homepage": homepage,
                "demo": meta.get("demo", ""),
                "stars": meta.get("stars") or 0,
                "version": version,
                "file": f"css/{file}",
                "bytes": size,
                "downloaded": dl[slug]["source"] != "local",
                "upstream": {
                    "repo": meta["github"],
                    "ref": meta.get("ref"),
                    "tag": tag,
                    "commit": meta.get("commit"),
                    "minified": dl[slug].get("minified"),
                },
                "note": NOTE.get(slug, ""),
            }
        )

    rows.sort(key=lambda r: r["slug"])
    (ROOT / "frameworks.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")

    # ---- index.html: replace the data block --------------------------------
    html_path = ROOT / "index.html"
    html = html_path.read_text(encoding="utf-8")
    kind_order = {"classless": 0, "class-light": 1, "extra": 2, "local": 3}
    js_rows = sorted(rows, key=lambda r: (kind_order[r["kind"]], r["slug"]))
    lines = ["const frameworks = {"]
    kind_comment = {"classless": "Classless", "class-light": "Class-light", "extra": "额外项目", "local": "本地开发"}
    last_kind = None
    for row in js_rows:
        if row["kind"] != last_kind:
            lines.append(f"  // ===== {kind_comment[row['kind']]} =====")
            last_kind = row["kind"]
        lines.append(
            f"  {json.dumps(row['slug'])}: [{json.dumps(row['file'])}, {row['stars']}, "
            f"{json.dumps(row['version'])}, {row['bytes']}],"
        )
    lines[-1] = lines[-1].rstrip(",")
    lines.append("};")
    block = "\n".join(lines)

    start = html.index("const frameworks = {")
    end = html.index("\n};", start) + len("\n};")
    html = html[:start] + block + html[end:]

    # Replace the stale "everything goes through jsDelivr" note above the map.
    stale = re.search(r"    // Load order matters for Fylgja.*?jsDelivr 的 gh 通道代替官方直链/官网直链。\n", html, re.S)
    if stale:
        html = html[:stale.start()] + (
            "    // 数据由 tools/gen.py 生成：每个框架都是\n"
            "    //   [本地样式表, GitHub 星数, 版本, 文件字节数]\n"
            "    // 样式表已全部下载到 css/，运行时只读本地文件，不请求任何 CDN。\n"
        ) + html[stale.end():]

    # loadFramework: replace the whole region up to the next section so
    # re-running this generator is idempotent. The page's toolbar label
    # (#fw-name) carries the metadata of the active framework.
    load_start = html.index("    function loadFramework(name) {")
    load_end = html.index("    // The nav pills are generated", load_start)
    new_load = '''    function loadFramework(name) {
      document.querySelectorAll('link[data-framework]').forEach(link => link.remove());

      // Element 0 is the local stylesheet path (a list, so a framework may
      // ship more than one sheet).
      for (const url of [].concat(frameworks[name][0])) {
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = url;
        link.dataset.framework = '';
        document.head.insertBefore(link, pageStyle);
      }

      // Single place that knows the active framework, so the toolbar label can
      // never disagree with the stylesheet actually loaded.
      const [, stars, version, bytes] = frameworks[name];
      document.getElementById('fw-name').textContent = name
        + '  \\u00b7  \\u2605 ' + stars.toLocaleString('en-US')
        + '  \\u00b7  ' + version
        + '  \\u00b7  ' + (bytes / 1024).toFixed(1) + ' KB';
    }

'''
    html = html[:load_start] + new_load + html[load_end:]
    html_path.write_text(html, encoding="utf-8")

    # ---- readme.md ---------------------------------------------------------
    by_stars = sorted(rows, key=lambda r: (-r["stars"], r["slug"]))
    kind_label = {"classless": "classless", "class-light": "class-light", "extra": "extra", "local": "local"}
    table = [
        "| # | 框架 | 项目地址 | 星数 | 版本 | 文件 | 字节数 | 类型 |",
        "|--:|------|----------|-----:|------|-----:|-------:|------|",
    ]
    for i, r in enumerate(by_stars, 1):
        table.append(
            f"| {i} | {r['title']} | <{r['homepage']}> | {r['stars']} | {r['version']} "
            f"| [{r['file'].split('/')[-1]}]({r['file']}) | {r['bytes']} | {kind_label[r['kind']]} |"
        )
    total = sum(r["bytes"] for r in rows)
    counts = {k: sum(1 for r in rows if r["kind"] == k) for k in kind_label}
    local_min = [r for r in rows if r["upstream"]["minified"]]
    local_min_names = "、".join(r["title"] for r in local_min)
    notes = "\n".join(
        f"- **{metas[slug]['title']}**：{text}"
        for slug, text in NOTE.items()
        if slug in metas
    )
    readme = f"""# Classless CSS — 对比测试

同一份无 class 的 HTML 页面（表格、排版、表单控件、模态框、折叠、进度条……），
用 {len(rows)} 个 classless / class-light CSS 框架轮流渲染，对比它们的默认样式。

- 在线预览：直接用浏览器打开 `index.html`（完整样式表都在 `css/` 本地，无需服务器，也无需联网）。
- 顶栏中间实时显示当前框架的 `名称 · ★星数 · 版本 · 文件大小`。
- 数据来源：[dbohdan/classless-css](https://github.com/dbohdan/classless-css) 的 `data/projects.toml`（全部 {counts['classless'] + counts['class-light']} 项），
  外加 Sumi.css、Missing.css、Materia、Pure（Fylgja 本来就在该列表中）。
- 所有样式表均下载自项目**官方 GitHub 仓库的最新 Release**（无 Release 时用仓库默认分支），不使用任何 CSS CDN。
- 统一保存 `*.min.css`，不含 gzip 版本；上游只发布未压缩 CSS 的项目在本地用 esbuild 压缩。
- `css/materia.css` 与 `css/pure.classless.css` 是本地开发的样式表，不下载。

统计：classless {counts['classless']} 个 · class-light {counts['class-light']} 个 · 额外 {counts['extra']} 个 · 本地 {counts['local']} 个，
合计 {total} 字节（{total / 1024 / 1024:.2f} MB）。

## frameworks

`index.html` 里的 `const frameworks` 形如 `name: ['css/name.min.css', 星数, '版本', 字节数]`，
由 [`frameworks.json`](frameworks.json) 生成：

{len(rows)} 个框架按星数降序排列。

""" + "\n".join(table) + f"""

星数取自 GitHub 仓库主页的 `stargazers_count`；版本为最新 Release 的 tag，没有 Release 的项目显示 `分支@commit`。
文件大小为 `css/` 目录中实际文件的字节数。

## 说明

- **本地压缩（{len(local_min)} 个）**：{local_min_names}。这些项目上游没有提交 `.min.css`，
  下载官方 `.css` 后用 esbuild 压缩，`frameworks.json` 中记为 `"minified": "esbuild"`。
{notes}

## 重新生成

```bash
python tools/collect.py   # 读取 data/projects.toml，查询最新 Release / 星数，浅克隆取文件树
python tools/build.py     # 下载到 css/，必要时本地压缩
python tools/gen.py       # 生成 frameworks.json、index.html 的 const、本表格
```

依赖：Python 3.11+、Node 22+（本地压缩 / SCSS 编译）。首次需在 `.tmp/minify` 安装：

```bash
npm --prefix .tmp/minify i esbuild sass
```
"""
    (ROOT / "readme.md").write_text(readme, encoding="utf-8")

    print(f"{len(rows)} frameworks, {total} bytes")
    for r in rows:
        print(f"  {r['slug']:<16} {r['version']:<16} {r['bytes']:>7} B  {r['kind']}")


if __name__ == "__main__":
    main()

