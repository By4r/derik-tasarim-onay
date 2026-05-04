#!/usr/bin/env python3
"""Build 4 account dashboard pages (KD layout + Trendyol card anatomy)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BASE_CSS = r"""
:root {
  --primary-700:#3B4A2A; --primary-800:#6B7A3F; --primary-900:#2A3520;
  --primary-100:#F2EBDC; --primary-200:#E8DFC9;
  --bg:#FAF6EE; --bg-soft:#F2EBDC; --bg-section:#F2EBDC;
  --bg-card:#E8DFC9; --bg-product:#FAF9F5;
  --text:#2A1F14; --text-2:#4A3A2A; --muted:#8C7A6A; --muted-2:#B5A693;
  --border:#E8DFC9;
  --accent-gold:#C9A55B; --accent-gold-soft:#E8D4A1;
  --accent-earth:#8C6A4A; --accent-red:#B04A3E; --accent-success:#5A7A3A;
  --font:"Inter","Helvetica Neue",system-ui,Arial,sans-serif;
  --fs-xs:12px; --fs-sm:14px; --fs-base:16px; --fs-md:18px;
  --fs-lg:20px; --fs-xl:24px; --fs-2xl:32px; --fs-3xl:36px;
  --icon-sm:14px; --icon-md:18px; --icon-lg:22px;
  --s-1:4px;--s-2:8px;--s-3:12px;--s-4:16px;--s-5:20px;--s-6:24px;
  --s-8:32px;--s-10:40px;--s-12:48px;--s-16:64px;
  --r-sm:6px; --r-md:10px; --r-lg:12px; --r-xl:14px; --r-pill:100px;
  --shadow-1:0 2px 8px rgba(0,0,0,.06);
  --shadow-2:0 6px 20px rgba(42,31,20,.10);
  --shadow-header:0 1px 4px rgba(0,0,0,.04);
  --maxw:1320px; --t-fast:.2s ease; --t-mid:.3s ease;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:var(--font);font-size:var(--fs-base);color:var(--text);background:var(--bg);line-height:1.6;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4{letter-spacing:-0.015em;line-height:1.2}
a{color:inherit;text-decoration:none;transition:color var(--t-fast)}
a:hover{color:var(--primary-700)}
button{font-family:inherit;cursor:pointer;border:0;background:transparent;color:inherit}
img,svg{display:block;max-width:100%}
ul{list-style:none}
.container{max-width:var(--maxw);margin:0 auto;padding:0 var(--s-8)}
@media(max-width:768px){.container{padding:0 var(--s-6)}}
@media(max-width:480px){.container{padding:0 var(--s-4)}}

/* TOPBAR */
.topbar{background:var(--primary-700);color:var(--bg);font-size:13px;font-weight:500}
.topbar.hidden{display:none}
.topbar .container{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:var(--s-4);min-height:36px}
.topbar a{color:var(--bg)}
.topbar a:hover{color:var(--accent-gold)}
.topbar .tb-left{justify-self:start}
.topbar .tb-mid{justify-self:center;text-align:center}
.topbar .tb-mid b{color:var(--accent-gold);font-weight:700;letter-spacing:.04em}
.topbar .tb-right{justify-self:end;display:flex;align-items:center;gap:var(--s-3)}
.topbar .tb-close{color:var(--bg);opacity:.8;width:28px;height:28px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center}
.topbar .tb-close:hover{background:rgba(255,255,255,.12);opacity:1}
@media(max-width:768px){.topbar .container{grid-template-columns:1fr auto}.topbar .tb-left{display:none}}

/* HEADER */
.header{position:sticky;top:0;z-index:50;background:var(--bg);box-shadow:var(--shadow-header);border-bottom:1px solid var(--border)}
.header-row1{display:flex;align-items:center;gap:var(--s-6);height:88px}
.brand-logo{font-size:30px;font-weight:800;letter-spacing:-0.025em;color:var(--primary-700);font-style:italic}
.brand-logo:hover{color:var(--primary-700)}
.header-actions{display:flex;align-items:center;gap:var(--s-2)}
.icon-btn{position:relative;width:42px;height:42px;display:inline-flex;align-items:center;justify-content:center;border-radius:50%;color:var(--text);transition:background var(--t-fast),color var(--t-fast)}
.icon-btn i{font-size:var(--icon-md)}
.icon-btn:hover{background:var(--primary-100);color:var(--primary-700)}
.cart-badge .cart-num{position:absolute;top:-2px;right:-2px;background:var(--accent-gold);color:var(--primary-900);font-size:11px;font-weight:700;width:18px;height:18px;border-radius:50%;display:flex;align-items:center;justify-content:center;border:2px solid var(--bg)}
.header-top{background:var(--bg);border-bottom:1px solid var(--border);font-size:var(--fs-xs)}
.header-top .container{display:flex;justify-content:flex-end;align-items:center;gap:var(--s-5);min-height:38px}
.header-top .top-link{font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:var(--text-2);padding:6px 4px;display:inline-flex;align-items:center;gap:6px;position:relative}
.header-top .top-link i{font-size:10px;color:var(--muted)}
.header-top .top-link:hover{color:var(--primary-700)}
.header-top .has-dd{cursor:pointer}
.header-top .dd-menu{position:absolute;top:calc(100% + 2px);right:0;background:#fff;border:1px solid var(--border);border-radius:var(--r-sm);box-shadow:var(--shadow-2);padding:4px 0;min-width:160px;display:none;z-index:60}
.header-top .has-dd:hover .dd-menu,.header-top .dd-menu:hover{display:block}
.header-top .dd-menu a{display:block;padding:7px 14px;font-size:var(--fs-xs);font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:var(--text-2);text-align:right;line-height:1.3}
.header-top .dd-menu a:hover{background:var(--primary-100);color:var(--primary-700)}
.nav{display:flex;justify-content:center;gap:var(--s-8);flex:1}
.nav a{font-size:var(--fs-sm);font-weight:600;letter-spacing:.05em;text-transform:uppercase;padding:8px 0;position:relative;color:var(--text);white-space:nowrap}
.nav a::after{content:"";position:absolute;left:0;bottom:0;height:2px;width:0;background:var(--primary-700);transition:width var(--t-fast)}
.nav a:hover::after,.nav a.active::after{width:100%}
.nav a.active{color:var(--primary-700)}
@media(max-width:1024px){.nav{display:none}.header-row1{height:auto;padding:var(--s-4) 0;gap:var(--s-4)}.header-top{display:none}}

/* USER DROPDOWN */
.user-dd-wrap{position:relative}
.user-dd-wrap:hover .user-dd-menu,.user-dd-menu:hover{display:block}
.user-dd-menu{position:absolute;top:calc(100% + 4px);right:0;background:#fff;border:1px solid var(--border);border-radius:var(--r-md);box-shadow:var(--shadow-2);padding:var(--s-2) 0;min-width:220px;display:none;z-index:60}
.user-dd-menu a{display:flex;align-items:center;gap:var(--s-3);padding:10px 16px;font-size:var(--fs-sm);color:var(--text-2);font-weight:600}
.user-dd-menu a i{width:18px;color:var(--muted);font-size:var(--icon-sm)}
.user-dd-menu a:hover{background:var(--primary-100);color:var(--primary-700)}
.user-dd-menu a:hover i{color:var(--primary-700)}
.user-dd-menu .divider{height:1px;background:var(--border);margin:var(--s-2) 0}

/* BUTTONS */
.btn{display:inline-flex;align-items:center;gap:var(--s-2);padding:14px 28px;border-radius:var(--r-sm);font-size:var(--fs-sm);font-weight:700;letter-spacing:.04em;text-transform:uppercase;transition:transform var(--t-fast),background var(--t-fast),color var(--t-fast)}
.btn-primary{background:var(--primary-700);color:#fff}
.btn-primary:hover{background:var(--primary-900);color:#fff;transform:translateY(-2px)}
.btn-outline{background:transparent;color:var(--primary-700);border:2px solid var(--primary-700)}
.btn-outline:hover{background:var(--primary-700);color:#fff}

/* BREADCRUMB */
.crumb{font-size:var(--fs-sm);color:var(--muted);padding:var(--s-6) 0;display:flex;align-items:center;gap:var(--s-2);flex-wrap:wrap}
.crumb a{color:var(--muted)}
.crumb a:hover{color:var(--primary-700)}
.crumb .sep{font-size:10px;color:var(--muted-2)}
.crumb .active{color:var(--text);font-weight:600}

/* FOOTER */
.footer{background:var(--bg-section);padding:var(--s-12) 0 var(--s-6);margin-top:96px}
.footer-cols{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:var(--s-8);padding-bottom:var(--s-10);border-bottom:1px solid var(--border)}
.footer h4{font-size:var(--fs-sm);font-weight:800;letter-spacing:.05em;text-transform:uppercase;margin-bottom:var(--s-4)}
.footer ul li{padding:6px 0}
.footer ul li a{color:var(--text-2);font-size:var(--fs-sm)}
.footer-brand p{color:var(--muted);font-size:var(--fs-sm);margin-top:var(--s-3);max-width:300px}
.footer-bottom{padding-top:var(--s-5);display:flex;justify-content:space-between;align-items:center;font-size:var(--fs-xs);color:var(--muted);flex-wrap:wrap;gap:var(--s-4)}
.socials{display:flex;gap:var(--s-3);margin-top:var(--s-4)}
.socials a{width:38px;height:38px;border-radius:50%;background:var(--bg);display:flex;align-items:center;justify-content:center;color:var(--text-2);transition:all var(--t-fast)}
.socials a i{font-size:var(--icon-md)}
.socials a:hover{background:var(--primary-700);color:#fff}
.policies{display:flex;gap:var(--s-4);flex-wrap:wrap}
.contact-line{display:flex;align-items:center;gap:var(--s-2);color:var(--text-2);font-size:var(--fs-sm);padding:6px 0}
.contact-line i{color:var(--primary-700);width:16px}

/* ============ ACCOUNT DASHBOARD ============ */
.account-page-head{padding:var(--s-2) 0 var(--s-6)}
.account-page-head h1{font-size:36px;font-weight:700;letter-spacing:-0.02em;margin-bottom:var(--s-2)}
.account-page-head .lead{color:var(--text-2);max-width:640px}

.account-layout{display:grid;grid-template-columns:280px 1fr;gap:var(--s-8);padding:var(--s-2) 0 96px;align-items:start}
.account-side{position:sticky;top:120px;align-self:start;background:#fff;border:1px solid var(--border);border-radius:var(--r-lg);overflow:hidden}
.account-side .user{padding:var(--s-5) var(--s-6);display:flex;align-items:center;gap:var(--s-3);border-bottom:1px solid var(--border)}
.account-side .avatar{width:48px;height:48px;border-radius:50%;background:#F4D7D9;color:#8B3A3A;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:18px;flex-shrink:0}
.account-side .user-info b{display:block;font-size:var(--fs-sm);font-weight:700;color:var(--text);line-height:1.3}
.account-side .user-info span{display:block;font-size:11px;color:var(--muted);margin-top:2px}
.account-side nav{display:flex;flex-direction:column;padding:var(--s-2) 0}
.account-side nav a{display:flex;align-items:center;gap:var(--s-3);padding:13px 22px;font-size:var(--fs-sm);font-weight:600;color:var(--text-2);border-left:3px solid transparent;transition:all var(--t-fast)}
.account-side nav a i{width:18px;color:var(--muted);font-size:var(--icon-md);text-align:center}
.account-side nav a:hover{background:var(--primary-100);color:var(--primary-700)}
.account-side nav a:hover i{color:var(--primary-700)}
.account-side nav a.active{border-left-color:var(--primary-700);background:var(--primary-100);color:var(--primary-700)}
.account-side nav a.active i{color:var(--primary-700)}
.account-side .signout-wrap{border-top:1px solid var(--border);padding:var(--s-2) 0}
.account-side .signout-wrap a{color:var(--accent-red)}
.account-side .signout-wrap a:hover{background:#FBEDEB;color:var(--accent-red)}
.account-side .signout-wrap a i{color:var(--accent-red)}

.account-content{min-width:0}
.acc-section-title{font-size:22px;font-weight:700;margin-bottom:var(--s-2);color:var(--text)}
.acc-section-sub{color:var(--text-2);font-size:var(--fs-sm);margin-bottom:var(--s-5)}

/* CHIPS */
.chips{display:flex;gap:var(--s-2);flex-wrap:wrap;margin-bottom:var(--s-5)}
.chip{padding:8px 18px;border-radius:var(--r-pill);background:var(--bg-soft);color:var(--text-2);font-size:var(--fs-sm);font-weight:600;border:1px solid transparent;cursor:pointer;transition:all var(--t-fast)}
.chip:hover{background:var(--primary-100);color:var(--primary-700)}
.chip.active{background:var(--accent-gold);color:var(--primary-900);border-color:var(--accent-gold)}

/* FORM */
.acc-form{background:#fff;border:1px solid var(--border);border-radius:var(--r-lg);padding:var(--s-8)}
.acc-form .form-row{display:grid;grid-template-columns:1fr 1fr;gap:var(--s-5);margin-bottom:var(--s-5)}
.acc-form .field{display:flex;flex-direction:column}
.acc-form .field.full{grid-column:1/-1}
.acc-form label{font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin-bottom:6px}
.acc-form input,.acc-form select,.acc-form textarea{padding:12px 14px;border:1px solid var(--border);border-radius:var(--r-sm);font-family:inherit;font-size:var(--fs-sm);background:#fff;color:var(--text);width:100%}
.acc-form input:focus,.acc-form select:focus,.acc-form textarea:focus{outline:none;border-color:var(--primary-700);box-shadow:0 0 0 2px rgba(59,74,42,.08)}
.acc-form input[disabled]{background:var(--bg-soft);color:var(--muted);cursor:not-allowed}
.acc-form .check-row{display:flex;align-items:center;gap:var(--s-2);font-size:var(--fs-sm);color:var(--text-2);margin:var(--s-3) 0;cursor:pointer}
.acc-form .check-row input{width:16px;height:16px;accent-color:var(--primary-700);margin-right:var(--s-2)}
.acc-form .form-actions{display:flex;justify-content:flex-end;gap:var(--s-3);margin-top:var(--s-6);padding-top:var(--s-6);border-top:1px solid var(--border)}
.acc-form h2{font-size:var(--fs-lg);font-weight:700;margin-bottom:var(--s-2);color:var(--text)}
.acc-form .form-section-sub{color:var(--muted);font-size:var(--fs-sm);margin-bottom:var(--s-5)}
.acc-form + .acc-form{margin-top:var(--s-5)}

/* ORDER CARD */
.order-card{background:#fff;border:1px solid var(--border);border-radius:var(--r-lg);overflow:hidden;margin-bottom:var(--s-4);transition:border-color var(--t-fast)}
.order-card:hover{border-color:var(--primary-700)}
.order-head{display:grid;grid-template-columns:repeat(4,1fr) auto;gap:var(--s-5);padding:var(--s-5) var(--s-6);background:var(--bg-product);border-bottom:1px solid var(--border);align-items:center}
.order-head .col span{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);font-weight:700;margin-bottom:4px}
.order-head .col b{display:block;font-size:var(--fs-sm);font-weight:700;color:var(--text)}
.btn-detail{padding:10px 22px;border-radius:var(--r-sm);background:transparent;border:1.5px solid var(--primary-700);color:var(--primary-700);font-weight:700;font-size:var(--fs-xs);text-transform:uppercase;letter-spacing:.04em;transition:all var(--t-fast);cursor:pointer;white-space:nowrap}
.btn-detail:hover{background:var(--primary-700);color:#fff}
.order-body{display:flex;align-items:center;gap:var(--s-5);padding:var(--s-5) var(--s-6)}
.order-body .thumb{width:72px;height:72px;border-radius:var(--r-md);background:var(--bg-product);overflow:hidden;flex-shrink:0;border:1px solid var(--border)}
.order-body .thumb img{width:100%;height:100%;object-fit:cover}
.order-status-col{flex:1;display:flex;flex-direction:column;gap:6px;min-width:0}
.badge-status{display:inline-flex;align-items:center;gap:6px;font-size:var(--fs-xs);font-weight:700;color:var(--accent-success);text-transform:uppercase;letter-spacing:.04em;width:max-content}
.badge-status.pending{color:var(--accent-gold)}
.badge-status.cancelled{color:var(--accent-red)}
.badge-status i{font-size:11px}
.order-status-col p{font-size:var(--fs-sm);color:var(--text-2)}
.btn-review{padding:10px 18px;border-radius:var(--r-sm);background:var(--accent-gold);color:var(--primary-900);font-weight:700;font-size:var(--fs-xs);text-transform:uppercase;letter-spacing:.04em;transition:all var(--t-fast);white-space:nowrap;border:0;cursor:pointer}
.btn-review:hover{background:#d8b46c;transform:translateY(-1px)}

/* ADDRESS */
.addr-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:var(--s-4)}
.addr-card{background:#fff;border:1px solid var(--border);border-radius:var(--r-lg);padding:var(--s-6);position:relative;transition:border-color var(--t-fast)}
.addr-card:hover{border-color:var(--primary-700)}
.addr-card .addr-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:var(--s-4);padding-bottom:var(--s-3);border-bottom:1px solid var(--border)}
.addr-card .addr-title{display:inline-flex;align-items:center;gap:var(--s-2);font-size:var(--fs-md);font-weight:700;color:var(--text)}
.addr-card .addr-title i{color:var(--primary-700)}
.addr-card .default-tag{display:inline-block;background:var(--primary-100);color:var(--primary-700);font-size:10px;font-weight:700;padding:3px 8px;border-radius:var(--r-pill);text-transform:uppercase;letter-spacing:.06em;margin-left:6px}
.addr-card .addr-actions{display:flex;gap:var(--s-2)}
.addr-card .addr-actions button{width:32px;height:32px;border-radius:var(--r-sm);background:var(--bg-soft);color:var(--text-2);display:inline-flex;align-items:center;justify-content:center;transition:all var(--t-fast)}
.addr-card .addr-actions button:hover{background:var(--primary-700);color:#fff}
.addr-card .addr-actions button.danger:hover{background:var(--accent-red)}
.addr-card .addr-name{font-weight:700;color:var(--text);margin-bottom:var(--s-2);font-size:var(--fs-sm)}
.addr-card p{font-size:var(--fs-sm);color:var(--text-2);line-height:1.6}
.addr-card .addr-phone{margin-top:var(--s-3);padding-top:var(--s-3);border-top:1px solid var(--border);color:var(--muted);font-size:var(--fs-xs);display:inline-flex;align-items:center;gap:6px}
.addr-card .addr-phone i{color:var(--primary-700)}
.addr-add{background:transparent;border:2px dashed var(--border);border-radius:var(--r-lg);padding:var(--s-8);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:var(--s-3);color:var(--muted);font-weight:700;cursor:pointer;text-transform:uppercase;letter-spacing:.04em;font-size:var(--fs-sm);transition:all var(--t-fast);min-height:200px;text-align:center}
.addr-add i{font-size:28px;color:var(--muted)}
.addr-add:hover{border-color:var(--primary-700);color:var(--primary-700);background:var(--bg-product)}
.addr-add:hover i{color:var(--primary-700)}

/* ACC TABS */
.acc-tabs{display:flex;gap:0;border-bottom:1px solid var(--border);margin-bottom:var(--s-6)}
.acc-tabs button{padding:var(--s-4) var(--s-5);font-size:var(--fs-sm);font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.04em;border-bottom:3px solid transparent;cursor:pointer;transition:all var(--t-fast)}
.acc-tabs button:hover{color:var(--text)}
.acc-tabs button.active{color:var(--primary-700);border-bottom-color:var(--primary-700)}
.acc-tab-panel{display:none}
.acc-tab-panel.active{display:block}

/* EMPTY STATE */
.empty-state{background:#fff;border:1px solid var(--border);border-radius:var(--r-lg);padding:var(--s-12) var(--s-8);text-align:center}
.empty-state i{font-size:48px;color:var(--muted-2);margin-bottom:var(--s-4)}
.empty-state h3{font-size:var(--fs-lg);font-weight:700;margin-bottom:var(--s-2)}
.empty-state p{color:var(--text-2);margin-bottom:var(--s-5)}

/* PROMO */
.promo-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:var(--s-4)}
.promo-card{background:#fff;border:1px solid var(--border);border-radius:var(--r-lg);padding:var(--s-5) var(--s-6);position:relative;display:grid;grid-template-columns:auto 1fr auto;gap:var(--s-4);align-items:center;transition:border-color var(--t-fast)}
.promo-card:hover{border-color:var(--accent-gold)}
.promo-card .promo-icon{width:64px;height:64px;border-radius:var(--r-md);background:var(--primary-100);display:flex;align-items:center;justify-content:center;color:var(--primary-700);font-size:26px;flex-shrink:0}
.promo-card .promo-icon.gold{background:#FBF1DC;color:var(--accent-gold)}
.promo-card .promo-body h3{font-size:var(--fs-md);font-weight:700;margin-bottom:4px;line-height:1.3}
.promo-card .promo-amount{font-size:22px;font-weight:800;color:var(--accent-gold);letter-spacing:-0.02em;margin-bottom:6px}
.promo-card .promo-meta{font-size:var(--fs-xs);color:var(--muted);line-height:1.5}
.promo-card .promo-meta .date{color:var(--accent-red);font-weight:700}
.promo-card .badge-soon{position:absolute;top:var(--s-3);right:var(--s-3);background:var(--accent-red);color:#fff;font-size:10px;font-weight:700;padding:3px 8px;border-radius:var(--r-pill);text-transform:uppercase;letter-spacing:.04em}
.btn-use{padding:10px 18px;border-radius:var(--r-sm);background:var(--primary-700);color:#fff;font-weight:700;font-size:var(--fs-xs);text-transform:uppercase;letter-spacing:.04em;white-space:nowrap;transition:all var(--t-fast);border:0;cursor:pointer}
.btn-use:hover{background:var(--primary-900);color:#fff}

@media(max-width:1024px){
  .account-layout{grid-template-columns:1fr;gap:var(--s-5)}
  .account-side{position:static}
  .order-head{grid-template-columns:repeat(2,1fr);gap:var(--s-3)}
  .addr-grid,.promo-grid{grid-template-columns:1fr}
  .acc-form .form-row{grid-template-columns:1fr}
}
@media(max-width:480px){
  .promo-card{grid-template-columns:auto 1fr;gap:var(--s-3)}
  .promo-card .btn-use{grid-column:1/-1;justify-self:start}
}
"""

def header(active_main=""):
    """Header with topbar + secondary + main row + user dropdown."""
    nav_classes = {
        "magaza": "active" if active_main == "magaza" else "",
    }
    return f'''
<!-- TOP RIBBON -->
<div class="topbar" id="topRibbon">
  <div class="container">
    <a class="tb-left" href="kurumsal-satis.html">Kurumsal Hediyeler · kurumlara özel fiyatlarla <i class="fa-solid fa-arrow-right" style="font-size:11px;margin-left:4px;"></i></a>
    <span class="tb-mid">750 TL ÜZERİ <b>KARGO ÜCRETSİZ</b> · YENİ HASAT ÜRÜNLERİ STOKTA</span>
    <span class="tb-right">
      <button class="tb-close" aria-label="Kapat" onclick="document.getElementById('topRibbon').classList.add('hidden')"><i class="fa-solid fa-xmark"></i></button>
    </span>
  </div>
</div>

<!-- HEADER TOP -->
<div class="header-top">
  <div class="container">
    <a href="kurumsal-satis.html" class="top-link">Kurumsal Satış</a>
    <span class="top-link has-dd">Hakkımızda <i class="fa-solid fa-chevron-down"></i>
      <span class="dd-menu">
        <a href="hikayemiz.html">Hikayemiz</a>
        <a href="uretim.html">Üretim</a>
        <a href="#magazalar">Mağazalar</a>
        <a href="iletisim.html">İletişim</a>
      </span>
    </span>
  </div>
</div>

<!-- HEADER -->
<header class="header">
  <div class="container header-row1">
    <a href="index.html" class="brand-logo">Derik</a>
    <nav class="nav">
      <a href="magaza.html" class="{nav_classes['magaza']}">Zeytinyağları</a>
      <a href="#zeytinler">Zeytinler</a>
      <a href="#sabunlar">Sabunlar</a>
      <a href="#dogal">Doğal Ürünler</a>
      <a href="#hediye">Hediye Setleri</a>
    </nav>
    <div class="header-actions">
      <a href="#ara" class="icon-btn" aria-label="Ara"><i class="fa-solid fa-magnifying-glass"></i></a>
      <span class="user-dd-wrap">
        <a href="uyelik-bilgilerim.html" class="icon-btn" aria-label="Hesabım"><i class="fa-regular fa-user"></i></a>
        <span class="user-dd-menu">
          <a href="uyelik-bilgilerim.html"><i class="fa-regular fa-id-card"></i> Üyelik Bilgilerim</a>
          <a href="siparis-gecmisim.html"><i class="fa-solid fa-box"></i> Sipariş Geçmişim</a>
          <a href="adreslerim.html"><i class="fa-solid fa-location-dot"></i> Adreslerim</a>
          <a href="promosyonlarim.html"><i class="fa-solid fa-ticket"></i> Promosyonlarım</a>
          <span class="divider"></span>
          <a href="#"><i class="fa-solid fa-right-from-bracket"></i> Çıkış Yap</a>
        </span>
      </span>
      <a href="#favoriler" class="icon-btn" aria-label="Favoriler"><i class="fa-regular fa-heart"></i></a>
      <a href="#sepet" class="icon-btn cart-badge" aria-label="Sepetim"><i class="fa-solid fa-bag-shopping"></i><span class="cart-num">0</span></a>
    </div>
  </div>
</header>
'''

def sidebar(active):
    """Account sidebar. active: uyelik|siparis|adres|promo"""
    items = [
        ("uyelik", "uyelik-bilgilerim.html", "fa-regular fa-id-card", "Üyelik Bilgilerim"),
        ("siparis", "siparis-gecmisim.html", "fa-solid fa-box", "Sipariş Geçmişim"),
        ("adres", "adreslerim.html", "fa-solid fa-location-dot", "Adreslerim"),
        ("promo", "promosyonlarim.html", "fa-solid fa-ticket", "Promosyonlarım"),
    ]
    nav_html = ""
    for key, href, ico, label in items:
        cls = "active" if key == active else ""
        nav_html += f'      <a href="{href}" class="{cls}"><i class="{ico}"></i> {label}</a>\n'
    return f'''<aside class="account-side">
  <div class="user">
    <div class="avatar">B</div>
    <div class="user-info">
      <b>Beyar Güneş</b>
      <span>beyar@derik.com</span>
    </div>
  </div>
  <nav>
{nav_html}  </nav>
  <div class="signout-wrap">
    <nav><a href="#"><i class="fa-solid fa-right-from-bracket"></i> Çıkış Yap</a></nav>
  </div>
</aside>
'''

FOOTER = '''
<footer class="footer">
  <div class="container">
    <div class="footer-cols">
      <div class="footer-brand">
        <span class="brand-logo">Derik</span>
        <p>Mardin Derik'ten sofranıza.</p>
        <div class="contact-line"><i class="fa-solid fa-location-dot"></i> Mardin Derik, Türkiye</div>
        <div class="contact-line"><i class="fa-solid fa-envelope"></i> info@derikzeytin.com</div>
        <div class="contact-line"><i class="fa-brands fa-whatsapp"></i> 0 (850) 393 7070</div>
        <div class="socials">
          <a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
          <a href="#" aria-label="Facebook"><i class="fa-brands fa-facebook"></i></a>
          <a href="#" aria-label="X"><i class="fa-brands fa-x-twitter"></i></a>
          <a href="#" aria-label="YouTube"><i class="fa-brands fa-youtube"></i></a>
        </div>
      </div>
      <div>
        <h4>Kategoriler</h4>
        <ul>
          <li><a href="magaza.html">Zeytinyağları</a></li>
          <li><a href="#zeytinler">Zeytinler</a></li>
          <li><a href="#sabunlar">Sabunlar</a></li>
          <li><a href="#dogal">Doğal Ürünler</a></li>
          <li><a href="#hediye">Hediye Setleri</a></li>
        </ul>
      </div>
      <div>
        <h4>Kurumsal</h4>
        <ul>
          <li><a href="#hakkimizda">Hakkımızda</a></li>
          <li><a href="hikayemiz.html">Derik'in Hikâyesi</a></li>
          <li><a href="uretim.html">Üretim Sürecimiz</a></li>
          <li><a href="kurumsal-satis.html">Kurumsal Satış</a></li>
          <li><a href="iletisim.html">İletişim</a></li>
        </ul>
      </div>
      <div>
        <h4>Yardım</h4>
        <ul>
          <li><a href="sss.html">Sıkça Sorulan Sorular</a></li>
          <li><a href="#iade">İade ve Değişim</a></li>
          <li><a href="iletisim.html">İletişim</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy;2026 Derik. Tüm hakları saklıdır.</span>
      <div class="policies">
        <a href="#">KVKK</a>
        <a href="#">Gizlilik</a>
        <a href="#">Mesafeli Satış</a>
        <a href="#">Çerez Politikası</a>
      </div>
    </div>
  </div>
</footer>
'''

JS = '''
<script>
// Chips toggle
document.querySelectorAll('.chips').forEach(g => {
  g.addEventListener('click', e => {
    if (e.target.matches('.chip')) {
      g.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
      e.target.classList.add('active');
    }
  });
});
// Tabs
document.querySelectorAll('.acc-tabs').forEach(g => {
  g.addEventListener('click', e => {
    if (e.target.matches('button')) {
      const id = e.target.dataset.tab;
      g.querySelectorAll('button').forEach(b => b.classList.remove('active'));
      e.target.classList.add('active');
      document.querySelectorAll('.acc-tab-panel').forEach(p => p.classList.toggle('active', p.id === id));
    }
  });
});
</script>
'''

def page(title, active, breadcrumb_label, head_h1, head_lead, content):
    return f'''<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Derik</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" crossorigin="anonymous" referrerpolicy="no-referrer">
<style>{BASE_CSS}</style>
</head>
<body>
{header()}

<div class="container">
  <nav class="crumb">
    <a href="index.html">Anasayfa</a>
    <i class="fa-solid fa-chevron-right sep"></i>
    <span class="active">{breadcrumb_label}</span>
  </nav>
</div>

<div class="container account-page-head">
  <h1>{head_h1}</h1>
  <p class="lead">{head_lead}</p>
</div>

<div class="container">
  <div class="account-layout">
    {sidebar(active)}
    <div class="account-content">
{content}
    </div>
  </div>
</div>

{FOOTER}
{JS}
</body>
</html>
'''

# ============ PAGE CONTENT ============

UYELIK_CONTENT = '''      <form class="acc-form">
        <h2>Kişisel Bilgiler</h2>
        <p class="form-section-sub">Profil bilgilerinizi güncel tutun, kargo ve fatura işlemlerinde kullanılır.</p>
        <div class="form-row">
          <div class="field">
            <label for="ad">Ad</label>
            <input id="ad" type="text" value="Beyar">
          </div>
          <div class="field">
            <label for="soyad">Soyad</label>
            <input id="soyad" type="text" value="Güneş">
          </div>
          <div class="field">
            <label for="email">E-posta</label>
            <input id="email" type="email" value="beyar@derik.com" disabled>
          </div>
          <div class="field">
            <label for="tel">Telefon</label>
            <input id="tel" type="tel" value="0 (546) 123 4575" placeholder="0 (5xx) xxx xx xx">
          </div>
          <div class="field">
            <label for="dogum">Doğum Tarihi</label>
            <input id="dogum" type="date" value="1990-06-15">
          </div>
          <div class="field">
            <label for="cinsiyet">Cinsiyet</label>
            <select id="cinsiyet">
              <option value="">Belirtilmemiş</option>
              <option selected>Erkek</option>
              <option>Kadın</option>
              <option>Belirtmek istemiyorum</option>
            </select>
          </div>
        </div>
        <label class="check-row"><input type="checkbox" checked> Yeni ürünler ve kampanyalardan e-posta ile haberdar olmak istiyorum</label>
        <label class="check-row"><input type="checkbox"> SMS ile bildirim almak istiyorum</label>
        <div class="form-actions">
          <button type="button" class="btn btn-outline">İptal</button>
          <button type="submit" class="btn btn-primary">Kaydet <i class="fa-solid fa-check"></i></button>
        </div>
      </form>

      <form class="acc-form">
        <h2>Şifre Değiştir</h2>
        <p class="form-section-sub">Güvenliğiniz için şifrenizi düzenli aralıklarla güncelleyin.</p>
        <div class="form-row">
          <div class="field full">
            <label for="pw-old">Mevcut Şifre</label>
            <input id="pw-old" type="password" placeholder="••••••••">
          </div>
          <div class="field">
            <label for="pw-new">Yeni Şifre</label>
            <input id="pw-new" type="password" placeholder="En az 8 karakter">
          </div>
          <div class="field">
            <label for="pw-new2">Yeni Şifre (Tekrar)</label>
            <input id="pw-new2" type="password" placeholder="Yeni şifrenizi tekrar girin">
          </div>
        </div>
        <div class="form-actions">
          <button type="submit" class="btn btn-primary">Şifreyi Güncelle <i class="fa-solid fa-lock"></i></button>
        </div>
      </form>'''

SIPARIS_CONTENT = '''      <div class="chips">
        <button class="chip active">Tümü</button>
        <button class="chip">Devam Edenler</button>
        <button class="chip">İptaller</button>
        <button class="chip">İadeler</button>
      </div>

      <div class="order-card">
        <div class="order-head">
          <div class="col"><span>Sipariş Tarihi</span><b>12 Nisan 2026</b></div>
          <div class="col"><span>Sipariş No</span><b>DRK-104872</b></div>
          <div class="col"><span>Alıcı</span><b>Beyar Güneş</b></div>
          <div class="col"><span>Toplam</span><b>1.245,00 TL</b></div>
          <a href="#" class="btn-detail">Detaylar</a>
        </div>
        <div class="order-body">
          <div class="thumb"><img src="https://images.unsplash.com/photo-1620577573039-a96c2c0e4e84?w=200&h=200&fit=crop" alt="Erken Hasat 500ml" data-fallback></div>
          <div class="order-status-col">
            <span class="badge-status"><i class="fa-solid fa-circle-check"></i> Teslim Edildi</span>
            <p>Erken Hasat Naturel Sızma Zeytinyağı 500ml · 2 ürün teslim edildi</p>
          </div>
          <button class="btn-review">Değerlendir</button>
        </div>
      </div>

      <div class="order-card">
        <div class="order-head">
          <div class="col"><span>Sipariş Tarihi</span><b>3 Nisan 2026</b></div>
          <div class="col"><span>Sipariş No</span><b>DRK-103219</b></div>
          <div class="col"><span>Alıcı</span><b>Beyar Güneş</b></div>
          <div class="col"><span>Toplam</span><b>680,00 TL</b></div>
          <a href="#" class="btn-detail">Detaylar</a>
        </div>
        <div class="order-body">
          <div class="thumb"><img src="https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=200&h=200&fit=crop" alt="Halhalı Yeşil Zeytin" data-fallback></div>
          <div class="order-status-col">
            <span class="badge-status pending"><i class="fa-solid fa-truck"></i> Kargoda</span>
            <p>Halhalı Yeşil Zeytin 1kg · Tahmini teslim 15 Nisan</p>
          </div>
          <a href="#" class="btn-detail">Kargo Takip</a>
        </div>
      </div>

      <div class="order-card">
        <div class="order-head">
          <div class="col"><span>Sipariş Tarihi</span><b>22 Mart 2026</b></div>
          <div class="col"><span>Sipariş No</span><b>DRK-102540</b></div>
          <div class="col"><span>Alıcı</span><b>Beyar Güneş</b></div>
          <div class="col"><span>Toplam</span><b>2.150,00 TL</b></div>
          <a href="#" class="btn-detail">Detaylar</a>
        </div>
        <div class="order-body">
          <div class="thumb"><img src="https://images.unsplash.com/photo-1611171711912-e3e9d31bbe7c?w=200&h=200&fit=crop" alt="Hediye Seti" data-fallback></div>
          <div class="order-status-col">
            <span class="badge-status"><i class="fa-solid fa-circle-check"></i> Teslim Edildi</span>
            <p>Derik Hediye Seti — 3 ürün · 1 ürün teslim edildi</p>
          </div>
          <button class="btn-review">Değerlendir</button>
        </div>
      </div>'''

ADRES_CONTENT = '''      <div class="acc-tabs">
        <button class="active" data-tab="tab-teslimat">Teslimat Adreslerim</button>
        <button data-tab="tab-fatura">Fatura Bilgilerim</button>
      </div>

      <div id="tab-teslimat" class="acc-tab-panel active">
        <div class="addr-grid">
          <div class="addr-card">
            <div class="addr-head">
              <span class="addr-title"><i class="fa-solid fa-house"></i> Ev <span class="default-tag">Varsayılan</span></span>
              <div class="addr-actions">
                <button aria-label="Düzenle"><i class="fa-solid fa-pen"></i></button>
                <button class="danger" aria-label="Sil"><i class="fa-regular fa-trash-can"></i></button>
              </div>
            </div>
            <div class="addr-name">Beyar Güneş</div>
            <p>Caferağa Mahallesi, Moda Caddesi No:42 Daire 5</p>
            <p>Kadıköy / İstanbul</p>
            <div class="addr-phone"><i class="fa-solid fa-phone"></i> 0 (546) **** 75</div>
          </div>

          <a href="#" class="addr-add">
            <i class="fa-solid fa-plus"></i>
            Yeni Adres Ekle
          </a>
        </div>
      </div>

      <div id="tab-fatura" class="acc-tab-panel">
        <div class="empty-state">
          <i class="fa-regular fa-file-lines"></i>
          <h3>Henüz fatura bilginiz yok</h3>
          <p>Kurumsal alımlarınız için fatura bilgilerinizi ekleyebilirsiniz.</p>
          <a href="#" class="btn btn-primary"><i class="fa-solid fa-plus"></i> Fatura Bilgisi Ekle</a>
        </div>
      </div>'''

PROMO_CONTENT = '''      <div class="chips">
        <button class="chip active">Tümü</button>
        <button class="chip">Avantajlı Kupon</button>
        <button class="chip">Sana Özel</button>
      </div>

      <div class="promo-grid">
        <div class="promo-card">
          <span class="badge-soon">Son 3 Gün</span>
          <div class="promo-icon gold"><i class="fa-solid fa-percent"></i></div>
          <div class="promo-body">
            <h3>İlk Sipariş İndirimi</h3>
            <div class="promo-amount">%15 İndirim</div>
            <div class="promo-meta">Min. 500 TL alışveriş · <span class="date">Son tarih: 7 Mayıs 2026</span></div>
          </div>
          <button class="btn-use">Kullan</button>
        </div>

        <div class="promo-card">
          <div class="promo-icon"><i class="fa-solid fa-truck-fast"></i></div>
          <div class="promo-body">
            <h3>Ücretsiz Kargo</h3>
            <div class="promo-amount">75 TL Hediye</div>
            <div class="promo-meta">Min. 750 TL alışveriş · <span class="date">Son tarih: 31 Mayıs 2026</span></div>
          </div>
          <button class="btn-use">Kullan</button>
        </div>

        <div class="promo-card">
          <div class="promo-icon gold"><i class="fa-solid fa-gift"></i></div>
          <div class="promo-body">
            <h3>Doğum Günü Hediyesi</h3>
            <div class="promo-amount">100 TL Kupon</div>
            <div class="promo-meta">Tüm kategorilerde geçerli · <span class="date">Son tarih: 15 Haziran 2026</span></div>
          </div>
          <button class="btn-use">Kullan</button>
        </div>
      </div>'''

PAGES = [
    {
        "file": "uyelik-bilgilerim.html",
        "title": "Üyelik Bilgilerim",
        "active": "uyelik",
        "breadcrumb": "Üyelik Bilgilerim",
        "h1": "Üyelik Bilgilerim",
        "lead": "Profil bilgilerinizi güncelleyin, şifrenizi yönetin.",
        "content": UYELIK_CONTENT,
    },
    {
        "file": "siparis-gecmisim.html",
        "title": "Sipariş Geçmişim",
        "active": "siparis",
        "breadcrumb": "Sipariş Geçmişim",
        "h1": "Sipariş Geçmişim",
        "lead": "Geçmiş ve devam eden siparişlerinizi takip edin.",
        "content": SIPARIS_CONTENT,
    },
    {
        "file": "adreslerim.html",
        "title": "Adreslerim",
        "active": "adres",
        "breadcrumb": "Adreslerim",
        "h1": "Adreslerim",
        "lead": "Teslimat ve fatura adreslerinizi yönetin.",
        "content": ADRES_CONTENT,
    },
    {
        "file": "promosyonlarim.html",
        "title": "Promosyonlarım",
        "active": "promo",
        "breadcrumb": "Promosyonlarım",
        "h1": "Promosyonlarım",
        "lead": "Size özel kuponlar ve aktif kampanyalar.",
        "content": PROMO_CONTENT,
    },
]

for p in PAGES:
    out = ROOT / p["file"]
    html = page(p["title"], p["active"], p["breadcrumb"], p["h1"], p["lead"], p["content"])
    out.write_text(html)
    print(f"Wrote {out}")

print("Done.")
