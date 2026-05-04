#!/usr/bin/env python3
"""Build 4 auth pages with v3.8.1 — FULL site header (replaces minimal header).

Reuses topbar + header-top + header markup from index.html for visual
consistency across the site. Form/breadcrumb/footer/JS unchanged from v3.7.1.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BASE_CSS = r"""
:root{
  --primary-700:#3B4A2A;--primary-800:#6B7A3F;--primary-900:#2A3520;
  --primary-100:#F2EBDC;--primary-200:#E8DFC9;
  --bg:#FAF6EE;--bg-soft:#F2EBDC;--bg-section:#F2EBDC;
  --bg-card:#E8DFC9;--bg-product:#FAF9F5;
  --text:#2A1F14;--text-2:#4A3A2A;--muted:#8C7A6A;--muted-2:#B5A693;
  --border:#E8DFC9;
  --accent-gold:#C9A55B;--accent-gold-soft:#E8D4A1;
  --accent-earth:#8C6A4A;--accent-red:#B04A3E;--accent-success:#5A7A3A;
  --font:"Inter","Helvetica Neue",system-ui,Arial,sans-serif;
  --fs-xs:12px;--fs-sm:14px;--fs-base:16px;--fs-md:18px;
  --fs-lg:20px;--fs-xl:24px;--fs-2xl:28px;--fs-3xl:36px;
  --icon-sm:14px;--icon-md:18px;
  --s-1:4px;--s-2:8px;--s-3:12px;--s-4:16px;--s-5:20px;--s-6:24px;
  --s-8:32px;--s-10:40px;--s-12:48px;
  --r-sm:6px;--r-md:10px;--r-lg:12px;--r-pill:100px;
  --shadow-1:0 2px 8px rgba(0,0,0,.06);
  --shadow-2:0 6px 20px rgba(42,31,20,.10);
  --shadow-header:0 1px 4px rgba(0,0,0,.04);
  --maxw:1320px;--t-fast:.2s ease;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--font);font-size:var(--fs-base);color:var(--text);background:var(--bg);line-height:1.6;-webkit-font-smoothing:antialiased;min-height:100vh;display:flex;flex-direction:column}
h1,h2,h3{letter-spacing:-0.015em;line-height:1.2}
a{color:inherit;text-decoration:none;transition:color var(--t-fast)}
a:hover{color:var(--primary-700)}
button{font-family:inherit;cursor:pointer;border:0;background:transparent;color:inherit}
ul{list-style:none}
.container{max-width:var(--maxw);margin:0 auto;padding:0 var(--s-8)}
@media(max-width:768px){.container{padding:0 var(--s-6)}}

/* TOP RIBBON */
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

/* HEADER TOP (Kurumsal + Hakkımızda) */
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

/* MAIN NAV */
.nav{display:flex;justify-content:center;gap:var(--s-8);flex:1}
.nav a{font-size:var(--fs-sm);font-weight:600;letter-spacing:.05em;text-transform:uppercase;padding:8px 0;position:relative;color:var(--text);white-space:nowrap}
.nav a::after{content:"";position:absolute;left:0;bottom:0;height:2px;width:0;background:var(--primary-700);transition:width var(--t-fast)}
.nav a:hover::after,.nav a.active::after{width:100%}
.nav a.active{color:var(--primary-700)}
@media(max-width:1024px){.nav{display:none}.header-row1{height:auto;padding:var(--s-4) 0;gap:var(--s-4)}.header-top{display:none}}

