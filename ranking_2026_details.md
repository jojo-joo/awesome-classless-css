
# Ranking 2026 Details

`const frameworks` in `index.html` looks like `name: ['css/name.min.css', stars, 'version', bytes]`
and is generated from [`frameworks.json`](frameworks.json):

The 60 frameworks below are sorted alphabetically, matching the `const frameworks` array.
The `stars` score is still the rank band by GitHub star count, independent of table order.

The component columns were filled by scanning each stylesheet for the selectors of that element
(✅ = the CSS has rules for it, ❌ = it has none). `switch`, `validation`, `loading` and `theme`
are attribute-only by definition: `[role=switch]`, `[aria-invalid]`, `[aria-busy]`, and a dark
theme (`prefers-color-scheme: dark` or `[data-theme]`).

`theme` is worth 5 points when ✅; `alignment` and `appearance` are the hand-made 0–5 judgements,
and `score` is their sum with the components (see [Rules](#rules), maximum 50).

| # | Framework | Stars | Version | Bytes | h1 | h2 | h3 | h4 | h5 | h6 | table | typography | lists | picture | input | select | radio | checkbox | color | range | button | accordions | progress | switch | validation | loading | theme | alignment | appearance | size | stars | score |
|--:|------|------:|------|------:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | [Almond](https://github.com/alvaromontoro/almond.css) | 1169 | v1.2.2 | 20233 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 5 | 5 | 1 | 4 | 34 |
| 2 | [attriCSS](https://github.com/raj457036/attriCSS) | 58 | master@3160620 | 4292 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 | 3 | 4 | 1 | 28 |
| 3 | [awsm](https://www.npmjs.com/package/awsm.css) | 0 | v3.0.7 | 13451 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | 4 | 2 | 2 | 0 | 26 |
| 4 | [axist](https://github.com/ruanmartinelli/axist) | 111 | v1.0.0 | 6872 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | 4 | 3 | 3 | 2 | 29 |
| 5 | [Bahunya](https://github.com/Kimeiga/bahunya) | 312 | master@4c92348 | 19048 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | 4 | 4 | 1 | 3 | 36 |
| 6 | [Bamboo](https://github.com/rilwis/bamboo) | 283 | master@f7fdb9b | 5280 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | 5 | 4 | 4 | 3 | 33 |
| 7 | [BareCSS](https://github.com/longsien/BareCSS) | 117 | v1.1.0 | 18639 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 3 | 4 | 1 | 2 | 26 |
| 8 | [Barrel](https://github.com/EternityForest/barrel.css) | 7 | v0.5.2 | 34971 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 0 | 0 | 0 | 0 | 18 |
| 9 | [Basic](https://github.com/vladocar/Basic.css) | 686 | master@681d40a | 2258 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 3 | 3 | 5 | 4 | 28 |
| 10 | [Blades](https://github.com/anyblades/blades) | 385 | v3.1.0-beta.6 | 76910 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 4 | 5 | 0 | 3 | 42 |
| 11 | [Bolt](https://github.com/tbolt/boltcss) | 586 | v1.0.1 | 7888 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 5 | 3 | 3 | 3 | 33 |
| 12 | [bullframe](https://github.com/marcop135/bullframe.css) | 47 | v6.4.2 | 18873 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | 3 | 3 | 1 | 1 | 28 |
| 13 | [ChimeraCSS](https://github.com/ChimeraCSS/ChimeraCSS) | 25 | main@b3f0bad | 5313 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 | 4 | 4 | 1 | 30 |
| 14 | [Chota](https://github.com/jenil/chota) | 1550 | v0.8.1 | 18547 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 | 4 | 2 | 4 | 28 |
| 15 | [Classless](https://github.com/emareg/classlesscss) | 274 | v1.1 | 9223 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | 4 | 3 | 2 | 3 | 26 |
| 16 | [concrete](https://github.com/louismerlin/concrete.css) | 633 | v3.0.0 | 2894 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 4 | 3 | 5 | 3 | 29 |
| 17 | [dev.css](https://github.com/intergrav/dev.css) | 38 | main@8fa5836 | 5448 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | 4 | 3 | 4 | 1 | 32 |
| 18 | [Downstyler](https://github.com/waldyrious/downstyler) | 40 | master@4c681a4 | 1708 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 | 3 | 5 | 1 | 27 |
| 19 | [Fylgja](https://github.com/fylgja/fylgja) | 116 | v2.2.1 | 44261 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | 5 | 4 | 0 | 2 | 31 |
| 20 | [holiday](https://github.com/EvgenyOrekhov/holiday.css) | 164 | v0.11.6 | 19210 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 4 | 3 | 1 | 2 | 22 |
| 21 | [LatexCSS](https://github.com/davidrzs/latexcss) | 178 | master@9264a50 | 304731 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 | 5 | 0 | 2 | 20 |
| 22 | [magick](https://github.com/wintermute-cell/magick.css) | 1040 | master@cdec42a | 6594 | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 1 | 5 | 3 | 4 | 26 |
| 23 | [MarkdownAir](https://github.com/markdowncss/air) | 107 | master@f31f83d | 1676 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | 5 | 5 | 5 | 2 | 33 |
| 24 | [MarkdownModest](https://github.com/markdowncss/modest) | 132 | master@f16599c | 1982 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | 5 | 5 | 5 | 2 | 32 |
| 25 | [MarkdownRetro](https://github.com/markdowncss/retro) | 129 | master@3171af7 | 1654 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 | 5 | 5 | 2 | 27 |
| 26 | [MarkdownSplendor](https://github.com/markdowncss/splendor) | 180 | master@40db295 | 1888 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | 5 | 4 | 5 | 3 | 33 |
| 27 | [Marx](https://github.com/mblode/marx) | 1710 | v5.3.2 | 16979 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | 4 | 5 | 2 | 4 | 41 |
| 28 | [matcha](https://github.com/lowlighter/matcha) | 1942 | v3.0.0 | 37417 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 2 | 3 | 0 | 4 | 28 |
| 29 | [Materia](https://github.com/jojo-joo/classless-form) | 0 | local | 6220 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | 5 | 4 | 3 | 0 | 21 |
| 30 | [MercuryCSS](https://github.com/wmeredith/MercuryCSS) | 31 | master@173e953 | 7862 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 5 | 4 | 3 | 1 | 28 |
| 31 | [mi](https://github.com/FelipeIzolan/mi) | 2 | main@16c2576 | 722 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 | 4 | 5 | 0 | 27 |
| 32 | [Milligram](https://github.com/milligram/milligram) | 10215 | v1.4.1 | 9014 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | 4 | 4 | 2 | 5 | 36 |
| 33 | [mini](https://github.com/Chalarangelo/mini.css) | 2948 | v3.0.1 | 46887 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 5 | 4 | 0 | 5 | 29 |
| 34 | [Missing](https://github.com/bigskysoftware/missing) | 797 | dev@b74e1c0 | 61364 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | 5 | 3 | 0 | 4 | 35 |
| 35 | [mono](https://github.com/artalar/mono) | 51 | main@f3c00aa | 10637 | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 | 3 | 2 | 1 | 25 |
| 36 | [MVP](https://github.com/andybrewer/mvp) | 5129 | v1.18 | 8171 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | 3 | 4 | 2 | 5 | 31 |
| 37 | [new](https://github.com/xz/new.css) | 4051 | v1.1.3 | 4477 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 5 | 4 | 4 | 5 | 33 |
| 38 | [nimble.css](https://github.com/Leftium/nimble.css) | 10 | v0.24.1 | 31506 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 5 | 4 | 0 | 0 | 39 |
| 39 | [no-class](https://github.com/davidpaulsson/no-class) | 40 | v1.0.1 | 6953 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | 3 | 3 | 3 | 1 | 27 |
| 40 | [Picnic](https://github.com/franciscop/picnic) | 3879 | master@c05e916 | 39512 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 5 | 5 | 0 | 5 | 32 |
| 41 | [Pico](https://github.com/picocss/pico) | 16834 | v2.1.1 | 71040 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 4 | 5 | 0 | 5 | 44 |
| 42 | [Pure](https://github.com/jojo-joo/classless-form) | 0 | local | 20473 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | 4 | 3 | 1 | 0 | 32 |
| 43 | [ridge](https://github.com/swlkr/ridgecss) | 154 | v0.2.0 | 19969 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 | 3 | 1 | 2 | 29 |
| 44 | [sakura](https://github.com/oxalorg/sakura) | 4393 | v1.5.1 | 3074 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 4 | 4 | 4 | 5 | 31 |
| 45 | [SASS-ZERO](https://github.com/lazaronixon/sass-zero) | 39 | v1.5.5 | 12913 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 5 | 3 | 2 | 1 | 28 |
| 46 | [shadcn](https://github.com/Nandaleio/shadcn-classless) | 8 | main@b3f94b5 | 20650 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | 5 | 5 | 1 | 0 | 39 |
| 47 | [Simple](https://github.com/kevquirk/simple.css) | 5020 | v2.3.7 | 9429 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 5 | 3 | 2 | 5 | 34 |
| 48 | [SPCSS](https://github.com/susam/spcss) | 970 | main@ebb5197 | 1369 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 | 3 | 5 | 4 | 26 |
| 49 | [style](https://github.com/ungoldman/style.css) | 81 | v2.0.0-0 | 7209 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 5 | 3 | 3 | 2 | 28 |
| 50 | [Stylize](https://github.com/gadenbuie/stylize.css) | 0 | v1.0.1 | 4812 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | 5 | 3 | 4 | 0 | 28 |
| 51 | [Sumi](https://github.com/vladocar/Sumi.css) | 190 | main@d823a5f | 28245 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 4 | 5 | 1 | 3 | 34 |
| 52 | [tacit](https://github.com/yegor256/tacit) | 1879 | v1.9.7 | 6557 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 | 2 | 3 | 4 | 32 |
| 53 | [Tiny](https://github.com/ihsan6133/tiny.css) | 46 | main@27b0410 | 5281 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | 4 | 3 | 4 | 1 | 20 |
| 54 | [tty.css](https://github.com/piranna/tty.css) | 10 | master@d35d0dc | 4478 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 | 2 | 4 | 0 | 22 |
| 55 | [Tufte](https://github.com/edwardtufte/tufte-css) | 6585 | gh-pages@b5d7b7b | 6946 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | 5 | 3 | 3 | 5 | 28 |
| 56 | [W3CCore](https://www.w3.org/StyleSheets/Core/Overview) | 0 | 1998 | 9369 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 | 3 | 2 | 0 | 21 |
| 57 | [water](https://github.com/kognise/water.css) | 8655 | master@d950cbc | 22668 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 | 4 | 1 | 5 | 32 |
| 58 | [Wing](https://github.com/kbrsh/wing) | 1991 | master@5792c1c | 5978 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 4 | 2 | 4 | 4 | 27 |
| 59 | [Writ](https://github.com/programble/writ) | 466 | v1.0.4 | 2228 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 | 3 | 5 | 3 | 26 |
| 60 | [YoRHa](https://github.com/metakirby5/yorha) | 330 | master@b575933 | 7939 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 5 | 3 | 3 | 3 | 27 |

Stars come from `stargazers_count` on the GitHub repository page; the version is the latest
release tag, or `branch@commit` for projects without releases.
Bytes are the exact size of the file in the `css/` directory.

## Rules

**Component scan** — each ✅ cell answers one question: does the stylesheet contain a rule whose
selector targets that element? Element selectors are matched in selector position (`h1`…`h6`,
`table{`, `td`, `ul`, `img`, `input`, `select`, `button`, `details`, `summary`, `progress`),
typed inputs by attribute (`input[type=radio]`, `[type=checkbox]`, `[type=color]`,
`[type=range]`), and four are attribute-only:

| Column | Selector that decides it |
|------|------|
| `switch` | `[role=switch]` |
| `validation` | `[aria-invalid]` |
| `loading` | `[aria-busy]` |
| `theme` | `prefers-color-scheme: dark` or `[data-theme]` |

Property values such as `display:table` or `list-style` do not count; selectors wrapped in
`:where()` / `:is()` do. ✅ = implemented, ❌ = not implemented.

**Scoring**

| Group | Columns | Points |
|------|------|------|
| Base components (19) | `h1` `h2` `h3` `h4` `h5` `h6`, `table`, `typography`, `lists`, `picture`, `input`, `select`, `radio`, `checkbox`, `color`, `range`, `button`, `accordions`, `progress` | 1 each |
| Extended components (3) | `switch`, `validation`, `loading` | 2 each |
| Theme | `theme` | ✅ = 5, ❌ = 0 |
| Subjective | `alignment`, `appearance` | 0–5 each, judged by hand |
| Popularity | `stars` | 0–5, rank band by GitHub star count |
| Weight | `size` | 0–5, rank band by file size (smallest = 5) |

`score` = sum of the columns above, maximum 19 × 1 + 3 × 2 + 5 + 5 + 5 + 5 + 5 = 50.

**Popularity (`stars`, 0–5)** — the 60 frameworks are ranked by GitHub star count, descending
(the table itself is alphabetical, so the rank is not the row number); only the band of ten
matters:

| Rank by stars | 1–10 | 11–20 | 21–30 | 31–40 | 41–50 | 51–60 |
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| `stars` | 5 | 4 | 3 | 2 | 1 | 0 |

Rank 40 still belongs to the 31–40 band and scores 2; ranks 41–50 score 1, and every rank from
51 on scores 0.

**File size (`size`, 1–5)** — the 60 stylesheets are ranked by `Bytes`, smallest first, and the
same ten-per-band ranking as `stars` is used: the lightest stylesheet gets size rank 1.

| Size rank | 1–10 | 11–20 | 21–30 | 31–40 | 41–50 | 51–60 |
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| `size` | 5 | 4 | 3 | 2 | 1 | 0 |

Size rank 1 is mi.css (722 B); size rank 60 is LatexCSS (304,731 B). Equal byte counts would
share a rank — there are no ties in the current data.

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