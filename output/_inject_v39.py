#!/usr/bin/env python3
"""
v3.9 Global components injector — idempotent.
Adds: cookie banner, whatsapp button, toast container, mini cart drawer.
Newsletter block REMOVED in v3.9.4 (patron decision).
Each block uses marker comment so re-runs are safe.
"""
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = glob.glob(os.path.join(ROOT, "*.html"))

GLOBAL_MARKER = "<!-- INJECT:V39:GLOBAL -->"
GLOBAL_BLOCK = GLOBAL_MARKER + """
<!-- Cookie Banner -->
<div id="v39-cookie" style="display:none;position:fixed;bottom:0;left:0;right:0;z-index:9000;background:#fff;border-top:1px solid var(--border);box-shadow:0 -8px 32px rgba(0,0,0,.08);padding:16px 24px">
  <div style="max-width:1320px;margin:0 auto;display:flex;flex-wrap:wrap;align-items:center;gap:16px;justify-content:space-between">
    <div style="flex:1;min-width:260px;color:var(--text);font-size:14px;line-height:1.5">
      <strong>Çerez kullanımı.</strong> Bu sitede deneyiminizi iyileştirmek için çerezler kullanıyoruz. Detaylı bilgi için <a href="cerez-politikasi.html" style="color:var(--primary-700);text-decoration:underline">Çerez Politikası</a> sayfasını inceleyebilirsiniz.
    </div>
    <div style="display:flex;gap:8px;flex-wrap:wrap">
      <button onclick="v39CookieAccept('necessary')" style="padding:10px 16px;background:#fff;border:1px solid var(--border);color:var(--text);border-radius:var(--r-sm,8px);font-weight:600;cursor:pointer;font:inherit">Sadece Gerekli</button>
      <a href="cerez-politikasi.html" style="padding:10px 16px;color:var(--text);text-decoration:none;font-weight:600;align-self:center">Tercihler</a>
      <button onclick="v39CookieAccept('all')" style="padding:10px 18px;background:var(--primary-700);border:0;color:#fff;border-radius:var(--r-sm,8px);font-weight:700;cursor:pointer;font:inherit">Tümünü Kabul Et</button>
    </div>
  </div>
</div>

<!-- WhatsApp Floating Button -->
<a href="https://wa.me/905XXXXXXXXX" target="_blank" rel="noopener" id="v39-wa" aria-label="WhatsApp" style="position:fixed;right:24px;bottom:24px;width:56px;height:56px;border-radius:50%;background:#25D366;color:#fff;display:flex;align-items:center;justify-content:center;font-size:28px;box-shadow:0 6px 20px rgba(37,211,102,.4);z-index:8500;text-decoration:none;transition:transform .2s">
  <i class="fa-brands fa-whatsapp"></i>
</a>

<!-- Toast Container -->
<div id="v39-toast-wrap" style="position:fixed;top:96px;right:24px;z-index:9500;display:flex;flex-direction:column;gap:8px;pointer-events:none"></div>

<!-- Mini Cart Drawer -->
<div id="v39-minicart-overlay" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:9100"></div>
<aside id="v39-minicart" style="display:none;position:fixed;top:0;right:0;bottom:0;width:380px;max-width:90vw;background:#fff;z-index:9200;box-shadow:-12px 0 32px rgba(0,0,0,.12);flex-direction:column">
  <header style="padding:20px 24px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between">
    <h3 style="margin:0;font-size:18px;font-weight:700;color:var(--primary-700)">Sepetim</h3>
    <button onclick="v39MiniCart(false)" aria-label="Kapat" style="background:none;border:0;font-size:22px;color:var(--text);cursor:pointer">&times;</button>
  </header>
  <div id="v39-minicart-body" style="flex:1;overflow:auto;padding:16px 24px"></div>
  <footer style="padding:20px 24px;border-top:1px solid var(--border)">
    <div style="display:flex;justify-content:space-between;margin-bottom:12px;font-weight:700;color:var(--primary-700)"><span>Ara Toplam</span><span id="v39-minicart-total">1.940,00 TL</span></div>
    <a href="sepet.html" style="display:block;padding:12px;background:#fff;border:1.5px solid var(--primary-700);color:var(--primary-700);text-align:center;text-decoration:none;border-radius:var(--r-sm,8px);font-weight:700;margin-bottom:8px">Sepete Git</a>
    <a href="odeme.html" style="display:block;padding:12px;background:var(--primary-700);color:#fff;text-align:center;text-decoration:none;border-radius:var(--r-sm,8px);font-weight:700">Ödemeye Geç</a>
  </footer>
</aside>

<!-- Search Dropdown Panel -->
<div id="v39-search-overlay" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,.35);z-index:9100"></div>
<div id="v39-search-panel" style="display:none;position:fixed;top:80px;left:50%;transform:translateX(-50%);width:560px;max-width:92vw;background:#fff;border:1px solid var(--border);border-radius:var(--r-md,12px);box-shadow:0 12px 40px rgba(0,0,0,.16);z-index:9200;padding:20px">
  <form onsubmit="event.preventDefault();var q=document.getElementById('v39-search-input').value.trim();if(q)location.href='arama.html?q='+encodeURIComponent(q);">
    <div style="display:flex;align-items:center;gap:8px;border:1.5px solid var(--border);border-radius:var(--r-sm,8px);padding:10px 14px">
      <i class="fa-solid fa-magnifying-glass" style="color:var(--text-2,#6B5847)"></i>
      <input id="v39-search-input" type="text" placeholder="Ürün, kategori veya etiket ara..." autocomplete="off" style="flex:1;border:0;outline:0;font:inherit;background:transparent;color:var(--text)">
      <button type="button" onclick="v39Search(false)" aria-label="Kapat" style="background:none;border:0;color:var(--text-2,#6B5847);cursor:pointer;font-size:18px">&times;</button>
    </div>
  </form>
  <div style="margin-top:16px">
    <div style="font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--text-2,#6B5847);margin-bottom:8px">Popüler aramalar</div>
    <div style="display:flex;flex-wrap:wrap;gap:8px">
      <a href="arama.html?q=zeytinya%C4%9F%C4%B1" class="v39-chip">zeytinyağı</a>
      <a href="arama.html?q=hediye+seti" class="v39-chip">hediye seti</a>
      <a href="arama.html?q=sabun" class="v39-chip">sabun</a>
      <a href="arama.html?q=Halhal%C4%B1" class="v39-chip">Halhalı</a>
      <a href="arama.html?q=5L+teneke" class="v39-chip">5L teneke</a>
    </div>
  </div>
</div>

<style>
.v39-chip{display:inline-block;padding:6px 12px;background:var(--bg-soft);color:var(--text);text-decoration:none;border-radius:999px;font-size:13px;border:1px solid var(--border);transition:all .2s}
.v39-chip:hover{background:var(--primary-700);color:#fff;border-color:var(--primary-700)}
#v39-wa:hover{transform:scale(1.08)}
.v39-toast{pointer-events:auto;padding:12px 20px;border-radius:var(--r-sm,8px);background:#fff;border-left:4px solid var(--primary-700);color:var(--text);box-shadow:0 8px 24px rgba(0,0,0,.12);font-size:14px;font-weight:500;max-width:320px;animation:v39toastIn .25s ease-out}
.v39-toast.error{border-left-color:#C0392B}
.v39-toast.info{border-left-color:var(--accent-gold)}
@keyframes v39toastIn{from{opacity:0;transform:translateX(20px)}to{opacity:1;transform:translateX(0)}}
.v39-mini-row{display:flex;gap:12px;padding:12px 0;border-bottom:1px solid var(--border)}
.v39-mini-row:last-child{border-bottom:0}
.v39-mini-row img{width:60px;height:60px;border-radius:var(--r-sm,8px);object-fit:cover}
.v39-mini-row .meta{flex:1;font-size:13px}
.v39-mini-row .name{font-weight:600;color:var(--text);margin-bottom:4px;display:block;text-decoration:none}
.v39-mini-row .price{color:var(--primary-700);font-weight:700}
@media(max-width:560px){#v39-minicart{width:100%}}
</style>

<script>
// === V39 GLOBAL JS ===
window.showToast=function(msg,type){
  var w=document.getElementById('v39-toast-wrap');if(!w)return;
  var last=w.lastChild;if(last&&last.dataset&&last.dataset.msg===msg)return;
  while(w.children.length>=3)w.firstChild.remove();
  var t=document.createElement('div');t.className='v39-toast '+(type||'success');t.innerHTML=msg;t.dataset.msg=msg;
  w.appendChild(t);setTimeout(function(){t.style.opacity=0;t.style.transform='translateX(20px)';setTimeout(function(){t.remove()},250)},3000);
};
// Cookie banner
(function(){
  if(!localStorage.getItem('cookieConsent')){var b=document.getElementById('v39-cookie');if(b)b.style.display='block'}
})();
window.v39CookieAccept=function(v){localStorage.setItem('cookieConsent',v);var b=document.getElementById('v39-cookie');if(b)b.style.display='none'};
// Mini cart
window.v39MiniCart=function(open){
  var d=document.getElementById('v39-minicart');var o=document.getElementById('v39-minicart-overlay');if(!d||!o)return;
  d.style.display=open?'flex':'none';o.style.display=open?'block':'none';document.body.style.overflow=open?'hidden':'';
  if(open){
    var demo=[
      {name:'Erken Hasat 500ml',price:'320,00 TL',img:'https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=120&h=120&fit=crop&q=80'},
      {name:'Soğuk Sıkım 1L',price:'450,00 TL',img:'https://images.unsplash.com/photo-1620706857370-e1b9770e8bb1?w=120&h=120&fit=crop&q=80'},
      {name:'Hediye Seti Premium',price:'850,00 TL',img:'https://images.unsplash.com/photo-1549049950-48d5887197a0?w=120&h=120&fit=crop&q=80'}
    ];
    var b=document.getElementById('v39-minicart-body');
    b.innerHTML=demo.map(function(p){return '<div class="v39-mini-row"><img src="'+p.img+'" alt=""><div class="meta"><a class="name" href="urun-detay.html">'+p.name+'</a><span class="price">'+p.price+'</span></div></div>'}).join('');
  }
};
document.addEventListener('click',function(e){
  var t=e.target.closest('[data-mini-cart-trigger]');
  if(t){e.preventDefault();v39MiniCart(true)}
  if(e.target.id==='v39-minicart-overlay')v39MiniCart(false);
});
// Search dropdown
window.v39Search=function(open){
  var p=document.getElementById('v39-search-panel');var o=document.getElementById('v39-search-overlay');if(!p||!o)return;
  p.style.display=open?'block':'none';o.style.display=open?'block':'none';
  if(open){setTimeout(function(){var i=document.getElementById('v39-search-input');if(i)i.focus()},50)}
};
document.addEventListener('click',function(e){
  var s=e.target.closest('[data-search-trigger]');
  if(s){e.preventDefault();v39Search(true)}
  if(e.target.id==='v39-search-overlay')v39Search(false);
});
document.addEventListener('keydown',function(e){if(e.key==='Escape'){v39Search(false);v39MiniCart(false)}});
// Logout
document.addEventListener('click',function(e){
  var l=e.target.closest('[data-logout]');
  if(l){localStorage.removeItem('isLoggedIn');localStorage.removeItem('userName');localStorage.removeItem('userEmail')}
});
// Favorites toggle (any .fav-btn)
document.addEventListener('click',function(e){
  var fb=e.target.closest('.fav-btn');
  if(fb && fb.tagName==='A' && fb.getAttribute('href')==='urun-detay.html'){return} // legacy non-favorite link
  if(fb){
    e.preventDefault();
    var i=fb.querySelector('i');
    if(i){
      if(i.classList.contains('fa-regular')){i.classList.remove('fa-regular');i.classList.add('fa-solid');fb.style.color='#C0392B';showToast('Favorilere eklendi','success')}
      else{i.classList.remove('fa-solid');i.classList.add('fa-regular');fb.style.color='';showToast('Favorilerden çıkarıldı','info')}
    }
  }
});
</script>
"""

def inject_global(html):
    if GLOBAL_MARKER in html:
        return html, False
    pattern = r'(</body>)'
    if re.search(pattern, html):
        return re.sub(pattern, GLOBAL_BLOCK + r'\n\1', html, count=1), True
    return html, False

def main():
    changed = []
    skipped = []
    for path in PAGES:
        name = os.path.basename(path)
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        orig = html
        html, n_glob = inject_global(html)
        if html != orig:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(html)
            changed.append(name)
        else:
            skipped.append(name)
    print(f"INJECTED: {len(changed)} files")
    for f in changed: print(f"  + {f}")
    print(f"SKIPPED (already injected or no </body>): {len(skipped)}")

if __name__ == '__main__':
    main()