/* USER DROPDOWN */
.user-dd-wrap{position:relative;display:inline-flex}
.user-dd-wrap:hover .user-dd-menu,.user-dd-menu:hover{display:block}
.user-dd-menu{position:absolute;top:calc(100% + 4px);right:0;background:#fff;border:1px solid var(--border);border-radius:var(--r-md);box-shadow:var(--shadow-2);padding:var(--s-2) 0;min-width:220px;display:none;z-index:60}
.user-dd-menu a{display:flex;align-items:center;gap:var(--s-3);padding:10px 16px;font-size:var(--fs-sm);color:var(--text-2);font-weight:600}
.user-dd-menu a i{width:18px;color:var(--muted);font-size:var(--icon-sm)}
.user-dd-menu a:hover{background:var(--primary-100);color:var(--primary-700)}
.user-dd-menu a:hover i{color:var(--primary-700)}
.user-dd-menu .divider{height:1px;background:var(--border);margin:var(--s-2) 0;display:block}

/* BREADCRUMB */
.crumb{font-size:var(--fs-sm);color:var(--muted);padding:var(--s-6) 0 var(--s-2);display:flex;align-items:center;gap:var(--s-2);flex-wrap:wrap}
.crumb a{color:var(--primary-700);font-weight:600}
.crumb a:hover{color:var(--primary-900);text-decoration:underline}
.crumb .sep{font-size:10px;color:var(--muted-2)}
.crumb .active{color:var(--text);font-weight:600}

/* MAIN */
main.auth-main{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;padding:var(--s-4) var(--s-4) var(--s-10)}

.auth-card{background:#fff;border:1px solid var(--border);border-radius:var(--r-lg);padding:var(--s-10) var(--s-8);max-width:480px;width:100%;box-shadow:var(--shadow-1)}
.auth-card.wide{max-width:540px}
.auth-card .auth-head{text-align:center;margin-bottom:var(--s-8)}
.auth-card h1{font-size:var(--fs-2xl);font-weight:700;margin-bottom:var(--s-2);color:var(--text)}
.auth-card .lead{color:var(--text-2);font-size:var(--fs-sm)}

.continue-link{display:inline-flex;align-items:center;gap:6px;font-size:var(--fs-sm);color:var(--text-2);font-weight:600;margin-top:var(--s-6);transition:color var(--t-fast)}
.continue-link:hover{color:var(--primary-700)}

.field{display:flex;flex-direction:column;margin-bottom:var(--s-4)}
.field-row{display:grid;grid-template-columns:1fr 1fr;gap:var(--s-3);margin-bottom:var(--s-4)}
.field-row .field{margin-bottom:0}
.field label{font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin-bottom:6px}
.field label .req{color:var(--accent-gold);margin-left:2px}
.field input{padding:13px 14px;border:1px solid var(--border);border-radius:var(--r-sm);font-family:inherit;font-size:var(--fs-sm);background:#fff;color:var(--text);width:100%;font-weight:500;transition:all var(--t-fast)}
.field input:focus{outline:none;border-color:var(--primary-700);box-shadow:0 0 0 2px rgba(59,74,42,.08)}
.field input.error{border-color:var(--accent-red);box-shadow:0 0 0 2px rgba(176,74,62,.08)}
.field .hint{font-size:11px;color:var(--muted);margin-top:6px}
.field .field-err{font-size:11px;color:var(--accent-red);font-weight:600;margin-top:6px;display:none}
.field.has-error .field-err{display:block}

.pw-wrap{position:relative}
.pw-wrap input{padding-right:42px}
.pw-toggle{position:absolute;top:50%;right:10px;transform:translateY(-50%);width:30px;height:30px;border-radius:var(--r-sm);color:var(--muted);display:inline-flex;align-items:center;justify-content:center;transition:color var(--t-fast)}
.pw-toggle:hover{color:var(--primary-700);background:var(--bg-soft)}

.phone-group{display:flex;align-items:stretch;border:1px solid var(--border);border-radius:var(--r-sm);overflow:hidden;background:#fff;transition:all var(--t-fast)}
.phone-group:focus-within{border-color:var(--primary-700);box-shadow:0 0 0 2px rgba(59,74,42,.08)}
.phone-group .prefix{padding:13px 14px;background:var(--bg-soft);color:var(--text-2);font-weight:700;font-size:var(--fs-sm);border-right:1px solid var(--border);display:inline-flex;align-items:center;flex-shrink:0}
.phone-group input{border:0!important;box-shadow:none!important;border-radius:0!important;flex:1}

.pw-strength{display:flex;gap:4px;margin-top:8px;height:4px}
.pw-strength span{flex:1;background:var(--border);border-radius:var(--r-pill);transition:background var(--t-fast)}
.pw-strength.weak span:nth-child(1){background:var(--accent-red)}
.pw-strength.medium span:nth-child(-n+2){background:var(--accent-gold)}
.pw-strength.strong span{background:var(--accent-success)}
.pw-strength-label{font-size:11px;margin-top:6px;font-weight:700;letter-spacing:.04em;text-transform:uppercase}
.pw-strength-label.weak{color:var(--accent-red)}
.pw-strength-label.medium{color:var(--accent-gold)}
.pw-strength-label.strong{color:var(--accent-success)}
.match-msg{font-size:11px;margin-top:6px;font-weight:600;display:block}
.match-msg.ok{color:var(--accent-success)}
.match-msg.err{color:var(--accent-red)}

.check-row{display:flex;align-items:flex-start;gap:8px;font-size:var(--fs-sm);color:var(--text-2);margin:var(--s-3) 0;cursor:pointer;line-height:1.5}
.check-row input{width:16px;height:16px;accent-color:var(--primary-700);flex-shrink:0;margin-top:3px}
.check-row a{color:var(--primary-700);font-weight:700;text-decoration:underline}

.btn-submit{width:100%;padding:14px;border-radius:var(--r-sm);background:var(--primary-700);color:#fff;font-weight:700;font-size:var(--fs-sm);letter-spacing:.04em;text-transform:uppercase;display:inline-flex;align-items:center;justify-content:center;gap:var(--s-2);cursor:pointer;border:0;margin-top:var(--s-4);transition:all var(--t-fast)}
.btn-submit:hover:not(:disabled){background:var(--primary-900)}
.btn-submit:disabled{background:var(--muted-2);cursor:not-allowed;opacity:.7}
.btn-submit.loading{pointer-events:none}
.btn-submit.loading::before{content:"";width:14px;height:14px;border:2px solid #fff;border-right-color:transparent;border-radius:50%;animation:spin .7s linear infinite;margin-right:6px}
@keyframes spin{to{transform:rotate(360deg)}}

.row-between{display:flex;justify-content:space-between;align-items:center;margin:var(--s-2) 0 var(--s-4);flex-wrap:wrap;gap:8px}
.row-between .check-row{margin:0;font-size:var(--fs-sm)}
.row-between .forgot{font-size:var(--fs-sm);font-weight:700;color:var(--primary-700)}
.row-between .forgot:hover{color:var(--primary-900);text-decoration:underline}

.divider-or{display:flex;align-items:center;gap:var(--s-3);margin:var(--s-6) 0;color:var(--muted);font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase}
.divider-or::before,.divider-or::after{content:"";flex:1;height:1px;background:var(--border)}

.social-row{display:grid;grid-template-columns:1fr 1fr;gap:var(--s-3)}
.social-btn{padding:12px;border:1px solid var(--border);border-radius:var(--r-sm);background:#fff;color:var(--text-2);font-weight:600;font-size:var(--fs-sm);display:inline-flex;align-items:center;justify-content:center;gap:8px;cursor:not-allowed;opacity:.7;position:relative;transition:all var(--t-fast)}
.social-btn:hover{border-color:var(--muted-2)}
.social-btn .soon{position:absolute;top:-8px;right:-6px;background:var(--accent-gold);color:var(--primary-900);font-size:9px;font-weight:700;padding:2px 6px;border-radius:var(--r-pill);text-transform:uppercase;letter-spacing:.04em}
.social-btn i{font-size:16px}

.auth-switch{text-align:center;margin-top:var(--s-6);padding-top:var(--s-6);border-top:1px solid var(--border);font-size:var(--fs-sm);color:var(--text-2)}
.auth-switch a{color:var(--primary-700);font-weight:700;margin-left:6px}
.auth-switch a:hover{text-decoration:underline}

.kvkk-note{margin-top:var(--s-4);font-size:11px;color:var(--muted);text-align:center;line-height:1.5}
.kvkk-note a{color:var(--primary-700);text-decoration:underline}

.success-state{text-align:center;padding:var(--s-6) 0}
.success-state .check-icon{width:72px;height:72px;border-radius:50%;background:#E8F0DC;color:var(--accent-success);display:inline-flex;align-items:center;justify-content:center;font-size:32px;margin-bottom:var(--s-5)}
.success-state h2{font-size:var(--fs-xl);font-weight:700;margin-bottom:var(--s-3)}
.success-state p{color:var(--text-2);font-size:var(--fs-sm);margin-bottom:var(--s-5)}
.cooldown{font-size:var(--fs-sm);color:var(--muted);margin-top:var(--s-3)}
.cooldown b{color:var(--primary-700)}

/* FOOTER */
.footer{background:var(--bg-section);padding:var(--s-12) 0 var(--s-6);margin-top:auto}
.footer-cols{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:var(--s-8);padding-bottom:var(--s-10);border-bottom:1px solid var(--border)}
.footer h4{font-size:var(--fs-sm);font-weight:800;letter-spacing:.05em;text-transform:uppercase;margin-bottom:var(--s-4)}
.footer ul li{padding:6px 0}
.footer ul li a{color:var(--text-2);font-size:var(--fs-sm)}
.footer-brand p{color:var(--muted);font-size:var(--fs-sm);margin-top:var(--s-3);max-width:300px}
.footer-bottom{padding-top:var(--s-5);display:flex;justify-content:space-between;align-items:center;font-size:var(--fs-xs);color:var(--muted);flex-wrap:wrap;gap:var(--s-4)}
.socials{display:flex;gap:var(--s-3);margin-top:var(--s-4)}
.socials a{width:38px;height:38px;border-radius:50%;background:var(--bg);display:flex;align-items:center;justify-content:center;color:var(--text-2);transition:all var(--t-fast)}
.socials a:hover{background:var(--primary-700);color:#fff}
.policies{display:flex;gap:var(--s-4);flex-wrap:wrap}
.contact-line{display:flex;align-items:center;gap:var(--s-2);color:var(--text-2);font-size:var(--fs-sm);padding:6px 0}
.contact-line i{color:var(--primary-700);width:16px}
@media(max-width:768px){
  .footer-cols{grid-template-columns:1fr;gap:var(--s-6)}
  .field-row{grid-template-columns:1fr}
  .auth-card{padding:var(--s-6)}
}

/* TOAST */
.toast-stack{position:fixed;bottom:24px;left:50%;transform:translateX(-50%);z-index:200;display:flex;flex-direction:column;gap:10px;pointer-events:none}
.toast{background:var(--primary-900);color:#fff;padding:12px 20px;border-radius:var(--r-md);font-size:var(--fs-sm);font-weight:600;box-shadow:0 8px 24px rgba(0,0,0,.25);display:flex;align-items:center;gap:10px;min-width:260px;animation:toastIn .25s ease;pointer-events:auto}
.toast i{color:var(--accent-gold);font-size:16px}
.toast.fade-out{animation:toastOut .3s ease forwards}
@keyframes toastIn{from{transform:translateY(20px);opacity:0}to{transform:translateY(0);opacity:1}}
@keyframes toastOut{to{transform:translateY(20px);opacity:0}}
"""

FULL_HEADER = '''
<!-- TOP RIBBON 3-col -->
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
      <a href="magaza.html">Zeytinyağları</a>
      <a href="#zeytinler">Zeytinler</a>
      <a href="#sabunlar">Sabunlar</a>
      <a href="#dogal">Doğal Ürünler</a>
      <a href="#hediye">Hediye Setleri</a>
    </nav>
    <div class="header-actions">
      <a href="magaza.html" class="icon-btn" aria-label="Ara"><i class="fa-solid fa-magnifying-glass"></i></a>
      <span class="user-dd-wrap">
        <a href="giris.html" class="icon-btn" aria-label="Hesabım"><i class="fa-regular fa-user"></i></a>
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

def head_block(title, breadcrumb_label):
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
{FULL_HEADER}

<div class="container">
  <nav class="crumb">
    <a href="index.html">Anasayfa</a>
    <i class="fa-solid fa-chevron-right sep"></i>
    <span class="active">{breadcrumb_label}</span>
  </nav>
</div>

<main class="auth-main">
'''

FOOTER_HTML = '''
<a href="index.html" class="continue-link"><i class="fa-solid fa-arrow-left"></i> Alışverişe devam et</a>
</main>

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
          <li><a href="hikayemiz.html">Derik\'in Hikâyesi</a></li>
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
        <a href="#">KVKK</a><a href="#">Gizlilik</a><a href="#">Mesafeli Satış</a><a href="#">Çerez Politikası</a>
      </div>
    </div>
  </div>
</footer>

<div class="toast-stack" id="toastStack" aria-live="polite"></div>
'''

# Auth-state JS for header dropdown — same pattern as _inject_auth_state.py
AUTH_STATE_JS = '''
<script>
// === AUTH HEADER STATE (v3.8.1) ===
(function(){
  const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
  const userName = localStorage.getItem('userName') || 'Hesabım';
  const userEmail = localStorage.getItem('userEmail') || '';
  const initial = (userName.trim().charAt(0) || 'H').toUpperCase();
  document.querySelectorAll('.user-dd-wrap').forEach(wrap => {
    const link = wrap.querySelector('a.icon-btn');
    const menu = wrap.querySelector('.user-dd-menu');
    if (!isLoggedIn) {
      if (link) link.setAttribute('href', 'giris.html');
      if (menu) {
        // Replace dropdown with login/register CTAs
        menu.innerHTML = `
          <a href="giris.html"><i class="fa-solid fa-arrow-right-to-bracket"></i> Giriş Yap</a>
          <a href="kayit.html"><i class="fa-solid fa-user-plus"></i> Üye Ol</a>
        `;
      }
    } else {
      if (menu && !menu.querySelector('.dd-user-head')) {
        const header = document.createElement('div');
        header.className = 'dd-user-head';
        header.innerHTML = `
          <div class="dd-avatar">${initial}</div>
          <div class="dd-info">
            <b>${userName}</b>
            ${userEmail ? `<span>${userEmail}</span>` : ''}
          </div>`;
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
  // Çıkış Yap
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
})();
</script>
'''

JS_COMMON = '''
<script>
function showToast(msg, icon){
  const stack = document.getElementById('toastStack');
  const t = document.createElement('div');
  t.className = 'toast';
  t.innerHTML = `<i class="fa-solid ${icon || 'fa-circle-check'}"></i> ${msg}`;
  stack.appendChild(t);
  setTimeout(() => { t.classList.add('fade-out'); setTimeout(() => t.remove(), 300); }, 2700);
}

document.querySelectorAll('.pw-toggle').forEach(btn => {
  btn.addEventListener('click', () => {
    const inp = btn.previousElementSibling;
    const showing = inp.type === 'text';
    inp.type = showing ? 'password' : 'text';
    btn.querySelector('i').className = showing ? 'fa-regular fa-eye' : 'fa-regular fa-eye-slash';
  });
});

function calcStrength(pw){
  let s = 0;
  if (pw.length >= 8) s++;
  if (/[A-Z]/.test(pw) && /[a-z]/.test(pw)) s++;
  if (/[0-9]/.test(pw)) s++;
  if (/[^A-Za-z0-9]/.test(pw)) s++;
  if (pw.length >= 12) s++;
  if (s <= 1) return 'weak';
  if (s <= 3) return 'medium';
  return 'strong';
}
const STRENGTH_LABEL = { weak: 'Zayıf', medium: 'Orta', strong: 'Güçlü' };
document.querySelectorAll('[data-pw-strength]').forEach(inp => {
  const target = document.querySelector(inp.dataset.pwStrength);
  if (!target) return;
  const bar = target.querySelector('.pw-strength');
  const label = target.querySelector('.pw-strength-label');
  inp.addEventListener('input', () => {
    if (!inp.value) { bar.className = 'pw-strength'; label.textContent = ''; label.className = 'pw-strength-label'; return; }
    const s = calcStrength(inp.value);
    bar.className = 'pw-strength ' + s;
    label.className = 'pw-strength-label ' + s;
    label.textContent = STRENGTH_LABEL[s];
  });
});

document.querySelectorAll('[data-pw-match]').forEach(inp => {
  const source = document.querySelector(inp.dataset.pwMatch);
  const msg = inp.parentElement.parentElement.querySelector('.match-msg');
  if (!msg) return;
  function check(){
    if (!inp.value) { msg.textContent = ''; msg.className = 'match-msg'; return; }
    if (inp.value === source.value) { msg.textContent = '✓ Şifreler eşleşiyor'; msg.className = 'match-msg ok'; }
    else { msg.textContent = '✗ Şifreler eşleşmiyor'; msg.className = 'match-msg err'; }
  }
  inp.addEventListener('input', check);
  source.addEventListener('input', check);
});

function setFieldError(inp, msg){
  const field = inp.closest('.field') || inp.parentElement;
  inp.classList.add('error');
  field.classList.add('has-error');
  let err = field.querySelector('.field-err');
  if (!err) { err = document.createElement('span'); err.className = 'field-err'; field.appendChild(err); }
  err.textContent = msg;
}
function clearFieldError(inp){
  const field = inp.closest('.field') || inp.parentElement;
  inp.classList.remove('error');
  field.classList.remove('has-error');
}

function btnLoading(btn){
  btn.dataset.orig = btn.innerHTML;
  btn.classList.add('loading');
  btn.disabled = true;
  btn.innerHTML = 'İşleniyor...';
}
function btnReset(btn){
  btn.classList.remove('loading');
  btn.disabled = false;
  btn.innerHTML = btn.dataset.orig || btn.innerHTML;
}
</script>
'''

# ============ PAGE BODIES ============
GIRIS_BODY = '''<div class="auth-card">
  <div class="auth-head">
    <h1>Hoş geldiniz</h1>
    <p class="lead">Hesabınıza giriş yapın</p>
  </div>

  <form id="loginForm" onsubmit="return false" novalidate>
    <div class="field">
      <label for="email">E-posta <span class="req">*</span></label>
      <input id="email" name="email" type="email" placeholder="ornek@mail.com" autocomplete="email">
    </div>

    <div class="field">
      <label for="pw">Şifre <span class="req">*</span></label>
      <div class="pw-wrap">
        <input id="pw" name="password" type="password" placeholder="Şifrenizi girin" autocomplete="current-password">
        <button type="button" class="pw-toggle" aria-label="Şifreyi göster"><i class="fa-regular fa-eye"></i></button>
      </div>
    </div>

    <div class="row-between">
      <label class="check-row">
        <input type="checkbox" name="remember"> Beni hatırla
      </label>
      <a href="sifremi-unuttum.html" class="forgot">Şifremi unuttum</a>
    </div>

    <button type="button" id="loginBtn" class="btn-submit"><i class="fa-solid fa-arrow-right-to-bracket"></i> Giriş Yap</button>

    <p class="kvkk-note">Giriş yaparak <a href="#">Kullanım Koşulları</a> ve <a href="#">Gizlilik Politikası</a>&apos;nı kabul etmiş olursunuz.</p>
  </form>

  <div class="divider-or">veya</div>

  <div class="social-row">
    <button type="button" class="social-btn" disabled><i class="fa-brands fa-google"></i> Google<span class="soon">Yakında</span></button>
    <button type="button" class="social-btn" disabled><i class="fa-brands fa-apple"></i> Apple<span class="soon">Yakında</span></button>
  </div>

  <div class="auth-switch">
    Üye değil misiniz?<a href="kayit.html">Hemen Üye Olun</a>
  </div>
</div>

<script>
document.getElementById('loginBtn').addEventListener('click', () => {
  const email = document.getElementById('email');
  const pw = document.getElementById('pw');
  const btn = document.getElementById('loginBtn');
  let ok = true;
  clearFieldError(email); clearFieldError(pw);
  if (!email.value.trim() || !/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email.value)) { setFieldError(email, 'Geçerli bir e-posta girin.'); ok = false; }
  if (!pw.value || pw.value.length < 6) { setFieldError(pw, 'Şifre en az 6 karakter olmalı.'); ok = false; }
  if (!ok) return;
  btnLoading(btn);
  setTimeout(() => {
    localStorage.setItem('isLoggedIn', 'true');
    localStorage.setItem('userEmail', email.value);
    if (!localStorage.getItem('userName')) {
      const local = email.value.split('@')[0];
      const name = local.charAt(0).toUpperCase() + local.slice(1);
      localStorage.setItem('userName', name);
    }
    const next = new URLSearchParams(location.search).get('next');
    location.href = next || 'uyelik-bilgilerim.html';
  }, 800);
});
</script>
'''

KAYIT_BODY = '''<div class="auth-card wide">
  <div class="auth-head">
    <h1>Hesap Oluşturun</h1>
    <p class="lead">Derik\'e hoş geldiniz, üyelik avantajlarından faydalanın</p>
  </div>

  <form id="registerForm" onsubmit="return false" novalidate>
    <div class="field-row">
      <div class="field">
        <label for="ad">Ad <span class="req">*</span></label>
        <input id="ad" name="ad" type="text">
      </div>
      <div class="field">
        <label for="soyad">Soyad <span class="req">*</span></label>
        <input id="soyad" name="soyad" type="text">
      </div>
    </div>

    <div class="field">
      <label for="email">E-posta <span class="req">*</span></label>
      <input id="email" name="email" type="email" placeholder="ornek@mail.com" autocomplete="email">
    </div>

    <div class="field">
      <label for="tel">Telefon <span class="req">*</span></label>
      <div class="phone-group">
        <span class="prefix">+90</span>
        <input id="tel" name="tel" type="tel" placeholder="(5xx) xxx xx xx" autocomplete="tel-national">
      </div>
    </div>

    <div class="field">
      <label for="pw">Şifre <span class="req">*</span></label>
      <div class="pw-wrap">
        <input id="pw" name="password" type="password" placeholder="En az 8 karakter" autocomplete="new-password" data-pw-strength="#pwStrengthBox">
        <button type="button" class="pw-toggle" aria-label="Şifreyi göster"><i class="fa-regular fa-eye"></i></button>
      </div>
      <div id="pwStrengthBox">
        <div class="pw-strength"><span></span><span></span><span></span><span></span></div>
        <div class="pw-strength-label"></div>
      </div>
    </div>

    <div class="field">
      <label for="pw2">Şifre Tekrar <span class="req">*</span></label>
      <div class="pw-wrap">
        <input id="pw2" name="password2" type="password" placeholder="Şifrenizi tekrar girin" autocomplete="new-password" data-pw-match="#pw">
        <button type="button" class="pw-toggle" aria-label="Şifreyi göster"><i class="fa-regular fa-eye"></i></button>
      </div>
      <span class="match-msg"></span>
    </div>

    <label class="check-row">
      <input type="checkbox" id="kvkk" name="kvkk">
      <span><a href="#">KVKK Aydınlatma Metni</a> ve <a href="#">Üyelik Sözleşmesi</a>&apos;ni okudum, kabul ediyorum. <span class="req">*</span></span>
    </label>
    <label class="check-row">
      <input type="checkbox" name="bulten">
      <span>Yeni ürün ve kampanyalardan e-posta ile haberdar olmak istiyorum.</span>
    </label>

    <button type="button" id="registerBtn" class="btn-submit"><i class="fa-solid fa-user-plus"></i> Üye Ol</button>
  </form>

  <div class="auth-switch">
    Zaten üye misiniz?<a href="giris.html">Giriş Yapın</a>
  </div>
</div>

<script>
document.getElementById('registerBtn').addEventListener('click', () => {
  const ad = document.getElementById('ad');
  const soyad = document.getElementById('soyad');
  const email = document.getElementById('email');
  const tel = document.getElementById('tel');
  const pw = document.getElementById('pw');
  const pw2 = document.getElementById('pw2');
  const kvkk = document.getElementById('kvkk');
  const btn = document.getElementById('registerBtn');
  let ok = true;
  [ad, soyad, email, tel, pw, pw2].forEach(clearFieldError);
  if (!ad.value.trim()) { setFieldError(ad, 'Ad zorunlu.'); ok = false; }
  if (!soyad.value.trim()) { setFieldError(soyad, 'Soyad zorunlu.'); ok = false; }
  if (!email.value.trim() || !/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email.value)) { setFieldError(email, 'Geçerli bir e-posta girin.'); ok = false; }
  if (!tel.value.trim() || tel.value.replace(/\\D/g,'').length < 10) { setFieldError(tel, 'Geçerli bir telefon girin.'); ok = false; }
  if (!pw.value || pw.value.length < 8) { setFieldError(pw, 'Şifre en az 8 karakter olmalı.'); ok = false; }
  if (pw.value !== pw2.value) { setFieldError(pw2, 'Şifreler eşleşmiyor.'); ok = false; }
  if (!kvkk.checked) { showToast('KVKK metnini onaylamanız gerekiyor.', 'fa-circle-exclamation'); ok = false; }
  if (!ok) return;
  btnLoading(btn);
  setTimeout(() => {
    const fullName = ad.value.trim() + ' ' + soyad.value.trim();
    localStorage.setItem('isLoggedIn', 'true');
    localStorage.setItem('userName', fullName);
    localStorage.setItem('userEmail', email.value.trim());
    showToast('Hoş geldiniz ' + ad.value.trim() + '!', 'fa-circle-check');
    setTimeout(() => location.href = 'uyelik-bilgilerim.html', 1500);
  }, 800);
});
</script>
'''

UNUTTUM_BODY = '''<div class="auth-card" id="forgotCard">
  <div class="auth-head">
    <h1>Şifremi Unuttum</h1>
    <p class="lead">E-posta adresinizi girin, size sıfırlama bağlantısı gönderelim.</p>
  </div>

  <form id="forgotForm" onsubmit="return false" novalidate>
    <div class="field">
      <label for="email">E-posta <span class="req">*</span></label>
      <input id="email" name="email" type="email" placeholder="ornek@mail.com" autocomplete="email">
      <span class="hint">Hesabınıza kayıtlı e-posta adresini girin.</span>
    </div>
    <button type="button" id="forgotBtn" class="btn-submit"><i class="fa-solid fa-paper-plane"></i> Sıfırlama Bağlantısı Gönder</button>
  </form>

  <div class="auth-switch">
    <a href="giris.html"><i class="fa-solid fa-arrow-left"></i> Giriş sayfasına dön</a>
  </div>
</div>

<div class="auth-card" id="successCard" style="display:none">
  <div class="success-state">
    <div class="check-icon"><i class="fa-solid fa-check"></i></div>
    <h2>Bağlantıyı gönderdik</h2>
    <p>E-posta kutunuzu kontrol edin. Spam klasörünüze de bakmayı unutmayın.</p>
    <a href="giris.html" class="btn-submit" style="text-decoration:none">Giriş Sayfasına Dön</a>
    <div class="cooldown" id="cooldownText">Tekrar göndermek için: <b><span id="cdSec">60</span></b> saniye</div>
    <button type="button" class="forgot" id="resendBtn" style="display:none;border:0;background:transparent;margin-top:var(--s-3);font-weight:700;cursor:pointer;color:var(--primary-700)">Tekrar Gönder</button>
  </div>
</div>

<script>
document.getElementById('forgotBtn').addEventListener('click', () => {
  const email = document.getElementById('email');
  const btn = document.getElementById('forgotBtn');
  clearFieldError(email);
  if (!email.value.trim() || !/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email.value)) {
    setFieldError(email, 'Geçerli bir e-posta girin.'); return;
  }
  btnLoading(btn);
  setTimeout(() => {
    document.getElementById('forgotCard').style.display = 'none';
    document.getElementById('successCard').style.display = 'block';
    let s = 60;
    const tick = setInterval(() => {
      s--;
      document.getElementById('cdSec').textContent = s;
      if (s <= 0) {
        clearInterval(tick);
        document.getElementById('cooldownText').style.display = 'none';
        document.getElementById('resendBtn').style.display = 'inline-block';
      }
    }, 1000);
  }, 700);
});
document.getElementById('resendBtn').addEventListener('click', () => location.reload());
</script>
'''

SIFIRLA_BODY = '''<div class="auth-card" id="resetCard">
  <div class="auth-head">
    <h1>Yeni Şifre Belirle</h1>
    <p class="lead">Hesabınız için güçlü bir şifre seçin.</p>
  </div>

  <form id="resetForm" onsubmit="return false" novalidate>
    <div class="field">
      <label for="pw">Yeni Şifre <span class="req">*</span></label>
      <div class="pw-wrap">
        <input id="pw" name="password" type="password" placeholder="En az 8 karakter" autocomplete="new-password" data-pw-strength="#pwStrengthBox">
        <button type="button" class="pw-toggle" aria-label="Şifreyi göster"><i class="fa-regular fa-eye"></i></button>
      </div>
      <div id="pwStrengthBox">
        <div class="pw-strength"><span></span><span></span><span></span><span></span></div>
        <div class="pw-strength-label"></div>
      </div>
    </div>

    <div class="field">
      <label for="pw2">Yeni Şifre Tekrar <span class="req">*</span></label>
      <div class="pw-wrap">
        <input id="pw2" name="password2" type="password" placeholder="Şifrenizi tekrar girin" autocomplete="new-password" data-pw-match="#pw">
        <button type="button" class="pw-toggle" aria-label="Şifreyi göster"><i class="fa-regular fa-eye"></i></button>
      </div>
      <span class="match-msg"></span>
    </div>

    <button type="button" id="resetBtn" class="btn-submit"><i class="fa-solid fa-lock"></i> Şifreyi Güncelle</button>
  </form>
</div>

<div class="auth-card" id="successCard" style="display:none">
  <div class="success-state">
    <div class="check-icon"><i class="fa-solid fa-check"></i></div>
    <h2>Şifreniz güncellendi</h2>
    <p>Yeni şifrenizle giriş yapabilirsiniz.</p>
    <a href="giris.html" class="btn-submit" style="text-decoration:none">Giriş Sayfasına Dön</a>
  </div>
</div>

<script>
document.getElementById('resetBtn').addEventListener('click', () => {
  const pw = document.getElementById('pw');
  const pw2 = document.getElementById('pw2');
  const btn = document.getElementById('resetBtn');
  clearFieldError(pw); clearFieldError(pw2);
  let ok = true;
  if (!pw.value || pw.value.length < 8) { setFieldError(pw, 'Şifre en az 8 karakter olmalı.'); ok = false; }
  if (calcStrength(pw.value) === 'weak') { setFieldError(pw, 'Şifre çok zayıf. Büyük harf, sayı ve sembol ekleyin.'); ok = false; }
  if (pw.value !== pw2.value) { setFieldError(pw2, 'Şifreler eşleşmiyor.'); ok = false; }
  if (!ok) return;
  btnLoading(btn);
  setTimeout(() => {
    document.getElementById('resetCard').style.display = 'none';
    document.getElementById('successCard').style.display = 'block';
  }, 700);
});
</script>
'''

PAGES = [
    ('giris.html', 'Giriş Yap', 'Üye Girişi', GIRIS_BODY),
    ('kayit.html', 'Üye Ol', 'Üye Ol', KAYIT_BODY),
    ('sifremi-unuttum.html', 'Şifremi Unuttum', 'Şifremi Unuttum', UNUTTUM_BODY),
    ('sifre-sifirla.html', 'Yeni Şifre Belirle', 'Şifre Sıfırla', SIFIRLA_BODY),
]

for fname, title, breadcrumb, body in PAGES:
    head = head_block(title, breadcrumb)
    html = head + body + FOOTER_HTML + AUTH_STATE_JS + JS_COMMON + '\n</body>\n</html>\n'
    (ROOT / fname).write_text(html)
    print(f'Wrote {fname}')

print('Done.')
