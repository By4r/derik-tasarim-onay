# Derik Anasayfa — KD'den Dönüşüm Logu

`kahvedunyasi-template.html` → `derik-anasayfa.html`

## 1. Find-replace temeli
```bash
cp kahvedunyasi-template.html derik-anasayfa.html
sed -i '' 's/BRAND/Derik/g' derik-anasayfa.html
# Sonuç: 14 BRAND-SLOT alanı Derik'e dönüştü, ardından Derik-SLOT yorum satırları temizlendi.
```

## 2. Renk paleti dönüşümü (CSS variables)

| Token | KD (teal) | Derik (zeytin/krem/altın) |
|---|---|---|
| `--primary-700` | `#005e5b` | **`#3B4A2A`** koyu zeytin yeşili |
| `--primary-800` | `#438c8a` | **`#6B7A3F`** orta zeytin |
| `--primary-900` | `#004947` | **`#2A3520`** en koyu zeytin |
| `--primary-100` | `#ebfffe` | **`#F2EBDC`** açık krem |
| `--primary-200` | `#edf4f9` | **`#E8DFC9`** açık bej |
| `--bg` | `#ffffff` | **`#FAF6EE`** Derik krem ana zemin |
| `--bg-soft` | `#fafafa` | **`#F2EBDC`** açık krem |
| `--bg-section` | `#f6f6f6` | **`#F2EBDC`** |
| `--bg-card` | `#f4f4f4` | **`#E8DFC9`** kategori card |
| `--bg-product` | `#FAF9F5` | (korundu — krem zaten uyumlu) |
| `--text` | `#000000` | **`#2A1F14`** koyu kahve, siyaha yakın |
| `--text-2` | `#363636` | **`#4A3A2A`** |
| `--muted` | `#888888` | **`#8C7A6A`** |
| `--border` | `#ececec` | **`#E8DFC9`** açık bej |
| `--accent-yellow` | `#fff46d` (KD sarı banner) | **`#C9A55B`** Derik altın |
| `--accent-red` | `#ff2d55` | **`#B04A3E`** terra-cotta |
| `--accent-gold` | `#f1c40f` | **`#C9A55B`** Derik altın |

**Hero gradient:**
- KD: `linear-gradient(120deg, #f5efe6 0%, #ecdfca 65%, #d9c2a0 100%)`
- Derik: `linear-gradient(120deg, #FAF6EE 0%, #EDE0C8 55%, #D6C29A 100%)` (krem→bej→altın)

**Pattern tint:** placeholder + hero-visual desenlerinde KD teal `rgba(0,94,91,*)` → Derik olive `rgba(59,74,42,*)`.

## 3. İçerik dönüşümü

### Top ribbon
- KD: "1250 TL VE ÜZERİ SİPARİŞLERİNİZDE KARGO BEDAVA!"
- Derik: **"750 TL ÜZERİ KARGO ÜCRETSİZ · YENİ HASAT ÜRÜNLERİ STOKTA"**

### Header navigation
| KD | Derik |
|---|---|
| Hediye Gönder | Kurumsal Satış |
| Kahve | Zeytinyağları |
| Çikolata | Zeytinler |
| Aksesuar | Sabunlar |
| Pastacılık | Doğal Ürünler |
| Reform | Hediye Setleri |

### Hero
- Eyebrow: "Yeni Sezon" → **"Yeni Hasat 2025"**
- H1: "Derik ile Hepimizin Ortak Noktası" → **"Derik'in Kadim Zeytinlerinden Saf Lezzet"**
- p: jenerik tagline → **"Mardin Derik'in bereketli topraklarında yetişen Halhalı zeytinlerinden elde edilen özel zeytinyağları."**
- CTA: "Keşfet" → **"Ürünleri İncele"**

### Kategoriler (6 kart)
Kahve / Çikolata / Hediyelik / Aksesuar / Pastacılık / Reform → **Zeytinyağları / Zeytinler / Sabunlar / Doğal Ürünler / Hediye Setleri / Kurumsal**

