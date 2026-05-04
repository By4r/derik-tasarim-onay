---
name: web-replicator
description: Verilen bir web sitesinin görsel/CSS/animasyon dilini analiz edip aynısını üreten tek-dosya HTML template oluşturur ve iteratif olarak orijinale yaklaştırır. Kullanıcı şu tarz şeyler söylediğinde tetiklenir: "bu siteyi referans al", "şu URL'in tasarım dilini kopyala", "site X'i clone et", "şu siteye benzeyen bir template üret", "bu sitenin CSS/animasyonlarını çıkar", "tasarım dilini benim projeme uygula".
---

# web-replicator

Bir referans URL'inden, **kullanıma hazır tek dosya HTML template** üretir. Marka adı/logosu generic (`BRAND` literal) bırakılır, böylece sonradan find-replace ile özelleştirilebilir.

## Pipeline (5 faz)

### 1. FETCH
- Hedef dizin oluştur: `output/_fetch/{slug}/`
- `scripts/fetch_site.sh <url> <out-dir>` çalıştır:
  - Ana HTML'i `index.html` olarak kaydeder
  - `<link rel=stylesheet>` ile referanslı tüm CSS dosyalarını indirir
  - Inline `<style>` blokları HTML'in içinde zaten gelir
- WebFetch ile aynı URL'i tarayıp "above-the-fold layout, navigation, hero, grid sections, footer; renkler ve tipografiyi de tarif et" özetini çıkar

### 2. ANALYZE
İndirilen HTML+CSS'i okuyup şu tokenları çıkar; sonucu `output/{slug}-design-tokens.md` olarak yaz:
- **Renk paleti**: en sık geçen 8-10 HEX/rgb (background, text, primary, accent, border, muted)
- **Tipografi**: font-family stack'leri, font-size scale (10/12/14/16/18/24/32/48 vb.), font-weight, letter-spacing, line-height
- **Spacing scale**: padding/margin değerlerinin sıklık dağılımı (4/8/12/16/24/32/48/64 vb.)
- **Radius / shadow / gradient**: kullanılan değerlerin envanteri
- **Breakpoints**: `@media (max-width: ...)` değerleri
- **Animations**: tüm `@keyframes` adları + transition timing fonksiyonları (`cubic-bezier(...)`, `ease-out`)
- **Components**: header, mega-menu, hero/banner, kategori grid, ürün card, button variants, footer columns, vb.

### 3. GENERATE
`output/{slug}-template.html` adında **tek dosya** üret:
- `<head>` içinde tüm CSS (`<style>` bloğu); CSS variables ile design tokens
- Orijinal layout iskeleti: header (logo + nav + arama + sepet) → hero/banner → 3-6 kategori grid → ürün card grid → öne çıkan banner → footer (4 sütun + alt bar)
- Görseller: `data:image/svg+xml` placeholder veya solid background (asla orijinal asset URL'i değil)
- **Türkçe içerik korunur** (Anasayfa, Kategoriler, Ürünler, Sepetim, İletişim, vb.)
- Hover/scroll/transition animasyonları orijinaldeki gibi
- Responsive: 1440 / 768 / 375

#### Brand placeholder protokolü (zorunlu)
- HTML başında blok yorumu:
  ```html
  <!-- ============================================
       DERIK MARKA YERİ
       Aşağıdaki BRAND-SLOT yorumlarını ara.
       Tek komutla değiştir:
         sed -i '' 's/BRAND/Derik/g' {slug}-template.html
       ============================================ -->
  ```
- Marka geçen her satırın hemen üstüne tek satır yorum:
  `<!-- BRAND-SLOT: header-logo -->`, `hero-title`, `footer-name`, `meta-title`, `tagline`, `email-domain` vb.
- Marka adı her zaman tek-kelime, case-sensitive `BRAND` literal'i olarak yazılır
- Logo yeri: `<span class="brand-logo">BRAND</span>` (img değil)
- Tagline: `<!-- BRAND-SLOT: tagline --> BRAND tagline buraya`

### 4. COMPARE
- `scripts/screenshot.mjs <orig-url> <local-html-path> <out-dir>` çalıştırmayı dene (Playwright + chromium)
- Playwright kurulu değilse → `npx playwright install chromium` deneyip 60s timeout'la
- Başarısızsa fallback: WebFetch ile orijinalin görsel tarifini al, template'i Read ile incele, kavramsal fark listesi çıkar
- Karşılaştırma çıktısı: somut fark listesi (renk yanlış, spacing dar, hiyerarşi ters, hover yok, vb.)

### 5. ITERATE
- En fazla 3 iterasyon
- Her iterasyonda fark listesini template'e Edit ile yansıt
- `output/{slug}-iteration-log.md` dosyasını her iterasyonda güncelle (ne değişti, neden, ne kadar yaklaştık)
- Yeterli yakınlık: ≤3 önemli fark veya 3. tur sonu
- **Son iterasyon sonunda log'a "Marka Değiştirme Notları" bölümü ekle**: tüm `BRAND-SLOT:*` satır numaraları + bağlam, önerilen sed komutu, logo değiştirme talimatı

## Çıktılar
- `output/{slug}-template.html`
- `output/{slug}-design-tokens.md`
- `output/{slug}-iteration-log.md`

## Detay için
Token çıkarma heuristikleri, prompt şablonları ve "yeterince yakın" kriterleri için `REFERENCE.md`'ye bak.
