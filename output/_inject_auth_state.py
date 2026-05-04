#!/usr/bin/env python3
"""Inject auth-state JS into 13 existing pages (v3.7.1).

- If !isLoggedIn: user icon → giris.html, dropdown hidden
- Protected pages (hesap*) require login → redirect giris.html?next=...
- "Çıkış Yap" anchors clear localStorage + redirect to giris.html
- Account sidebar: read userName/userEmail from localStorage; avatar initial from userName
- uyelik-bilgilerim form pre-fill from localStorage
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
// === AUTH STATE (v3.7.1) ===
(function(){
  const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
  const userName = localStorage.getItem('userName') || 'Hesabım';
  const userEmail = localStorage.getItem('userEmail') || '';
  const initial = (userName.trim().charAt(0) || 'H').toUpperCase();

  // 1. Header user icon: not logged in → redirect link, hide dropdown
  document.querySelectorAll('.user-dd-wrap').forEach(wrap => {
    const link = wrap.querySelector('a.icon-btn');
    const menu = wrap.querySelector('.user-dd-menu');
    if (!isLoggedIn) {
      if (link) link.setAttribute('href', 'giris.html');
      if (menu) menu.style.display = 'none';
      wrap.classList.add('logged-out');
      const css = document.createElement('style');
      css.textContent = '.user-dd-wrap.logged-out:hover .user-dd-menu{display:none!important}';
      document.head.appendChild(css);
    } else {
      // Inject user header at top of dropdown
      if (menu && !menu.querySelector('.dd-user-head')) {
        const header = document.createElement('div');
        header.className = 'dd-user-head';
        header.innerHTML = `
          <div class="dd-avatar">${initial}</div>
          <div class="dd-info">
            <b>${userName}</b>
            ${userEmail ? `<span>${userEmail}</span>` : ''}
          </div>
        `;
        header.style.cssText = 'display:flex;align-items:center;gap:10px;padding:12px 16px;border-bottom:1px solid var(--border);margin-bottom:4px';
        const ddCss = document.createElement('style');
        ddCss.textContent = `
          .dd-user-head .dd-avatar{width:36px;height:36px;border-radius:50%;background:#F4D7D9;color:#8B3A3A;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14px;flex-shrink:0}
          .dd-user-head .dd-info b{display:block;font-size:13px;font-weight:700;color:var(--text);line-height:1.3}
          .dd-user-head .dd-info span{display:block;font-size:11px;color:var(--muted);margin-top:2px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:160px}
        `;
        document.head.appendChild(ddCss);
        menu.insertBefore(header, menu.firstChild);
      }
    }
  });

  // 2. Protected pages — require login
  const protectedPages = ['uyelik-bilgilerim.html','siparis-gecmisim.html','siparis-detay.html','adreslerim.html','promosyonlarim.html'];
  const here = location.pathname.split('/').pop();
  if (!isLoggedIn && protectedPages.includes(here)) {
    location.replace('giris.html?next=' + encodeURIComponent(here));
    return;
  }

  // 3. Çıkış Yap handler
  document.querySelectorAll('a').forEach(a => {
    if (a.getAttribute('href') === '#' && a.textContent.trim().toLowerCase().includes('çıkış')) {
      a.addEventListener('click', e => {
        e.preventDefault();
        localStorage.removeItem('isLoggedIn');
        localStorage.removeItem('userName');
        localStorage.removeItem('userEmail');
        location.href = 'giris.html';
      });
    }
  });

  // 4. Account sidebar: replace name/email/avatar
  if (isLoggedIn) {
    const side = document.querySelector('.account-side .user');
    if (side) {
      const av = side.querySelector('.avatar');
      const nameEl = side.querySelector('.user-info b');
      const mailEl = side.querySelector('.user-info span');
      if (av) av.textContent = initial;
      if (nameEl) nameEl.textContent = userName;
      if (mailEl) mailEl.textContent = userEmail || '';
    }
  }

  // 5. uyelik-bilgilerim form pre-fill
  if (isLoggedIn && here === 'uyelik-bilgilerim.html') {
    const parts = userName.split(/\\s+/);
    const adInp = document.getElementById('ad');
    const soyadInp = document.getElementById('soyad');
    const emailInp = document.getElementById('email');
    if (adInp && parts[0]) adInp.value = parts[0];
    if (soyadInp && parts.length > 1) soyadInp.value = parts.slice(1).join(' ');
    if (emailInp && userEmail) emailInp.value = userEmail;
  }
})();
</script>
'''

OLD_MARKER_V37 = '=== AUTH STATE (v3.7) ==='
NEW_MARKER = '=== AUTH STATE (v3.7.1) ==='

count = 0
for fname in PAGES:
    p = ROOT / fname
    if not p.exists():
        print(f'SKIP {fname}: not found'); continue
    txt = p.read_text()
    # Remove old v3.7 block if present
    if OLD_MARKER_V37 in txt:
        # Find <script>...v3.7...</script> block and remove
        import re
        txt = re.sub(r'\n<script>\s*//\s*===\s*AUTH STATE \(v3\.7\)\s*===.*?</script>\n?', '\n', txt, flags=re.DOTALL)
    if NEW_MARKER in txt:
        # Already has new version → also strip and reinject for idempotency
        import re
        txt = re.sub(r'\n<script>\s*//\s*===\s*AUTH STATE \(v3\.7\.1\)\s*===.*?</script>\n?', '\n', txt, flags=re.DOTALL)
    txt = txt.replace('</body>', AUTH_JS + '\n</body>', 1)
    p.write_text(txt)
    count += 1
    print(f'Updated {fname}')

print(f'\n{count} files updated')