### Banner (Haberler ve Fırsatlar)
- SOL: "Sonbahar Kahveleri · %15 İndirim" → **"Yeni Hasat Erken Sızma · %15 Sezon Avantajı"** (eyebrow "Yeni Hasat")
- SAĞ: "Hediye Setleri için Teklif Al" → **"Kurumsal Hediye Setleri için Teklif Al"** (eyebrow "Kurumsal")

### Yeni Çıkanlar (4 ürün)
1. Filtre Kahve Yirgacheffe 250g · 189,90 TL → **Erken Hasat Natürel Sızma 500ml · 320,00 TL**
2. El Yapımı Çikolata 18'li · 249 TL → **Soğuk Sıkım Zeytinyağı 1L · 450,00 TL**
3. Türk Kahvesi Geleneksel · 129,90 TL (s/159) → **Halhalı Yeşil Zeytin 500g · 180,00 TL** (s/210)
4. Espresso Premium 1kg · 399 TL → **Hediye Seti Premium · 850,00 TL**

### Çok Satanlar (4 ürün)
1. Hediye Kutusu Klasik · 94,90 TL → **Klasik Natürel Sızma 750ml · 390,00 TL**
2. French Press 600ml · 219 TL → **Zeytinyağlı Sabun 3'lü Set · 220,00 TL**
3. Bademli Antep Fıstıklı Çikolata · 79,90 TL → **Teneke 5L Zeytinyağı · 1.450,00 TL**
4. Manuel Kahve Değirmeni · 549 TL → **Mini Hediye Kutusu · 285,00 TL**

### Hediyelik Kutular (1 feature + 3 ürün)
- Feature: "Sevdiklerinize Özel" başlığı korundu, p ve CTA korundu
- Mini Hediye Kutusu · 94,90 → **Zeytinyağı & Sabun Seti · 385,00 TL**
- Lezzet Sandığı · 189 → **Lezzet Sandığı Premium · 650,00 TL**
- Yıldönümü Seti · 329 → **Kurumsal Sunum Kutusu · 1.250,00 TL**

### Blog (2 yazı)
- "Türk Kahvesi Pişirmenin İncelikleri" (Kahve Kültürü) → **"Halhalı Zeytininin Hikâyesi"** (Zeytin Kültürü)
- "Çikolata Tadımı Nasıl Yapılır?" (Atölye) → **"Soğuk Sıkım vs Sızma — Fark Nedir?"** (Üretim)

### Instagram
- "@Derik" → **"@derikzeytin"**

### App download
- "Derik Uygulamasını Hemen İndir" → **"Derik Mobil Uygulamasını Hemen İndir"**
- Alt metin: jenerik kampanyalar → **"Yeni hasat duyuruları, özel kampanyalar ve sürpriz indirimler."**

### Footer
- **Brand tagline**: jenerik → **"Mardin Derik'ten sofranıza."**
- **Kategoriler kolonu**: Kahve/Çikolata/Aksesuar/Pastacılık/Reform → **Zeytinyağları/Zeytinler/Sabunlar/Doğal Ürünler/Hediye Setleri**
- **Kurumsal kolonu**: Derik Hakkında/Mağazalar/Kariyer/Bayilik/Basın → **Hakkımızda/Derik'in Hikâyesi/Üretim Sürecimiz/Kurumsal Satış/İletişim**
- **Yardım kolonu**: SSS/Sipariş Takibi/İade/İletişim/info@Derik.com.tr → **SSS/Kargo ve Teslimat/İade/İletişim/info@derikzeytin.com**
- **Politikalar**: Çerez/Gizlilik/Üyelik → **KVKK/Gizlilik/Mesafeli Satış/Çerez Politikası**

