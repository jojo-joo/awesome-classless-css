# Classless CSS — 对比测试

同一份无 class 的 HTML 页面（表格、排版、表单控件、模态框、折叠、进度条……），
用 60 个 classless / class-light CSS 框架轮流渲染，对比它们的默认样式。

- 在线预览：直接用浏览器打开 `index.html`（完整样式表都在 `css/` 本地，无需服务器，也无需联网）。
- 顶栏中间实时显示当前框架的 `名称 · ★星数 · 版本 · 文件大小`。
- 数据来源：[dbohdan/classless-css](https://github.com/dbohdan/classless-css) 的 `data/projects.toml`（全部 56 项），
  外加 Sumi.css、Missing.css、Materia、Pure（Fylgja 本来就在该列表中）。
- 所有样式表均下载自项目**官方 GitHub 仓库的最新 Release**（无 Release 时用仓库默认分支），不使用任何 CSS CDN。
- 统一保存 `*.min.css`，不含 gzip 版本；上游只发布未压缩 CSS 的项目在本地用 esbuild 压缩。
- `css/materia.css` 与 `css/pure.classless.css` 是本地开发的样式表，不下载。

统计：classless 47 个 · class-light 9 个 · 额外 2 个 · 本地 2 个，
合计 1212192 字节（1.16 MB）。

## frameworks

`index.html` 里的 `const frameworks` 形如 `name: ['css/name.min.css', 星数, '版本', 字节数]`，
由 [`frameworks.json`](frameworks.json) 生成：

60 个框架按星数降序排列。

| # | 框架 | 项目地址 | 星数 | 版本 | 文件 | 字节数 | 类型 |
|--:|------|----------|-----:|------|-----:|-------:|------|
| 1 | Pico.css | <https://github.com/picocss/pico> | 16834 | v2.1.1 | [pico.min.css](css/pico.min.css) | 71040 | classless |
| 2 | Milligram | <https://github.com/milligram/milligram> | 10215 | v1.4.1 | [milligram.min.css](css/milligram.min.css) | 9014 | class-light |
| 3 | water.css | <https://github.com/kognise/water.css> | 8655 | master@d950cbc | [water.min.css](css/water.min.css) | 22668 | classless |
| 4 | Tufte CSS | <https://github.com/edwardtufte/tufte-css> | 6585 | gh-pages@b5d7b7b | [tufte.min.css](css/tufte.min.css) | 6946 | classless |
| 5 | MVP.css | <https://github.com/andybrewer/mvp> | 5129 | v1.18 | [mvp.min.css](css/mvp.min.css) | 8171 | classless |
| 6 | Simple.css | <https://github.com/kevquirk/simple.css> | 5020 | v2.3.7 | [simple.min.css](css/simple.min.css) | 9429 | classless |
| 7 | sakura | <https://github.com/oxalorg/sakura> | 4393 | v1.5.1 | [sakura.min.css](css/sakura.min.css) | 3074 | classless |
| 8 | new.css | <https://github.com/xz/new.css> | 4051 | v1.1.3 | [newcss.min.css](css/newcss.min.css) | 4477 | classless |
| 9 | Picnic CSS | <https://github.com/franciscop/picnic> | 3879 | master@c05e916 | [picnic.min.css](css/picnic.min.css) | 39512 | class-light |
| 10 | mini.css | <https://github.com/Chalarangelo/mini.css> | 2948 | v3.0.1 | [minicss.min.css](css/minicss.min.css) | 46887 | class-light |
| 11 | Wing | <https://github.com/kbrsh/wing> | 1991 | master@5792c1c | [wing.min.css](css/wing.min.css) | 5978 | class-light |
| 12 | matcha.css | <https://github.com/lowlighter/matcha> | 1942 | v3.0.0 | [matcha.min.css](css/matcha.min.css) | 37417 | class-light |
| 13 | tacit | <https://github.com/yegor256/tacit> | 1879 | v1.9.7 | [tacit.min.css](css/tacit.min.css) | 6557 | classless |
| 14 | Marx | <https://github.com/mblode/marx> | 1710 | v5.3.2 | [marx.min.css](css/marx.min.css) | 16979 | classless |
| 15 | Chota | <https://github.com/jenil/chota> | 1550 | v0.8.1 | [chota.min.css](css/chota.min.css) | 18547 | class-light |
| 16 | Almond.CSS | <https://github.com/alvaromontoro/almond.css> | 1169 | v1.2.2 | [almond.min.css](css/almond.min.css) | 20233 | classless |
| 17 | magick.css | <https://github.com/wintermute-cell/magick.css> | 1040 | master@cdec42a | [magick.min.css](css/magick.min.css) | 6594 | classless |
| 18 | SPCSS | <https://github.com/susam/spcss> | 970 | main@ebb5197 | [spcss.min.css](css/spcss.min.css) | 1369 | classless |
| 19 | Missing.css | <https://github.com/bigskysoftware/missing> | 797 | dev@b74e1c0 | [missing.min.css](css/missing.min.css) | 61364 | extra |
| 20 | Basic.css | <https://github.com/vladocar/Basic.css> | 686 | master@681d40a | [basiccss.min.css](css/basiccss.min.css) | 2258 | classless |
| 21 | concrete.css | <https://github.com/louismerlin/concrete.css> | 633 | v3.0.0 | [concrete.min.css](css/concrete.min.css) | 2894 | classless |
| 22 | Bolt.css | <https://github.com/tbolt/boltcss> | 586 | v1.0.1 | [bolt.min.css](css/bolt.min.css) | 7888 | classless |
| 23 | Writ | <https://github.com/programble/writ> | 466 | v1.0.4 | [writ.min.css](css/writ.min.css) | 2228 | classless |
| 24 | Blades | <https://github.com/anyblades/blades> | 385 | v3.1.0-beta.6 | [blades.min.css](css/blades.min.css) | 76910 | classless |
| 25 | YoRHa | <https://github.com/metakirby5/yorha> | 330 | master@b575933 | [yorha.min.css](css/yorha.min.css) | 7939 | classless |
| 26 | Bahunya | <https://github.com/Kimeiga/bahunya> | 312 | master@4c92348 | [bahunya.min.css](css/bahunya.min.css) | 19048 | classless |
| 27 | Bamboo CSS | <https://github.com/rilwis/bamboo> | 283 | master@f7fdb9b | [bamboo.min.css](css/bamboo.min.css) | 5280 | classless |
| 28 | Classless.css | <https://github.com/emareg/classlesscss> | 274 | v1.1 | [classlesscss.min.css](css/classlesscss.min.css) | 9223 | classless |
| 29 | Sumi.css | <https://github.com/vladocar/Sumi.css> | 190 | main@d823a5f | [sumi.min.css](css/sumi.min.css) | 28245 | extra |
| 30 | Markdown CSS — Splendor | <https://github.com/markdowncss/splendor> | 180 | master@40db295 | [markdownsplendor.min.css](css/markdownsplendor.min.css) | 1888 | classless |
| 31 | LatexCSS | <https://github.com/davidrzs/latexcss> | 178 | master@9264a50 | [latex.min.css](css/latex.min.css) | 304731 | classless |
| 32 | holiday.css | <https://github.com/EvgenyOrekhov/holiday.css> | 164 | v0.11.6 | [holiday.min.css](css/holiday.min.css) | 19210 | classless |
| 33 | ridge.css | <https://github.com/swlkr/ridgecss> | 154 | v0.2.0 | [ridge.min.css](css/ridge.min.css) | 19969 | classless |
| 34 | Markdown CSS — Modest | <https://github.com/markdowncss/modest> | 132 | master@f16599c | [markdownmodest.min.css](css/markdownmodest.min.css) | 1982 | classless |
| 35 | Markdown CSS — Retro | <https://github.com/markdowncss/retro> | 129 | master@3171af7 | [markdownretro.min.css](css/markdownretro.min.css) | 1654 | classless |
| 36 | BareCSS | <https://github.com/longsien/BareCSS> | 117 | v1.1.0 | [barecss.min.css](css/barecss.min.css) | 18639 | classless |
| 37 | Fylgja | <https://github.com/fylgja/fylgja> | 116 | v2.2.1 | [fylgja.min.css](css/fylgja.min.css) | 44261 | classless |
| 38 | axist | <https://github.com/ruanmartinelli/axist> | 111 | v1.0.0 | [axist.min.css](css/axist.min.css) | 6872 | classless |
| 39 | Markdown CSS — Air | <https://github.com/markdowncss/air> | 107 | master@f31f83d | [markdownair.min.css](css/markdownair.min.css) | 1676 | classless |
| 40 | style.css | <https://github.com/ungoldman/style.css> | 81 | v2.0.0-0 | [stylecss.min.css](css/stylecss.min.css) | 7209 | classless |
| 41 | attriCSS | <https://github.com/raj457036/attriCSS> | 58 | master@3160620 | [attricss.min.css](css/attricss.min.css) | 4292 | classless |
| 42 | mono | <https://github.com/artalar/mono> | 51 | main@f3c00aa | [mono.min.css](css/mono.min.css) | 10637 | class-light |
| 43 | bullframe.css | <https://github.com/marcop135/bullframe.css> | 47 | v6.4.2 | [bullframe.min.css](css/bullframe.min.css) | 18873 | classless |
| 44 | Tiny.css | <https://github.com/ihsan6133/tiny.css> | 46 | main@27b0410 | [tinycss.min.css](css/tinycss.min.css) | 5281 | classless |
| 45 | Downstyler | <https://github.com/waldyrious/downstyler> | 40 | master@4c681a4 | [downstyler.min.css](css/downstyler.min.css) | 1708 | classless |
| 46 | no-class.css | <https://github.com/davidpaulsson/no-class> | 40 | v1.0.1 | [noclass.min.css](css/noclass.min.css) | 6953 | classless |
| 47 | SASS-ZERO (Breadboard) | <https://github.com/lazaronixon/sass-zero> | 39 | v1.5.5 | [sasszero.min.css](css/sasszero.min.css) | 12913 | class-light |
| 48 | dev.css | <https://github.com/intergrav/dev.css> | 38 | main@8fa5836 | [devcss.min.css](css/devcss.min.css) | 5448 | classless |
| 49 | MercuryCSS | <https://github.com/wmeredith/MercuryCSS> | 31 | master@173e953 | [mercury.min.css](css/mercury.min.css) | 7862 | classless |
| 50 | ChimeraCSS | <https://github.com/ChimeraCSS/ChimeraCSS> | 25 | main@b3f0bad | [chimeracss.min.css](css/chimeracss.min.css) | 5313 | classless |
| 51 | nimble.css | <https://github.com/Leftium/nimble.css> | 10 | v0.24.1 | [nimble.min.css](css/nimble.min.css) | 31506 | classless |
| 52 | tty.css | <https://github.com/piranna/tty.css> | 10 | master@d35d0dc | [ttycss.min.css](css/ttycss.min.css) | 4478 | classless |
| 53 | shadcn-classless (Nandaleio) | <https://github.com/Nandaleio/shadcn-classless> | 8 | main@b3f94b5 | [shadcn.min.css](css/shadcn.min.css) | 20650 | classless |
| 54 | Barrel.css | <https://github.com/EternityForest/barrel.css> | 7 | v0.5.2 | [barrel.min.css](css/barrel.min.css) | 34971 | class-light |
| 55 | mi.css | <https://github.com/FelipeIzolan/mi> | 2 | main@16c2576 | [micss.min.css](css/micss.min.css) | 722 | classless |
| 56 | awsm.css | <https://www.npmjs.com/package/awsm.css> | 0 | v3.0.7 | [awsm.min.css](css/awsm.min.css) | 13451 | classless |
| 57 | Materia (local) | <https://github.com/jojo-joo/classless-form> | 0 | local | [materia.css](css/materia.css) | 6220 | local |
| 58 | Pure Classless (local) | <https://github.com/jojo-joo/classless-form> | 0 | local | [pure.classless.css](css/pure.classless.css) | 20473 | local |
| 59 | Stylize.css | <https://github.com/gadenbuie/stylize.css> | 0 | v1.0.1 | [stylize.min.css](css/stylize.min.css) | 4812 | classless |
| 60 | W3C Core Styles | <https://www.w3.org/StyleSheets/Core/Overview> | 0 | 1998 | [w3ccore.min.css](css/w3ccore.min.css) | 9369 | classless |

星数取自 GitHub 仓库主页的 `stargazers_count`；版本为最新 Release 的 tag，没有 Release 的项目显示 `分支@commit`。
文件大小为 `css/` 目录中实际文件的字节数。

## 说明

- **本地压缩（27 个）**：attriCSS、axist、Barrel.css、ChimeraCSS、Classless.css、dev.css、Downstyler、holiday.css、LatexCSS、Markdown CSS — Air、Markdown CSS — Modest、Markdown CSS — Retro、matcha.css、mi.css、Missing.css、mono、MVP.css、new.css、nimble.css、ridge.css、sakura、SASS-ZERO (Breadboard)、shadcn-classless (Nandaleio)、style.css、Tiny.css、tty.css、W3C Core Styles。这些项目上游没有提交 `.min.css`，
  下载官方 `.css` 后用 esbuild 压缩，`frameworks.json` 中记为 `"minified": "esbuild"`。
- **awsm.css**：原官网与 GitHub 仓库均已下线，取自官方 npm 包 awsm.css@3.0.7 的 dist/awsm.min.css
- **Stylize.css**：原仓库 vasanthv/stylize.css 已删除，取自最后公开的 GitHub fork（stylize.min.css 原文件）
- **W3C Core Styles**：W3C Core Styles 无 .min 构建，取官方 Swiss 主题并由本地 esbuild 压缩
- **Materia (local)**：本地开发的样式表，不下载
- **Pure Classless (local)**：本地开发的样式表，不下载
- **Fylgja**：官方 5 个包按 tokens → base → theme → form-class-less → utilities 顺序拼接
- **SASS-ZERO (Breadboard)**：官方仓库只有 SCSS，按 README 的 base → utilities → breadboard 顺序用 dart-sass 编译

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
