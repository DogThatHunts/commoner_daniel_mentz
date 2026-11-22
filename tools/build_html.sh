#!/bin/zsh
# Render NN.slug/summary.md -> summary.html (policy P8). Usage: tools/build_html.sh [folder ...]  (default: all NN.* folders)
cd "$(dirname "$0")/.." || exit 1
dirs=("$@"); [ ${#dirs[@]} -eq 0 ] && dirs=(0*/)
for d in "${dirs[@]}"; do d=${d%/}
  t=$(sed -n '1s/^# //p' $d/summary.md)
  pandoc $d/summary.md -f gfm -t html5 --standalone --metadata title="$t" -V pagetitle="$t: Summary" \
    -H <(printf '<meta name="viewport" content="width=device-width,initial-scale=1"><style>'; cat tools/style.css; printf '</style>') -o $d/summary.html
  sed -i '' '/<header id="title-block-header">/,/<\/header>/d; s|href="\([^"]*\)/summary\.md"|href="\1/summary.html"|g; s|<body>|<body><p style="font:14px system-ui,sans-serif"><a href="../index.html">← All interviews</a></p>|' $d/summary.html
  # every slide image opens the full-size file in a new tab
  perl -0pi -e 's|<img src="(slides/[^"]+)"([^>]*?)\s*/?>|<a class="slide" href="$1" target="_blank" rel="noopener"><img src="$1"$2></a>|g' $d/summary.html
  echo "built $d/summary.html"
done
