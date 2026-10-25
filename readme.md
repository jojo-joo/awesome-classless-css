# Classless CSS — Comparison Test

One and the same HTML page, with no classes at all (tables, typography, form controls,
modal, accordion, progress bar, ...), is rendered by 60 classless / class-light CSS
frameworks in turn, so their default styles can be compared.

- Live preview: open `index.html` directly in a browser (all stylesheets are local in
  `css/`, so neither a server nor a network connection is needed).
- The top bar shows the current framework's `name · ★ stars · version · file size` in real time.
- Data source: `data/projects.toml` from [dbohdan/classless-css](https://github.com/dbohdan/classless-css)
  (all 56 entries), plus Sumi.css, Missing.css, Materia and Pure (Fylgja was already on that list).
- Every stylesheet was downloaded from the project's **official GitHub repository latest
  release** (default branch when there is no release); no CSS CDN is used anywhere.
- Everything is stored as `*.min.css`, without gzip variants; projects that only ship
  unminified CSS were minified locally with esbuild.
- `css/materia.css` and `css/pure.classless.css` are developed locally and are not downloaded.

Stats: 47 classless · 9 class-light · 2 extra · 2 local, 1,212,192 bytes (1.16 MB) in total.

## Frameworks

`const frameworks` in `index.html` looks like `name: ['css/name.min.css', stars, 'version', bytes]`
and is generated from [`frameworks.json`](frameworks.json):

The 60 frameworks below are sorted by stars, descending.

The 22 columns from `table` to `score` are empty test slots for feature checks: mark a cell
when testing how a framework handles that kind of content (✅ pass / ❌ fail).

| # | Framework | Stars | Version | Bytes | table | typography | lists | picture | input | select | radio | checkbox | switch | color | range | validation | button | accordions | progress | mobile | theme | alignment | appearance | size | stars | score |
|--:|------|------:|------|------:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | [Pico.css](https://github.com/picocss/pico) | 16834 | v2.1.1 | 71040 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 | [Milligram](https://github.com/milligram/milligram) | 10215 | v1.4.1 | 9014 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | [water.css](https://github.com/kognise/water.css) | 8655 | master@d950cbc | 22668 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | [Tufte CSS](https://github.com/edwardtufte/tufte-css) | 6585 | gh-pages@b5d7b7b | 6946 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | [MVP.css](https://github.com/andybrewer/mvp) | 5129 | v1.18 | 8171 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | [Simple.css](https://github.com/kevquirk/simple.css) | 5020 | v2.3.7 | 9429 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | [sakura](https://github.com/oxalorg/sakura) | 4393 | v1.5.1 | 3074 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 | [new.css](https://github.com/xz/new.css) | 4051 | v1.1.3 | 4477 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | [Picnic CSS](https://github.com/franciscop/picnic) | 3879 | master@c05e916 | 39512 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 | [mini.css](https://github.com/Chalarangelo/mini.css) | 2948 | v3.0.1 | 46887 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | [Wing](https://github.com/kbrsh/wing) | 1991 | master@5792c1c | 5978 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 12 | [matcha.css](https://github.com/lowlighter/matcha) | 1942 | v3.0.0 | 37417 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 13 | [tacit](https://github.com/yegor256/tacit) | 1879 | v1.9.7 | 6557 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 14 | [Marx](https://github.com/mblode/marx) | 1710 | v5.3.2 | 16979 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 15 | [Chota](https://github.com/jenil/chota) | 1550 | v0.8.1 | 18547 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 16 | [Almond.CSS](https://github.com/alvaromontoro/almond.css) | 1169 | v1.2.2 | 20233 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 17 | [magick.css](https://github.com/wintermute-cell/magick.css) | 1040 | master@cdec42a | 6594 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 18 | [SPCSS](https://github.com/susam/spcss) | 970 | main@ebb5197 | 1369 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 19 | [Missing.css](https://github.com/bigskysoftware/missing) | 797 | dev@b74e1c0 | 61364 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 20 | [Basic.css](https://github.com/vladocar/Basic.css) | 686 | master@681d40a | 2258 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 21 | [concrete.css](https://github.com/louismerlin/concrete.css) | 633 | v3.0.0 | 2894 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 22 | [Bolt.css](https://github.com/tbolt/boltcss) | 586 | v1.0.1 | 7888 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 23 | [Writ](https://github.com/programble/writ) | 466 | v1.0.4 | 2228 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 24 | [Blades](https://github.com/anyblades/blades) | 385 | v3.1.0-beta.6 | 76910 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 25 | [YoRHa](https://github.com/metakirby5/yorha) | 330 | master@b575933 | 7939 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 26 | [Bahunya](https://github.com/Kimeiga/bahunya) | 312 | master@4c92348 | 19048 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 27 | [Bamboo CSS](https://github.com/rilwis/bamboo) | 283 | master@f7fdb9b | 5280 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 28 | [Classless.css](https://github.com/emareg/classlesscss) | 274 | v1.1 | 9223 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 29 | [Sumi.css](https://github.com/vladocar/Sumi.css) | 190 | main@d823a5f | 28245 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 30 | [Markdown CSS — Splendor](https://github.com/markdowncss/splendor) | 180 | master@40db295 | 1888 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 31 | [LatexCSS](https://github.com/davidrzs/latexcss) | 178 | master@9264a50 | 304731 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 32 | [holiday.css](https://github.com/EvgenyOrekhov/holiday.css) | 164 | v0.11.6 | 19210 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 33 | [ridge.css](https://github.com/swlkr/ridgecss) | 154 | v0.2.0 | 19969 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 34 | [Markdown CSS — Modest](https://github.com/markdowncss/modest) | 132 | master@f16599c | 1982 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 35 | [Markdown CSS — Retro](https://github.com/markdowncss/retro) | 129 | master@3171af7 | 1654 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 36 | [BareCSS](https://github.com/longsien/BareCSS) | 117 | v1.1.0 | 18639 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 37 | [Fylgja](https://github.com/fylgja/fylgja) | 116 | v2.2.1 | 44261 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 38 | [axist](https://github.com/ruanmartinelli/axist) | 111 | v1.0.0 | 6872 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 39 | [Markdown CSS — Air](https://github.com/markdowncss/air) | 107 | master@f31f83d | 1676 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 40 | [style.css](https://github.com/ungoldman/style.css) | 81 | v2.0.0-0 | 7209 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 41 | [attriCSS](https://github.com/raj457036/attriCSS) | 58 | master@3160620 | 4292 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 42 | [mono](https://github.com/artalar/mono) | 51 | main@f3c00aa | 10637 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 43 | [bullframe.css](https://github.com/marcop135/bullframe.css) | 47 | v6.4.2 | 18873 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 44 | [Tiny.css](https://github.com/ihsan6133/tiny.css) | 46 | main@27b0410 | 5281 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 45 | [Downstyler](https://github.com/waldyrious/downstyler) | 40 | master@4c681a4 | 1708 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 46 | [no-class.css](https://github.com/davidpaulsson/no-class) | 40 | v1.0.1 | 6953 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 47 | [SASS-ZERO (Breadboard)](https://github.com/lazaronixon/sass-zero) | 39 | v1.5.5 | 12913 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 48 | [dev.css](https://github.com/intergrav/dev.css) | 38 | main@8fa5836 | 5448 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 49 | [MercuryCSS](https://github.com/wmeredith/MercuryCSS) | 31 | master@173e953 | 7862 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 50 | [ChimeraCSS](https://github.com/ChimeraCSS/ChimeraCSS) | 25 | main@b3f0bad | 5313 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 51 | [nimble.css](https://github.com/Leftium/nimble.css) | 10 | v0.24.1 | 31506 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 52 | [tty.css](https://github.com/piranna/tty.css) | 10 | master@d35d0dc | 4478 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 53 | [shadcn-classless (Nandaleio)](https://github.com/Nandaleio/shadcn-classless) | 8 | main@b3f94b5 | 20650 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 54 | [Barrel.css](https://github.com/EternityForest/barrel.css) | 7 | v0.5.2 | 34971 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 55 | [mi.css](https://github.com/FelipeIzolan/mi) | 2 | main@16c2576 | 722 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 56 | [awsm.css](https://www.npmjs.com/package/awsm.css) | 0 | v3.0.7 | 13451 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 57 | [Materia (local)](https://github.com/jojo-joo/classless-form) | 0 | local | 6220 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 58 | [Pure Classless (local)](https://github.com/jojo-joo/classless-form) | 0 | local | 20473 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 59 | [Stylize.css](https://github.com/gadenbuie/stylize.css) | 0 | v1.0.1 | 4812 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 60 | [W3C Core Styles](https://www.w3.org/StyleSheets/Core/Overview) | 0 | 1998 | 9369 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Stars come from `stargazers_count` on the GitHub repository page; the version is the latest
release tag, or `branch@commit` for projects without releases.
Bytes are the exact size of the file in the `css/` directory.

## Notes

- **Locally minified (27)**: attriCSS, axist, Barrel.css, ChimeraCSS, Classless.css, dev.css,
  Downstyler, holiday.css, LatexCSS, Markdown CSS — Air, Markdown CSS — Modest,
  Markdown CSS — Retro, matcha.css, mi.css, Missing.css, mono, MVP.css, new.css, nimble.css,
  ridge.css, sakura, SASS-ZERO (Breadboard), shadcn-classless (Nandaleio), style.css, Tiny.css,
  tty.css, W3C Core Styles. These projects do not ship a `.min.css` upstream, so their official
  `.css` was downloaded and minified with esbuild; `frameworks.json` records
  `"minified": "esbuild"` for them.
- **awsm.css**: both the original website and the GitHub repository are offline; taken from
  `dist/awsm.min.css` of the official npm package awsm.css@3.0.7.
- **Stylize.css**: the original repository vasanthv/stylize.css has been deleted; taken from
  the last public GitHub fork (the original stylize.min.css file).
- **W3C Core Styles**: W3C Core Styles has no `.min` build; the official Swiss theme was used
  and minified locally with esbuild.
- **Materia (local)**: locally developed stylesheet, not downloaded.
- **Pure Classless (local)**: locally developed stylesheet, not downloaded.
- **Fylgja**: the five official packages concatenated as tokens → base → theme →
  form-class-less → utilities.
- **SASS-ZERO (Breadboard)**: the official repository only contains SCSS; compiled with
  dart-sass in the order base → utilities → breadboard, as described in its README.

## Regenerating

```bash
python tools/collect.py   # reads data/projects.toml, queries the latest release / stars, shallow-clones the file tree
python tools/build.py     # downloads into css/, minifies locally when needed
python tools/gen.py       # generates frameworks.json, the const in index.html, and this table
```

Requirements: Python 3.11+, Node 22+ (local minification / SCSS compilation). Install once in `.tmp/minify`:

```bash
npm --prefix .tmp/minify i esbuild sass
```
