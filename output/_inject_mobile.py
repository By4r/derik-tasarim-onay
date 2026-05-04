#!/usr/bin/env python3
"""v3.8 — Mobile hamburger panel + footer centering + general mobile fixes.

Idempotent: detects '=== MOBILE PANEL (v3.8) ===' marker and re-injects.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

MAIN_PAGES = [
    'index.html', 'magaza.html', 'urun-detay.html', 'hikayemiz.html',
    'uretim.html', 'iletisim.html', 'kurumsal-satis.html', 'sss.html',
    'uyelik-bilgilerim.html', 'siparis-gecmisim.html', 'siparis-detay.html',
    'adreslerim.html', 'promosyonlarim.html',
]
AUTH_PAGES = ['giris.html', 'kayit.html', 'sifremi-unuttum.html', 'sifre-sifirla.html']

MARKER = '=== MOBILE PANEL (v3.8) ==='

CSS_BLOCK = '''
/* ============ MOBILE PANEL (v3.8) ============ */
.mobile-burger{display:none;width:42px;height:42px;border-radius:50%;align-items:center;justify-content:center;color:var(--text);cursor:pointer;background:transparent;border:0;transition:background var(--t-fast)}
.mobile-burger:hover{background:var(--primary-100,#F2EBDC);color:var(--primary-700)}
.mobile-burger i{font-size:20px}
@media(max-width:1024px){.mobile-burger{display:inline-flex}}

.mobile-overlay{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:199;opacity:0;visibility:hidden;transition:opacity .3s ease,visibility .3s}
.mobile-overlay.open{opacity:1;visibility:visible}

.mobile-panel{position:fixed;top:0;right:0;height:100vh;width:82%;max-width:320px;background:var(--bg);border-left:1px solid rgba(0,0,0,.08);box-shadow:-8px 0 24px rgba(0,0,0,.12);transform:translateX(100%);transition:transform .3s ease;z-index:200;display:flex;flex-direction:column;overflow-y:auto}
.mobile-panel.open{transform:translateX(0)}
.mobile-panel-head{display:flex;align-items:center;justify-content:space-between;padding:20px 20px 16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:var(--bg);z-index:1}
.mobile-panel-head .brand-logo{font-size:24px}
.mobile-panel-close{width:36px;height:36px;border-radius:var(--r-sm,6px);background:var(--bg-soft);color:var(--text);display:inline-flex;align-items:center;justify-content:center;font-size:16px;cursor:pointer;border:0;transition:all var(--t-fast)}
.mobile-panel-close:hover{background:var(--accent-red,#B04A3E);color:#fff}
.mobile-panel-user{display:flex;align-items:center;gap:12px;padding:14px 16px;background:var(--bg-soft);margin:16px 20px;border-radius:var(--r-md,10px)}
.mobile-panel-user .avatar{width:42px;height:42px;border-radius:50%;background:#F4D7D9;color:#8B3A3A;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:16px;flex-shrink:0}
.mobile-panel-user .info{min-width:0;flex:1}
.mobile-panel-user .info b{display:block;font-size:14px;font-weight:700;color:var(--text);line-height:1.3;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.mobile-panel-user .info span{display:block;font-size:11px;color:var(--muted);margin-top:2px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.mobile-panel-cta{display:flex;flex-direction:column;gap:10px;padding:16px 20px}
.mobile-panel-cta a{display:block;padding:13px;border-radius:var(--r-sm,6px);text-align:center;font-weight:700;font-size:14px;text-transform:uppercase;letter-spacing:.04em;transition:all var(--t-fast)}
.mobile-panel-cta a.primary{background:var(--primary-700);color:#fff}
.mobile-panel-cta a.primary:hover{background:var(--primary-900);color:#fff}
.mobile-panel-cta a.outline{background:transparent;border:1.5px solid var(--primary-700);color:var(--primary-700)}
.mobile-panel-cta a.outline:hover{background:var(--primary-700);color:#fff}
.mobile-panel-nav{display:flex;flex-direction:column;padding:4px 20px}
.mobile-panel-nav a{display:flex;align-items:center;gap:14px;padding:14px 0;font-size:15px;color:var(--text);font-weight:600;border-bottom:1px solid rgba(0,0,0,.06);transition:color var(--t-fast)}
.mobile-panel-nav a i{width:18px;color:var(--muted);font-size:14px;text-align:center}
.mobile-panel-nav a:hover{color:var(--primary-700)}
.mobile-panel-nav a:hover i{color:var(--primary-700)}
.mobile-panel-nav a:last-child{border-bottom:0}
.mobile-panel-section-label{font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);padding:16px 20px 4px}
.mobile-panel-nav a.signout{color:var(--accent-red,#B04A3E);font-weight:700}
.mobile-panel-nav a.signout i{color:var(--accent-red,#B04A3E)}
body.mobile-panel-open{overflow:hidden}

/* FOOTER MOBILE CENTERING */
@media(max-width:767px){
  .footer{text-align:center;padding-bottom:40px}
  .footer-cols{grid-template-columns:1fr!important;gap:32px}
  .footer-brand p{max-width:100%;margin-left:auto;margin-right:auto}
  .footer .contact-line{justify-content:center}
  .footer .socials{justify-content:center}
  .footer-bottom{flex-direction:column;text-align:center;gap:12px}
  .footer-bottom .policies{justify-content:center}
}

/* GENERAL MOBILE FIXES */
@media(max-width:767px){
  .container{padding-left:16px!important;padding-right:16px!important}
  .section{padding:48px 0!important}
  .product-grid{grid-template-columns:repeat(2,1fr)!important;gap:12px}
  .banner-grid{grid-template-columns:1fr!important}
  .cat-grid{grid-template-columns:repeat(2,1fr)!important}
  .hero-slide{grid-template-columns:1fr!important;padding:24px!important;min-height:auto!important;gap:24px}
  .hero-slider{min-height:auto!important}
  .account-layout{grid-template-columns:1fr!important}
  .account-side{display:none}
  .modal{max-width:90vw}
  .modal-body{padding:20px}
  .modal-header,.modal-footer{padding:16px 20px}
  .acc-form{padding:20px!important}
  .acc-form .form-row{grid-template-columns:1fr!important}
  .order-head{grid-template-columns:repeat(2,1fr)!important}
  .addr-grid,.promo-grid{grid-template-columns:1fr!important}
  .pd{grid-template-columns:1fr!important;gap:24px}
  .shop-layout{grid-template-columns:1fr!important}
  .filter-panel{position:static!important}
  .stats-grid{grid-template-columns:1fr!important}
  .auth-card{padding:24px!important}
}
@media(max-width:480px){
  .product-grid{grid-template-columns:1fr!important}
  .cat-grid{grid-template-columns:1fr!important}
}
'''

# Hamburger button HTML — inserted into .header-actions
BURGER_BTN = '<button class="mobile-burger" aria-label="Menü" data-open-mpanel><i class="fa-solid fa-bars"></i></button>'

# Auth pages: hamburger placed in auth-header
AUTH_BURGER_BTN = '<button class="mobile-burger" aria-label="Menü" data-open-mpanel style="display:none"><i class="fa-solid fa-bars"></i></button>'

PANEL_HTML_MAIN = '''
<!-- MOBILE PANEL (v3.8) -->
<div class="mobile-overlay" data-close-mpanel></div>
<aside class="mobile-panel" id="mobilePanel" aria-hidden="true">
  <div class="mobile-panel-head">
    <a href="index.html" class="brand-logo">Derik</a>
    <button class="mobile-panel-close" data-close-mpanel aria-label="Kapat"><i class="fa-solid fa-xmark"></i></button>
  </div>
  <div id="mpanelUserSection"></div>
  <div class="mobile-panel-section-label">Menü</div>
  <nav class="mobile-panel-nav">
    <a href="index.html"><i class="fa-solid fa-house"></i> Anasayfa</a>
    <a href="magaza.html"><i class="fa-solid fa-shop"></i> Mağaza</a>
    <a href="hikayemiz.html"><i class="fa-solid fa-book-open"></i> Hikayemiz</a>
    <a href="uretim.html"><i class="fa-solid fa-leaf"></i> Üretim</a>
    <a href="kurumsal-satis.html"><i class="fa-solid fa-building"></i> Kurumsal Satış</a>
    <a href="sss.html"><i class="fa-solid fa-circle-question"></i> S.S.S.</a>
    <a href="iletisim.html"><i class="fa-solid fa-envelope"></i> İletişim</a>
  </nav>
  <div id="mpanelAccountSection"></div>
</aside>
'''

PANEL_HTML_AUTH = '''
<!-- MOBILE PANEL (v3.8) -->
<div class="mobile-overlay" data-close-mpanel></div>
<aside class="mobile-panel" id="mobilePanel" aria-hidden="true">
  <div class="mobile-panel-head">
    <a href="index.html" class="brand-logo">Derik</a>
    <button class="mobile-panel-close" data-close-mpanel aria-label="Kapat"><i class="fa-solid fa-xmark"></i></button>
  </div>
  <div class="mobile-panel-cta">
    <a href="index.html" class="primary"><i class="fa-solid fa-arrow-left"></i> Anasayfaya Dön</a>
  </div>
  <div class="mobile-panel-section-label">Menü</div>
  <nav class="mobile-panel-nav">
    <a href="magaza.html"><i class="fa-solid fa-shop"></i> Mağaza</a>
    <a href="hikayemiz.html"><i class="fa-solid fa-book-open"></i> Hikayemiz</a>
    <a href="iletisim.html"><i class="fa-solid fa-envelope"></i> İletişim</a>
  </nav>
</aside>
'''

JS_MAIN = '''
<script>
// === MOBILE PANEL (v3.8) ===
(function(){
  const panel = document.getElementById('mobilePanel');
  const overlay = document.querySelector('.mobile-overlay');
  if (!panel) return;
  function open(){ panel.classList.add('open'); overlay.classList.add('open'); document.body.classList.add('mobile-panel-open'); panel.setAttribute('aria-hidden','false'); }
  function close(){ panel.classList.remove('open'); overlay.classList.remove('open'); document.body.classList.remove('mobile-panel-open'); panel.setAttribute('aria-hidden','true'); }
  document.querySelectorAll('[data-open-mpanel]').forEach(b => b.addEventListener('click', open));
  document.querySelectorAll('[data-close-mpanel]').forEach(b => b.addEventListener('click', close));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });

  const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
  const userName = localStorage.getItem('userName') || 'Hesabım';
  const userEmail = localStorage.getItem('userEmail') || '';
  const initial = (userName.trim().charAt(0) || 'H').toUpperCase();
  const userSection = document.getElementById('mpanelUserSection');
  const accountSection = document.getElementById('mpanelAccountSection');
  if (isLoggedIn) {
    userSection.innerHTML = `
      <div class="mobile-panel-user">
        <div class="avatar">${initial}</div>
        <div class="info"><b>${userName}</b>${userEmail ? `<span>${userEmail}</span>` : ''}</div>
      </div>`;
    accountSection.innerHTML = `
      <div class="mobile-panel-section-label">Hesabım</div>
      <nav class="mobile-panel-nav">
        <a href="uyelik-bilgilerim.html"><i class="fa-regular fa-id-card"></i> Üyelik Bilgilerim</a>
        <a href="siparis-gecmisim.html"><i class="fa-solid fa-box"></i> Sipariş Geçmişim</a>
        <a href="adreslerim.html"><i class="fa-solid fa-location-dot"></i> Adreslerim</a>
        <a href="promosyonlarim.html"><i class="fa-solid fa-ticket"></i> Promosyonlarım</a>
        <a href="#" class="signout" id="mpanelSignout"><i class="fa-solid fa-right-from-bracket"></i> Çıkış Yap</a>
      </nav>`;
    document.getElementById('mpanelSignout').addEventListener('click', e => {
      e.preventDefault();
      localStorage.removeItem('isLoggedIn');
      localStorage.removeItem('userName');
      localStorage.removeItem('userEmail');
      location.href = 'giris.html';
    });
  } else {
    userSection.innerHTML = `
      <div class="mobile-panel-cta">
        <a href="giris.html" class="primary">Giriş Yap</a>
        <a href="kayit.html" class="outline">Üye Ol</a>
      </div>`;
  }
})();
</script>
'''

JS_AUTH = '''
<script>
// === MOBILE PANEL (v3.8) ===
(function(){
  const panel = document.getElementById('mobilePanel');
  const overlay = document.querySelector('.mobile-overlay');
  if (!panel) return;
  function open(){ panel.classList.add('open'); overlay.classList.add('open'); document.body.classList.add('mobile-panel-open'); }
  function close(){ panel.classList.remove('open'); overlay.classList.remove('open'); document.body.classList.remove('mobile-panel-open'); }
  document.querySelectorAll('[data-open-mpanel]').forEach(b => b.addEventListener('click', open));
  document.querySelectorAll('[data-close-mpanel]').forEach(b => b.addEventListener('click', close));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  // Force show burger only <1024
  const m = window.matchMedia('(max-width:1024px)');
  function sync(){ document.querySelectorAll('.mobile-burger').forEach(b => b.style.display = m.matches ? 'inline-flex' : 'none'); }
  sync(); m.addEventListener('change', sync);
})();
</script>
'''


def patch_main(fname: Path) -> bool:
    txt = fname.read_text()
    # Strip prior v3.8 injections (idempotent)
    txt = re.sub(r'/\* ============ MOBILE PANEL \(v3\.8\) ============.*?(?=/\* |</style>|$)', '', txt, flags=re.DOTALL)
    txt = re.sub(r'\n<!-- MOBILE PANEL \(v3\.8\) -->.*?</aside>\n?', '', txt, flags=re.DOTALL)
    txt = re.sub(r'\n<script>\s*//\s*===\s*MOBILE PANEL \(v3\.8\)\s*===.*?</script>\n?', '', txt, flags=re.DOTALL)
    # Remove existing burger button if any
    txt = re.sub(r'\s*<button class="mobile-burger"[^>]*>.*?</button>', '', txt, flags=re.DOTALL)

    # 1. Inject CSS before </style>
    if CSS_BLOCK not in txt:
        txt = txt.replace('</style>', CSS_BLOCK + '\n</style>', 1)

    # 2. Inject burger button just before </div></header> in main pages
    # Look for header-actions closing or sepet link as anchor
    # Simpler: insert burger as last child of .header-actions
    new_txt, n = re.subn(
        r'(<div class="header-actions">.*?</a>)(\s*</div>\s*</div>\s*</header>)',
        r'\1\n      ' + BURGER_BTN + r'\2',
        txt, count=1, flags=re.DOTALL
    )
    if n:
        txt = new_txt

    # 3. Inject panel HTML + JS before </body>
    txt = txt.replace('</body>', PANEL_HTML_MAIN + JS_MAIN + '\n</body>', 1)

    fname.write_text(txt)
    return True


def patch_auth(fname: Path) -> bool:
    txt = fname.read_text()
    txt = re.sub(r'/\* ============ MOBILE PANEL \(v3\.8\) ============.*?(?=/\* |</style>|$)', '', txt, flags=re.DOTALL)
    txt = re.sub(r'\n<!-- MOBILE PANEL \(v3\.8\) -->.*?</aside>\n?', '', txt, flags=re.DOTALL)
    txt = re.sub(r'\n<script>\s*//\s*===\s*MOBILE PANEL \(v3\.8\)\s*===.*?</script>\n?', '', txt, flags=re.DOTALL)
    txt = re.sub(r'\s*<button class="mobile-burger"[^>]*>.*?</button>', '', txt, flags=re.DOTALL)

    if CSS_BLOCK not in txt:
        txt = txt.replace('</style>', CSS_BLOCK + '\n</style>', 1)

    # Auth header: add burger after .ctx-link a
    new_txt, n = re.subn(
        r'(<a href="[^"]*" class="ctx-link">.*?</a>)(\s*</div>\s*</header>)',
        r'\1\n    ' + BURGER_BTN + r'\2',
        txt, count=1, flags=re.DOTALL
    )
    if n:
        txt = new_txt

    txt = txt.replace('</body>', PANEL_HTML_AUTH + JS_AUTH + '\n</body>', 1)

    fname.write_text(txt)
    return True


main_count = 0
for fn in MAIN_PAGES:
    p = ROOT / fn
    if not p.exists():
        print(f'SKIP {fn}: not found'); continue
    if patch_main(p):
        main_count += 1
        print(f'MAIN  {fn}')

auth_count = 0
for fn in AUTH_PAGES:
    p = ROOT / fn
    if not p.exists():
        print(f'SKIP {fn}: not found'); continue
    if patch_auth(p):
        auth_count += 1
        print(f'AUTH  {fn}')

print(f'\nUpdated: {main_count} main + {auth_count} auth = {main_count + auth_count} total')
