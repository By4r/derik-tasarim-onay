#!/usr/bin/env python3
"""Inject user dropdown into 8 existing pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OLD_LINE = '<a href="#hesap" class="icon-btn" aria-label="Hesabım"><i class="fa-regular fa-user"></i></a>'
NEW_BLOCK = '''<span class="user-dd-wrap">
        <a href="uyelik-bilgilerim.html" class="icon-btn" aria-label="Hesabım"><i class="fa-regular fa-user"></i></a>
        <span class="user-dd-menu">
          <a href="uyelik-bilgilerim.html"><i class="fa-regular fa-id-card"></i> Üyelik Bilgilerim</a>
          <a href="siparis-gecmisim.html"><i class="fa-solid fa-box"></i> Sipariş Geçmişim</a>
          <a href="adreslerim.html"><i class="fa-solid fa-location-dot"></i> Adreslerim</a>
          <a href="promosyonlarim.html"><i class="fa-solid fa-ticket"></i> Promosyonlarım</a>
          <span class="divider"></span>
          <a href="#"><i class="fa-solid fa-right-from-bracket"></i> Çıkış Yap</a>
        </span>
      </span>'''

USER_DD_CSS = '''
/* USER DROPDOWN */
.user-dd-wrap{position:relative;display:inline-flex}
.user-dd-wrap:hover .user-dd-menu,.user-dd-menu:hover{display:block}
.user-dd-menu{position:absolute;top:calc(100% + 4px);right:0;background:#fff;border:1px solid var(--border);border-radius:var(--r-md);box-shadow:var(--shadow-2);padding:var(--s-2) 0;min-width:220px;display:none;z-index:60}
.user-dd-menu a{display:flex;align-items:center;gap:var(--s-3);padding:10px 16px;font-size:var(--fs-sm);color:var(--text-2);font-weight:600}
.user-dd-menu a i{width:18px;color:var(--muted);font-size:var(--icon-sm)}
.user-dd-menu a:hover{background:var(--primary-100);color:var(--primary-700)}
.user-dd-menu a:hover i{color:var(--primary-700)}
.user-dd-menu .divider{height:1px;background:var(--border);margin:var(--s-2) 0;display:block}
'''

PAGES = ["index.html", "magaza.html", "urun-detay.html", "hikayemiz.html",
         "uretim.html", "iletisim.html", "kurumsal-satis.html", "sss.html"]

for fname in PAGES:
    p = ROOT / fname
    txt = p.read_text()
    if OLD_LINE not in txt:
        print(f"SKIP {fname}: pattern not found")
        continue
    if "user-dd-wrap" in txt:
        print(f"SKIP {fname}: already injected")
        continue
    txt = txt.replace(OLD_LINE, NEW_BLOCK, 1)
    # Inject CSS just before </style> (first occurrence)
    txt = txt.replace("</style>", USER_DD_CSS + "</style>", 1)
    p.write_text(txt)
    print(f"Updated {fname}")

print("Done.")