## 4. Marka tonu uyarlaması
- "Kampanya" eyebrow → "Kurumsal" (banner contextine göre)
- "Sonbahar Kahveleri" → "Yeni Hasat Erken Sızma"
- "Yeni Sezon" → "Yeni Hasat 2025"
- "İndirim" → "Sezon Avantajı"
- "Sepete Ekle" **korundu** (e-ticaret standardı)

## 5. Kontrol noktaları (manuel test)

```bash
open "/Users/dadaistanbul/Design/Derik Design/output/derik-anasayfa.html"
```

- [ ] Renk paleti tutarlı: hiçbir yerde KD teal (#005e5b ailesi) kalmadı (verified: 0 occurrence)
- [ ] BRAND literali kalmadı (verified: 0)
- [ ] Eski Derik-SLOT yorumları temizlendi (verified: 0)
- [ ] KD ürün isimleri (Yirgacheffe, French Press, vs.) kalmadı (verified)
- [ ] Tüm kategori/menü/footer linkleri Derik-uygun
- [ ] Hero, kategori, ürün, banner, blog, footer Derik içerik
- [ ] Responsive 1440 / 768 / 375 (CSS aynı, kontrol gerekmez)

## 6. Korunan KD asset'leri
- Layout iskeleti, component CSS'i, animasyon (hover, scroll reveal, hero dot rotator)
- BRAND-SLOT protokolü (artık ihtiyaç yok ama referans olarak skill'de kayıtlı)
- 5 yıldız rating sistemi (sayılar Derik bağlamında uygun: 28-312 yorum)

---

# v2 Revize Notları (Yasin Bey feedback'i sonrası)

Tarih: 2026-05-04
Etkilenen dosyalar: `index.html` (kök), `magaza.html` (yeni), `urun-detay.html` (yeni), `output/derik-anasayfa.html` (mirror).
Dokunulmayan: `referans/index.html`, `output/kahvedunyasi-template.html`, `.claude/skills/web-replicator/*`.

## v2 — index.html değişiklikleri

### Eklendi
- **Font Awesome 6 Free CDN** (`cdnjs/6.5.1/css/all.min.css`) — tüm emoji ikonlar FA'a geçti
- **Top ribbon 3-sütun**: sol "Kurumsal Hediyeler" linki, orta "750 TL ÜZERİ KARGO ÜCRETSİZ" (ÜCRETSİZ altın renkte), sağ xmark kapatma butonu (JS ile gizler)
- **Telefon barı**: krem zemin, sağda headset ikonu + "0 (850) 393 7070"
- **Header dropdown linkleri**: "Kurumsal Satış ▾" + "Hakkımızda ▾" sağ üstte
- **Geniş arama**: 480px max, pill, sol içinde magnifying-glass, focus'ta primary-700 border + soft glow
- **Sepet rozeti**: altın (#C9A55B) zemin, koyu kahve metin "0", header'a takılı
- **2-row header**: row1 logo+search+actions, row2 ana menü (hairline border ile ayrı)
- **Unsplash görsel entegrasyonu**: hero, 6 kategori, 2 banner, 8 ürün için `<img data-fallback>` — yüklenmezse desenli zemin

### Kaldırıldı
- **TR/EN dil switcher** (subtop bar tamamen)
- **Hediyelik Kutular section** (gift-grid)
- **Blog section** (2 blog kartı)
- **Bizi Takip Edin · Instagram grid**
- **Derik Mobil Uygulamasını Hemen İndir** (app-download)

### Değişti
- **Ana menü**: ZEYTİNYAĞLARI · ZEYTİNLER · SABUNLAR · DOĞAL ÜRÜNLER · HEDİYE SETLERİ (Kurumsal Satış ana menüden çıktı)
- **Top ribbon zemini**: altın → primary-700 (zeytin yeşili), altın yalnızca "ÜCRETSİZ" vurgusu
- **Footer "Yardım" kolonu**: 5 → 3 link (SSS, İade ve Değişim, İletişim)
- **Footer brand kolonu**: Konum + e-posta + WhatsApp ikonlu satırlar eklendi
- **Sosyal medya**: emoji harfler → FA brand ikonları (instagram, facebook, x-twitter, youtube)
- **CTA'lar**: tüm "→" arrow yerine `<i class="fa-solid fa-arrow-right">`

### Akış (yeni)
TopRibbon → TelBar → Header (logo+search+actions / nav) → Hero → Kategoriler → Banner → Yeni Çıkanlar → Çok Satanlar → Footer

## v2 — magaza.html (yeni)
- Aynı top ribbon + telbar + header + footer (3 sayfa birebir aynı kod)
- Breadcrumb: Anasayfa › Zeytinyağları
- Page-head: H1 "Zeytinyağları" + alt metin + sağda "12 ürün · Sıralama: Önerilen ▾"
- 2-sütun layout: sol 280px sticky filtre paneli, sağ 3-col ürün grid
- Filter accordion'ları (chevron-down ile aç-kapa, sol kenar primary çizgi):
  - Kategori (4 checkbox), Hacim (5), Fiyat slider (görsel), Üretim Yöntemi (2), Stok (2)
  - "Filtreleri Temizle" altın link
- 12 ürün kartı (165-1.650 TL aralığında, badge dağılımı: 3× Yeni, 2× İndirim, 2× Çok Satan, 5× nötr)
- Pagination: ‹ 1 2 3 … › alt orta, aktif sayfa primary zemin
- Mobile (<1024px): filtre üste düşer, grid 2-col; <480px 1-col

## v2 — urun-detay.html (yeni)
- Aynı top ribbon + telbar + header + footer
- Örnek ürün: **Erken Hasat Natürel Sızma Zeytinyağı 500ml** — 320 TL (eski 380 TL, -%16 badge)
- Breadcrumb: Anasayfa › Zeytinyağları › ürün adı
- 2-sütun layout (60/40):
  - SOL: ana görsel 1:1 + 5 thumbnail (JS ile değişim)
  - SAĞ sticky: producer "Derik · Yeni Hasat 2025", H1, 5 yıldız + (124 yorum), büyük fiyat + taksit, stok ikonu (yeşil nokta), 4 hacim varyant butonu (500ml aktif), adet seçici − [1] +, "Sepete Ekle" + "Hemen Al" + favori, 4 perk kartı (truck/rotate-left/shield-halved/leaf)
- 4 tab: Açıklama (default açık), Detaylı Bilgi (8 satırlık spec table), Yorumlar (3 örnek + ad/tarih/yıldız/metin), Kargo & İade
- Benzer ürünler section (4 kart)

## Cross-link haritası
- index "Tümünü Gör" → magaza.html (her section'da)
- index ürün kartları → urun-detay.html
- magaza ürün kartları → urun-detay.html
- magaza breadcrumb "Anasayfa" → index.html
- urun-detay breadcrumb "Zeytinyağları" → magaza.html
- urun-detay "Sepete Ekle" → JS ile cart-num +1

## Kullanılan Unsplash photo ID'leri
| Slot | Photo ID |
|---|---|
| Hero | `1474979266404-7eaacbcd87c5` |
| Cat: Zeytinyağları | `1611171711791-b34b41b1ccca` |
| Cat: Zeytinler | `1593001872095-7d5b3868fb1d` |
| Cat: Sabunlar | `1600857544200-b2f666a9a2ec` |
| Cat: Doğal Ürünler | `1563636619-e9143da7973b` |
| Cat: Hediye Setleri | `1607344645866-009c320c5ab8` |
| Cat: Kurumsal | `1606471838963-d5ff6e2e2bb1` |
| Banner: Yeni Hasat | `1593001872095-7d5b3868fb1d` |
| Banner: Kurumsal | `1606471838963-d5ff6e2e2bb1` |
| Ürünler (rotation) | aynı 8 ID döner |
| Fallback | `source.unsplash.com/500x500/?olive-oil,bottle` |

Yüklenmezse `data-fallback` + `onerror` JS ile desenli zemin (`.img-fallback`) görünür.

## Kullanılan Font Awesome ikonları (özet)
- **Solid**: magnifying-glass, bag-shopping, headset, xmark, chevron-down, chevron-right, chevron-left, arrow-right, location-dot, envelope, circle, plus, minus, truck, rotate-left, shield-halved, leaf, star
- **Regular**: user, heart
- **Brands**: instagram, facebook, x-twitter, youtube, whatsapp

---

## v2.4 — hikayemiz.html (yeni sayfa, skill ile KD referansı)

Tarih: 2026-05-04
Skill kullanımı: `web-replicator` → `https://www.kahvedunyasi.com/hikayemiz`
- FETCH: HTML + 6 CSS bundle indirildi (`output/_fetch/kahvedunyasi-hikayemiz/`)
- ANALYZE: WebFetch + structural read; KD'nin 3 section (marka tanıtım / mağaza divider / global başarılar) layout'u çıkarıldı
- GENERATE + ADAPT: Derik içerik + render

### Sayfa yapısı
1. **Breadcrumb** — Anasayfa > Hakkımızda > Hikayemiz
2. **HERO** (`.story-hero`) — primary-700 zemin, 2-col, eyebrow + başlık (altın `<em>` vurgusu) + p + Unsplash görsel
3. **SECTION 1** (`.story-intro`) — merkezi lead başlık + 3 vertical pillar (numaralı: 01/02/03 altın) + en altta full-width görsel (21:9)
4. **SECTION 2** (`.divider-section`) — primary-700 zemin, 2-col, başlıkta 3 altın `<em>` vurgusu, alt paragraf, "Tüm Satış Noktaları" altın CTA, sağda 4:5 görsel
5. **SECTION 3** (`.stats-section`) — eyebrow + başlık + lead + 3-col stat-card (12+ / 50+ / 5). Kartlar: krem zemin, altın rakam (72px), hover'da -6px lift + altın border. **Harita YOK**.
6. **Footer** — diğer 3 sayfa ile aynı

### Beyaz elips kullanılmadı
KD'deki ürün kartı askısı/yarım daire dekoratif eleman bilinçli olarak alınmadı.

### Header dropdown güncellemesi
"Hakkımızda ▾" altındaki "Hikayemiz" linki 4 sayfada (`index/magaza/urun-detay/hikayemiz`) artık `hikayemiz.html`'e gidiyor.

### Yeni Unsplash görseller
- `story_hero` — 1601000937856 (zeytin/zeytinyağı kompozisyon)
- `story_grove` — 1565299585323 (zeytinlik manzara, 21:9 hero altı)
- `story_press` — 1542838132 (zeytin işleme/üretim, divider sağ visual)

### Build
`output/_build_v2.py`'ye `build_hikayemiz()` modülü eklendi, FILES sözlüğüne girdi yapıldı. Tek seferde 4 sayfa build ediliyor (`hikayemiz.html` 42 KB).

---

## v2.5 — uretim.html (yeni sayfa, skill ile KD referansı)

Tarih: 2026-05-04
Skill kullanımı: `web-replicator` → `https://www.kahvedunyasi.com/uretim`
- FETCH: HTML + 5 CSS bundle (`output/_fetch/kahvedunyasi-uretim/`)
- ANALYZE: WebFetch ile KD'nin 3 ürün kategorisi (Kahve / Çikolata / Pastacılık) layout pattern'ı çıkarıldı
- ADAPT: Derik karşılığı 3 kategori (Zeytinyağı / Zeytin / Sabun & Doğal Ürünler)

### Bilinçli sapma — KD'den ayrılan tasarım kararı
KD'nin "Kakao Çekirdeği: Çikolatanın Kalbi" / "Çikolata Tutkusu Kakao Tanesinde Başlar" gibi alt başlıklı kart stack'i Derik'te **kullanılmadı** (kullanıcı kararı: hizalama sorunu yaratıyor). Yerine sağ tarafta **akıcı 2 paragraf düz yazı** kullanıldı.

### Sayfa yapısı
1. **Breadcrumb** — Anasayfa › Hakkımızda › Üretim
2. **HERO** (`.uretim-hero`) — primary-700 zemin, ortada eyebrow + h1 + p (centered, max-w 880)
3. **SECTION 1 — Zeytinyağı** — 2-col head (sol başlık, sağ akıcı 2 paragraf) + altta 21:9 full-width görsel
4. **SECTION 2 — Zeytin** — aynı layout, `.alt` (krem zemin)
5. **SECTION 3 — Sabun & Doğal Ürünler** — aynı layout, beyaz zemin
6. Her section'ın altta border ile ayrımı, alternating bg, hover'da görsel yumuşak scale 1.02

### Header dropdown güncellemesi
"Hakkımızda ▾" altındaki "Üretim" linki 5 sayfada (`index/magaza/urun-detay/hikayemiz/uretim`) artık `uretim.html`'e gidiyor.

### Görsel reuse (önceki sayfalardan)
- Zeytinyağı section: `story_grove` (zeytinlik manzara)
- Zeytin section: `cat_zeyt`
- Sabun section: `cat_sabun`

### Build
`output/_build_v2.py`'ye `build_uretim()` modülü + `.uretim-*` CSS sınıfları eklendi. Tek seferde 5 sayfa build oluyor.

## Park Edilenler (sonraki revize için)
1. **Canlı Destek floating buton** (sağ alt köşe, FA `fa-comments`)
2. **Mega menu**: kategori hover'da 3-sütun alt menü (KD'deki gibi)
3. **Slider otomatik geçiş**: hero'da 4 slide arasında geçişli geçiş + dot ile manuel
4. **Sepet drawer**: sepet ikonu tıklayınca sağdan açılan panel
5. **Real product API**: statik veri yerine JSON/CMS bağlantısı
6. **Mobile hamburger menu**: <1024px nav görünmüyor — hamburger açılırı eklenmedi
7. **Logo SVG**: "Derik" wordmark yerine zeytin dalı + serif font logo
8. **Filtre fonksiyonelliği**: accordion'lar görsel, filtreleme çalışmıyor (sadece toggle)
9. **Yorumlar pagination + form**: detay sayfasında 3 örnek yorum statik
10. **Adet → fiyat senkronu**: detayda adet/varyant değişince fiyat güncellenmiyor

## Verification (tarayıcıda manuel test)
```bash
open "/Users/dadaistanbul/Design/Derik Design/index.html"
open "/Users/dadaistanbul/Design/Derik Design/magaza.html"
open "/Users/dadaistanbul/Design/Derik Design/urun-detay.html"
```
- Header 3 sayfada birebir aynı görünüm (logo, arama, ikonlar, ana menü)
- Top ribbon kapatma butonu (xmark) çalışıyor
- Mağazada filtre accordion'ları aç-kapa
- Detayda thumbnail tıkla → ana görsel değişir, tab geçişi, adet ± , varyant aktif değişimi
- Detayda "Sepete Ekle" → header rozeti 0 → 1
- Responsive 1440 / 768 / 375

## 7. Sonraki adımlar (önerilen)
1. **Logo**: `<span class="brand-logo">Derik</span>` yerine gerçek SVG (zeytin dalı + Derik wordmark) yerleştir
2. **Görsel asset**: hero-visual + banner + ürün img-wrap + kategori .ph yerlerine gerçek fotoğraflar
3. **Font**: gothamFont yerine Derik kimlik fontu (örn. Playfair Display heading + Inter body)
4. **İçerik genişletme**: ürün sayfası, kurumsal sayfa template'leri için aynı skill yeniden çalıştırılabilir
