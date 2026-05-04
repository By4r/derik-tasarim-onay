#!/usr/bin/env python3
"""
v3.9.4 Strip newsletter block from footers — idempotent.
Removes the v3.9 newsletter block (marked with INJECT:V39:NEWSLETTER) from all *.html.
Safe to re-run: if marker not found, file is left untouched.
"""
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = glob.glob(os.path.join(ROOT, "*.html"))

# Block: <!-- INJECT:V39:NEWSLETTER --> <div class="footer-newsletter" ...>...</div>
# We match marker through the closing </div> of footer-newsletter.
PATTERN = re.compile(
    r'\s*<!--\s*INJECT:V39:NEWSLETTER\s*-->\s*'
    r'<div class="footer-newsletter".*?</form>\s*</div>\s*',
    re.DOTALL
)

def main():
    changed, skipped = [], []
    for path in PAGES:
        name = os.path.basename(path)
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        new_html, n = PATTERN.subn('\n    ', html)
        if n:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_html)
            changed.append(name)
        else:
            skipped.append(name)
    print(f"STRIPPED: {len(changed)} files")
    for f in changed: print(f"  - {f}")
    print(f"SKIPPED (no newsletter block): {len(skipped)}")

if __name__ == '__main__':
    main()
