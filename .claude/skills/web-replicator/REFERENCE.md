# web-replicator — Detaylı Referans

## Faz 1 — FETCH detayları
`scripts/fetch_site.sh` curl ile:
1. `index.html` indir (UA: Chrome)
2. HTML'den `href="..."` çıkar (CSS link'leri), her birini `css/{name}.css` olarak indir
3. Font URL'lerini sadece logla, indirme

Eğer site SPA / heavily JS-rendered (boş `<body>` döner) ise WebFetch'e fallback yap — Claude render edilmiş içeriği analiz eder.

## Faz 2 — ANALYZE heuristikleri
- **Renk frekansı**: `grep -oE '#[0-9a-fA-F]{3,8}|rgba?\([^)]+\)' *.css | sort | uniq -c | sort -rn | head -20`
- **Font scale**: `grep -oE 'font-size:\s*[0-9.]+(px|rem|em)' *.css | sort | uniq -c`
- **Spacing**: padding/margin değerlerinin frekans tablosu
- **Keyframes**: `grep -A 20 '@keyframes' *.css`
- **Components**: HTML'i Claude'a okutup component envanteri çıkart

Token dosyasının formatı:
```md
## Renk paleti
- `#5C2E1A` — primary (kahve)
- `#F5EFE6` — bg-cream
- ...

## Tipografi
- Heading: `'Playfair Display', serif` 700, scale 24/32/48/64
- Body: `'Inter', sans-serif` 400, 14/16/18

## Spacing scale
4 / 8 / 12 / 16 / 24 / 32 / 48 / 64

## Components
- Header: sticky, h=80, white bg, shadow on scroll
- Hero: full-width slider, h=560, dark overlay, white text center
- Category grid: 3 cols desktop / 2 tablet / 1 mobile, gap 24, image aspect 1:1, hover scale 1.05
- ...
```

## Faz 3 — GENERATE prompt şablonu
Claude'a verilecek görev:
> Aşağıdaki design tokens ve component envanterini kullanarak tek dosya HTML üret. CSS değişkenleri ile tokens, semantic HTML, Türkçe içerik, BRAND-SLOT yorumları, placeholder SVG görseller. Header > Hero > Kategori grid > Ürün card grid > Banner > Footer iskeleti. Hover/scroll animasyonları dahil. Responsive 3 breakpoint.

## Faz 4 — COMPARE
Playwright script `scripts/screenshot.mjs`:
- Argümanlar: `<orig-url> <local-html> <out-dir>`
- Her ikisi için 1440x900 ve 375x800 ekran çek → `original-desktop.png`, `template-desktop.png`, `original-mobile.png`, `template-mobile.png`
- Claude bunları Read ile alır, görsel diff yapar

Fallback (Playwright yok):
- WebFetch ile orijinalin layout/renk/tipografi tarifi
- Template'i Read ile görsel olmadan kavramsal kontrol
- Log'a "manuel verification için tarayıcıda aç" notu ekle

## Faz 5 — ITERATE kuralları
- Her iterasyon **fark listesi → Edit → yeniden screenshot** sırasıyla
- Log her iterasyonda append edilir, üzerine yazılmaz
- "Yeterince yakın": renk/font/spacing 3 ana noktada eşleşiyor + genel hiyerarşi tanınabilir
- En çok 3 tur, sonra zorla durur

## Marka Değiştirme Notları (her zaman log sonuna eklenir)
Format:
```md
## Marka Değiştirme Notları
Find-replace komutu:
    sed -i '' 's/BRAND/Derik/g' {slug}-template.html

BRAND-SLOT konumları:
- L42  header-logo       <span class="brand-logo">BRAND</span>
- L98  hero-title        <h1>BRAND'e Hoş Geldiniz</h1>
- L240 footer-name       <h4>BRAND</h4>
- L251 email-domain      info@BRAND.com.tr
- ...

Logo değişimi: `<span class="brand-logo">` içine SVG/img yerleştir, `font-family` ve renk korunabilir.
```

## Kısıtlamalar
- Bitmap asset indirme yok — placeholder SVG/CSS pattern
- Marka adı/logo generic
- Türkçe UI metinleri korunur
- git komutları yok (commit/push yasak)
