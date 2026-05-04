#!/usr/bin/env python3
"""Inject auth-state JS into 12 existing pages.

Behavior:
- If localStorage.isLoggedIn !== 'true':
  - Disable user-dd-menu (display none)
  - Change user icon link href → giris.html
- Sign-out anchors (Çıkış Yap) clear localStorage and redirect to giris.html
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PAGES = [
    'index.html', 'magaza.html', 'urun-detay.html', 'hikayemiz.html',
    'uretim.html', 'iletisim.html', 'kurumsal-satis.html', 'sss.html',
    'uyelik-bilgilerim.html', 'siparis-gecmisim.html', 'siparis-detay.html',
    'adreslerim.html', 'promosyonlarim.html',
]

AUTH_JS = '''
<script>
// === AUTH STATE (v3.7) ===
(function(){
  const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
  // 1. Header user icon: if not logged in, kill dropdown + redirect to giris
  document.querySelectorAll('.user-dd-wrap').forEach(wrap => {
    const link = wrap.querySelector('a.icon-btn');
    const menu = wrap.querySelector('.user-dd-menu');
    if (!isLoggedIn) {
      if (link) link.setAttribute('href', 'giris.html');
      if (menu) menu.style.display = 'none';
      wrap.classList.add('logged-out');
      // disable hover behavior by removing hover-trigger style
      wrap.style.pointerEvents = 'auto';
      const css = document.createElement('style');
      css.textContent = '.user-dd-wrap.logged-out:hover .user-dd-menu{display:none!important}';
      document.head.appendChild(css);
    }
  });
  // 2. Hesap sayfası protected — redirect to giris.html if not logged in
  const protectedPages = ['uyelik-bilgilerim.html','siparis-gecmisim.html','siparis-detay.html','adreslerim.html','promosyonlarim.html'];
  const here = location.pathname.split('/').pop();
  if (!isLoggedIn && protectedPages.includes(here)) {
    location.replace('giris.html?next=' + encodeURIComponent(here));
    return;
  }
  // 3. Çıkış Yap handler
  document.querySelectorAll('a[href="#"]').forEach(a => {
    if (a.textContent.trim().includes('Çıkış')) {
      a.addEventListener('click', e => {
        e.preventDefault();
        localStorage.removeItem('isLoggedIn');
        localStorage.removeItem('userEmail');
        location.href = 'giris.html';
      });
    }
  });
})();
</script>
'''

count = 0
for fname in PAGES:
    p = ROOT / fname
    if not p.exists():
        print(f'SKIP {fname}: not found')
        continue
    txt = p.read_text()
    if '=== AUTH STATE (v3.7) ===' in txt:
        print(f'SKIP {fname}: already injected')
        continue
    # Inject before </body>
    txt = txt.replace('</body>', AUTH_JS + '\n</body>', 1)
    p.write_text(txt)
    count += 1
    print(f'Updated {fname}')

print(f'\n{count} files updated')
