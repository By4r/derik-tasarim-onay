#!/usr/bin/env bash
# Usage: fetch_site.sh <url> <out-dir>
set -euo pipefail
URL="${1:?usage: fetch_site.sh <url> <out-dir>}"
OUT="${2:?usage: fetch_site.sh <url> <out-dir>}"
mkdir -p "$OUT/css"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

echo "[fetch] HTML → $OUT/index.html"
curl -sSL -A "$UA" "$URL" -o "$OUT/index.html"

# Origin (scheme://host) for resolving relative URLs
ORIGIN=$(printf '%s' "$URL" | sed -E 's#^(https?://[^/]+).*#\1#')

# Extract <link rel="stylesheet" href="..."> hrefs
grep -oE '<link[^>]+rel=["'\'']?stylesheet["'\'']?[^>]*>' "$OUT/index.html" \
  | grep -oE 'href=["'\''][^"'\'' ]+["'\'']' \
  | sed -E 's/href=["'\'']([^"'\'']+)["'\'']/\1/' \
  | while read -r href; do
      case "$href" in
        http*) cssurl="$href" ;;
        //*)   cssurl="https:$href" ;;
        /*)    cssurl="$ORIGIN$href" ;;
        *)     cssurl="$ORIGIN/$href" ;;
      esac
      name=$(printf '%s' "$cssurl" | sed -E 's#[^A-Za-z0-9._-]+#_#g' | tail -c 80)
      echo "[fetch] CSS  → $OUT/css/$name"
      curl -sSL -A "$UA" "$cssurl" -o "$OUT/css/$name" || echo "  (failed)"
    done

# Log discovered font URLs
grep -oE 'https?://fonts\.[^"'\'' )]+' "$OUT/index.html" "$OUT/css/"*.css 2>/dev/null \
  | sort -u > "$OUT/fonts.txt" || true

echo "[fetch] done. files:"
ls -la "$OUT" "$OUT/css"
