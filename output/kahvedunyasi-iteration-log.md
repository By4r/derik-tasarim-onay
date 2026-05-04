# Kahve Dünyası Template — İterasyon Logu

## Faz 1 — FETCH
- `https://www.kahvedunyasi.com/` → `index.html` (469 KB) + 9 CSS bundle
- Toplam ~560 KB CSS taranabildi (Next.js, gothamFont)
- Fontlar log'landı, indirilmedi

## Faz 2 — ANALYZE
- Frekans tabanlı renk/font/spacing/radius çıkarımı yapıldı (`kahvedunyasi-design-tokens.md`)
- **Sürpriz bulgu**: WebFetch'in görsel tahmini "kahve kahverengisi primary" derken, CSS source-of-truth `#005e5b` (deep teal) dedi. Inline HTML'de `background-color:#005e5b` + `color:#ffffff` doğrulandı. CSS'e güvenildi.

## Faz 3 — GENERATE (v0)
- Tek dosya `kahvedunyasi-template.html` üretildi
- Layout: topbar → subtop → header → hero → 6-col kategori → 2 banner → yeni çıkanlar → çok satanlar → hediyelik → blog → instagram → app download → 4-col footer
- Placeholder pattern (CSS gradient) — bitmap asset yok
- Türkçe içerik korundu (UI metni, kategori isimleri, kampanya cümleleri)
- Tüm marka geçişleri `BRAND` literal + `<!-- BRAND-SLOT: ... -->` yorumlu

