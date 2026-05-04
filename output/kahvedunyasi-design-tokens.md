# Kahve Dünyası — Design Tokens

Kaynak: `https://www.kahvedunyasi.com/` HTML + 9 CSS bundle (Next.js).

## Renk paleti

### Primary (sürpriz: koyu teal, kahve değil)
- `#005e5b` — **primary-700** — buton, link, vurgu
- `#004947` — primary-900 — koyu vurgu, hover
- `#438c8a` — primary-800 — orta ton
- `#edf4f9` — primary-200 — soft bg
- `#ebfffe` — primary-100 — en açık bg

### Nötr
- `#ffffff` — page bg
- `#fafafa` / `#f6f6f6` / `#f4f4f4` — section bg, card bg
- `#000000` — primary text, heading
- `#363636` — secondary text
- `#888888` / `#949494` / `#afafaf` — muted

### Accent
- `#fff46d` / `#fffac4` / `#fffde0` — gold/sarı banner (free shipping bar)
- `#ff2d55` — sale red
- `#f1c40f` — gold ikinci ton

## Tipografi
- Stack: `gothamFont, gothamFont Fallback, system-ui, Arial, sans-serif`
- Heading: weight 700, body: 400/500
- Scale (frequency-based):
  - 14px (en yaygın — body)
  - 16px (alt body)
  - 12px (caption, badge)
  - 18px (subtitle)
  - 20/22/24px (section title)
  - 28/32/36px (hero, page heading)
  - 60px (mega hero)

## Spacing scale
4 / 8 / 12 / 16 / 20 / 24 / 32 / 40 / 48 / 64

## Border-radius
- `10px` — card, button (en yaygın)
- `12px` / `15px` — banner
- `20px` — büyük card, image wrapper
- `100px` / `500px` — pill button
- `50%` — avatar, dot

## Shadow
- Hafif: `0 2px 8px rgba(0,0,0,0.06)` — card
- Orta: `0 4px 16px rgba(0,0,0,0.08)` — hover lift
- Sticky header: `0 1px 4px rgba(0,0,0,0.04)`

## Breakpoints
- mobile ≤ 480
- tablet ≤ 768
- desktop ≤ 1280
- wide ≥ 1440

## Animasyon / transition
- `transition: all .2s ease` (button, link)
- `transition: transform .3s ease` (hover scale 1.05 image)
- Toast: bounce in/out, slide in/out, flip
- Swiper: preloader spin
- Custom fade: 600ms ease-out (scroll reveal pattern)

## Component envanteri
1. **Top bar** — sarı (#fff46d) "1250 TL VE ÜZERİ KARGO BEDAVA"
2. **Sub-top bar** — language/phone, ince satır
3. **Header** — sticky white, h≈80, logo sol + nav merkez + arama + ikon (hesap, sepet) sağ
   - Nav: HEDİYE GÖNDER • KAHVE • ÇİKOLATA • AKSESUAR • PASTACILIK • REFORM
4. **Hero slider** — full-width, h≈480-560, 3 slide, dot navigation
5. **Kategoriler grid** — 4-6 kolon, kare card, üstünde resim altında label
6. **Haberler ve Fırsatlar** — 2 büyük banner yan yana
7. **Yeni Çıkanlar** — 4 kolon ürün card (görsel + isim + TL + Sepete Ekle)
8. **Çok Satanlar** — aynı 4 kolon
9. **Hediyelik Kutular** — 4 kolon + sol büyük banner
10. **Blog** — 2 kolon featured (resim + kategori tag + tarih + başlık)
11. **Instagram feed** — 9 kare grid
12. **App download** — merkezde "HEMEN İNDİR" + 3 store badge
13. **Footer** — 3 kolon (Kategoriler / Kurumsal / Yardım) + alt bar (copyright + sosyal + cookie)

## Aesthetic notlar
- Modern-traditional dengesi
- Geniş white space, davetkar
- Premium ama lüks değil
- Resim merkezli, tipografi destekleyici
- Yuvarlak köşeler ama soft (10-20px)
- Gölgeler ince, flat-ish