## Faz 4 — COMPARE (fallback)
- `npx playwright install chromium` denendi → kurulum başarısız (sandbox/network)
- Playwright atlanmış; karşılaştırma WebFetch görsel-tarif + Read kavramsal kontrol
- Tespit edilen farklar:
  1. Hero çok karanlık/dramatik (#2d1810 gradient) — orijinal aslında parlak ürün/cream tonları
  2. Eyebrow chip blur'lu cam efekti yerine düz primary teal olmalı
  3. CTA hero butonu: kontrast için solid primary teal istenir, beyaz değil
  4. Hero dots beyaz idi → açık zeminde görünmüyor, primary teal yapıldı
  5. Section header'larda görsel kimlik için altta küçük accent çizgi yok
  6. Product card içi "kahve kart bg" idi → orijinal ürünleri beyaz arka plan üzerinde gösteriyor

## Faz 5 — ITERATE

### İterasyon 1 — Hero & CTA tone (uygulandı)
- Hero gradient: `cream → caramel → tan` (radial teal vurgu)
- Hero text rengi: koyu cocoa (`#2d1810`)
- Eyebrow: solid teal pill
- `.btn-primary`: artık teal-üzerine-beyaz (orijinal CTA stiline uygun)
- Hero dots: teal active state
- **Sonuç**: hero hissi orijinaldekine benzer ürün-merkezli, davetkâr tona kaydı

### İterasyon 2 — Card & section polish (uygulandı)
- `.section-head h2::after` ile 40px×3px primary-teal accent çizgisi eklendi
- Product `.img-wrap` arka planı `#fff` + alt 1px border (orijinal beyaz ürün fotoğrafı hissi)
- **Sonuç**: ürün grid'i daha temiz/profesyonel; section başlıkları görsel hiyerarşi kazandı

### İterasyon 3 — Hero billboard + 2-col, container width, typography (uygulandı)
- Hero artık `min-height: 70vh` (gerçek "billboard" hissi)
- Hero içeriği 2-sütunlu: SOL `.hero-text` (eyebrow + h1 + p + CTA), SAĞ `.hero-visual` (16:9 desenli placeholder)
- Hero başlığı `letter-spacing: -0.025em` (daha tighter)
- Container max-width 1280 → 1320, yatay padding 24 → 32 (tablet 24, mobil 16)
- Body `font-size`: 14 → 16, `line-height` 1.5 → 1.6 (daha ferah)
- `h1-h4` global `letter-spacing: -0.015em`
- Section padding 64 → 96 (tablet 56), section başlık 32 → 36px
- Hero dot 4 nokta (KD'de 4 slide var)

### İterasyon 4 — Kategori, ürün ve banner zenginleştirme (uygulandı)
- **Kategori kartları**: aspect-ratio kaldırıldı → fixed `height: 240px` (mobil 180px). İsim alt-orta köşede beyaz pill içinde. Hover: kart kalkar, görsel parlar (filter brightness), pill primary teal'a döner. Üstte altta soft gradient overlay.
- **Ürün kartları**: img-wrap arka planı `#FAF9F5` krem (önceden #fff). Hover: -4px translate + shadow-2 + ürün scale 1.03. 5 yıldız (gold) + parantezli yorum sayısı eklendi (her 11 kart için).
- **Badge**: kırmızı + sol köşe; renk artık `--primary-900` koyu zemin + `#FAF6EE` krem yazı (pembe yerine brand-uyumlu). Pill şekli, "ÇOK SATAN" / "YENİ" / "İNDİRİM" varyantları.
- **Add-to-cart**: padding 10 → 12, hover translateY -1px (hafif kalkış).
- **Banner kartlar**: dikey gradient teal zemin + üstüne `.ph-banner` desenli "Banner Görseli" placeholder. Eyebrow chip'i + büyük başlık + beyaz CTA pill. Hover: kart kalkar + içerik parlar + CTA sağa kayar.
- **Section başlık**: 32 → 36px, weight 800 → 700 (KD'deki gibi karakterli ama dramatik değil), accent çizgi korundu.

### Yeterlilik
4. iterasyondan sonra kalan farklar sadece "gerçek görseller yok" — kasıtlı. Kalan farklar:
- Tipografi: orijinal "gothamFont" lisanslı; template Inter/system fallback kullanıyor (görsel olarak çok yakın, license-safe)
- Gerçek ürün fotoğrafları yok (placeholder pattern) — kasıtlı
- Hero'da gerçek lifestyle imajı yok (gradient) — kullanıcı kendi assetini koyacak

---

## Marka Değiştirme Notları

### Hızlı find-replace
```bash
cd "~/Design/Derik Design/output"
sed -i '' 's/BRAND/Derik/g' kahvedunyasi-template.html
# veya isim değişirse:
sed -i '' 's/BRAND/Derik Zeytinyağı/g' kahvedunyasi-template.html
```

### BRAND-SLOT konumları (satır numaraları template'in son halinde)

| Satır | Slot | İçerik |
|-------|------|--------|
| 6  | `meta-title`        | `<!-- BRAND-SLOT: meta-title -->` |
| 7  | -                   | `<title>BRAND — Anasayfa</title>` |
| 505 | `header-logo`       | `<!-- BRAND-SLOT: header-logo -->` |
| 506 | -                   | `<a href="#" class="brand-logo">BRAND</a>` |
| 532 | `hero-title`        | `<!-- BRAND-SLOT: hero-title -->` |
| 533 | -                   | `<h1>BRAND ile Hepimizin Ortak Noktası</h1>` |
| 534 | `tagline`           | `<!-- BRAND-SLOT: tagline -->` |
| 535 | -                   | `<p>BRAND tagline buraya — ...</p>` |
| 762 | `instagram-handle`  | `<!-- BRAND-SLOT: instagram-handle -->` |
| 763 | -                   | `<h2>Bizi Takip Edin · @BRAND</h2>` |
| 785 | `app-promo`         | `<!-- BRAND-SLOT: app-promo -->` |
| 786 | -                   | `<h2>BRAND Uygulamasını Hemen İndir</h2>` |
| 804 | `footer-logo`       | `<!-- BRAND-SLOT: footer-logo -->` |
| 805 | -                   | `<span class="brand-logo">BRAND</span>` |
| 806 | `footer-tagline`    | `<!-- BRAND-SLOT: footer-tagline -->` |
| 807 | -                   | `<p>BRAND — özenle hazırlanmış lezzetler...</p>` |
| 825 | `footer-about`      | `<!-- BRAND-SLOT: footer-about -->` |
| 826 | -                   | `<li><a>BRAND Hakkında</a></li>` |
| 840 | `email-domain`      | `<!-- BRAND-SLOT: email-domain -->` |
| 841 | -                   | `<li><a>info@BRAND.com.tr</a></li>` |
| 846 | `footer-copyright`  | `<!-- BRAND-SLOT: footer-copyright -->` |
| 847 | -                   | `<span>©2026 BRAND. Tüm hakları saklıdır.</span>` |

### Logo değişimi
- `<span class="brand-logo">BRAND</span>` öğesinin yerine SVG/img koy
- `.brand-logo` CSS sınıfı korunsun (header + footer'da aynı görünüm)
- Renk değiştirmek istersen: `--primary-700` CSS değişkenini değiştir, tüm tema kayar

### Tema kişiselleştirme (Derik için öneri)
Derik zeytinyağı projesinde renk paletini değiştirmek için sadece `:root`'taki birkaç değişken yeterli:
```css
--primary-700: #4a6b3a;  /* zeytin yeşili */
--primary-900: #2d4422;
--primary-100: #f0f5e8;
--accent-yellow: #f5e6a8;  /* daha doğal sarımsı */
```

### Manuel kontrol noktaları
- Tarayıcıda aç: `open "kahvedunyasi-template.html"` (macOS)
- Responsive: dev tools → 1440 / 768 / 375
- Hover: kategori kartları, ürün kartları, "Sepete Ekle" butonu, nav linkleri
- Scroll: `.reveal` öğeleri viewport'a girince fade-in
- Otomatik: hero dots her 4.5s aktif değişir
