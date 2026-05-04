# Web Replicator — Öğrenilen Pattern'ler

## L03 — Page-header band component'i: 3 varyant + DOM hierarşi + spacing
**Kaynak:** Derik v3.12 → v3.12.1 patron geri bildirimi (centering bug + spacing bug + minimal varyant ihtiyacı).

### Kural
Site genelinde uygulanan "page-header band" (sayfa başlığı için koyu zeminli ince bant) component'i **3 varyant** gerektirir; tek bir `.page-band` class yetmez.

### Varyantlar
1. **Full** — `.page-band` (default) — h1 + açıklama + breadcrumb. Padding 56px desktop, 36px mobile.
2. **Minimal** — `.page-band--minimal` — sadece breadcrumb, h1 yok. Padding 22px desktop, 18px mobile. Listeleme/sub-page sayfalarında kullan.
3. **Compact** — `.page-band--compact` — h1 var ama altında form/checkout/cart gibi yoğun içerik var. Padding 36px desktop, 28px mobile. Çıkış akışı (sepet, ödeme, başarılı/başarısız) için.

### DOM Hierarşisi (KRİTİK)
Bant **MAİN GRID'İN DIŞINDA**, full-width KARDEŞ element olmalı:
```
<header>...</header>
<section class="page-band"> ← body veya main'in direct child'ı
  <div class="container">
    <nav class="crumb">...</nav>
    <h1>Başlık</h1>
    <p class="lead">Açıklama</p>
  </div>
</section>
<section class="page-content"> ← AYRI kardeş, içinde sidebar+main grid
  ...
</section>
```

Bant `account-layout` veya `shop-layout` gibi grid'in **içine** nested edilirse sidebar'ın grid track'ine sticking yapar, viewport center'a hizalanmaz.

### Container hizalama
`.page-band > .container` site genelindeki `--maxw` değişkeni ile **AYNI max-width** kullanmalı. Daha küçük (1200px vs 1320px gibi) verirseniz altındaki content'ten dar kalır → optik olarak ortalanmamış görünür.

```css
.page-band > .container{max-width:var(--maxw);margin:0 auto;padding:0 var(--s-8);text-align:center}
```

### Bant ↔ sonraki content spacing
Bant ile sonraki section/container arasında **clamp(40px, 5vw, 64px)** padding-top zorunlu. Aksi halde "yapışık" görünür. Mobile'de clamp(28px, 5vw, 40px).

```css
.page-band + *,.page-band + .container{padding-top:clamp(40px,5vw,64px)}
```

### Varyant kararı (otomatik mi manuel mi?)
- **Manuel modifier class** (önerilen) — `.page-band--minimal`, `.page-band--compact` — explicit, predictable.
- `:has(h1)` selector ile otomatik mümkün ama Safari < 15.4 desteklemez ve yanlış pozitif riski var (h1'i sonradan eklerseniz padding değişir, beklenmedik).

### Yanlış pattern (kaçınılacak)
- Bant'ı `.account-layout` veya `.shop-layout` grid'in içine koymak — sidebar grid track'ine takılır.
- Bant container'ına `max-width:1200px` gibi sayfanın `--maxw`'inden farklı sabit değer vermek — alt içerikle hizasız.
- Bant'a `margin-bottom` koymak yerine sonraki section'a `padding-top` vermek daha güvenli (margin-collapse riskini önler).
- Tüm sayfalara aynı padding (48px) ile uygulamak — checkout/cart sayfalarında gereksiz dikey alan tüketir.

### Test kriteri
1. KVKK/iletisim/magaza/hakkimizda gibi 5 farklı A sayfasında: bant'ın H1'i ve breadcrumb'ı viewport horizontal center'da mı (DevTools'la `getBoundingClientRect().left` ile sol/sağ marj eşit olmalı).
2. Bant + sonraki section arasında ≥40px boşluk var mı.
3. Listeleme sayfasında (sadece crumb) bant <30px mi (minimal varyant).
4. Mobile (375px width) bant padding'i ≤36px mi.

## L02 — Component port: CSS property diff TEK BAŞINA yetersiz, visual diff zorunlu
**Kaynak:** Derik v3.11.5 → v3.11.7 patron geri bildirimi (modal sync, "FATURA TÜRÜ" centered+highlighted bug).

### Kural
Bir komponenti (modal, kart, form, hero, header) sayfa A'dan sayfa B'ye **birebir aynı** yapma görevlerinde, **CSS property-by-property diff TEK BAŞINA yetersizdir**. Mutlaka **visual/screenshot diff** de yapılmalı.

### Neden
Property diff iki sayfadaki **scoped selector**'ları karşılaştırır (örn. `.modal-backdrop .section-divider`). Ama render farkı şu kaynaklardan da gelebilir ve property diff bunları **kaçırır**:

1. **Base rule sızması** — A sayfasında `.section-divider{display:flex;justify-content:center;height:64px}` non-modal contextte tanımlı; modal-scoped override sadece font/color ekliyor → layout property'leri (flex, center, height, background) modal'a sızıyor. B sayfasında o base rule HİÇ yok, dolayısıyla diff "her iki tarafta da modal-scoped rule aynı" diyerek temiz raporluyor.
2. **`:target` / URL hash anchor states** — element ID'si URL hash'iyle eşleşince `:target` highlight tetiklenir; diff bunu pasif görmez.
3. **`:hover`, `:focus-within`, `:checked` pseudo-classes** — statik diff'te görünmez, etkileşimde fark yapar.
4. **`::before` / `::after` pseudo-elements** — global CSS reset/normalize'dan miras gelebilir, scoped diff atlar.
5. **Inherited properties** — body veya container'dan miras gelen `text-align`, `direction`, `font-family`.
6. **Cascade specificity sırası** — aynı property birden fazla rule'da, hangi sırada yüklendiğine bağlı olarak winner farklı olabilir.

### Implementation (port checklist)
1. **CSS property diff** (klasik) — scoped selector property'lerini karşılaştır.
2. **Base rule audit** — port edilen sayfada port edilmemiş element class'larının (örn. `.section-divider`) **base** kuralı var mı? Modal-scoped override bu base'i layout düzeyinde reset ediyor mu (`display`, `height`, `background`, `position`, `text-align`)?
3. **Visual diff** — Playwright `browser_take_screenshot` ile iki sayfa modal'ı yan-yana, veya browser DevTools'la elementi inspect edip **computed style** karşılaştırması (sadece declared değil).
4. **Pseudo-class/element scan** — `:target`, `:hover`, `:focus`, `:checked`, `::before`, `::after` rule'ları her iki sayfada eşleşiyor mu?
5. **Cascade test** — aynı sınıfı taşıyan başka element var mı, hangi rule önce yüklendi?

### Yanlış pattern (kaçınılacak)
- Sadece "modal CSS bloğunu" karşılaştırıp tamam demek — class adlarının paylaşıldığı global rule'lar atlanır.
- "Class isimleri aynı, property'ler aynı, demek ki aynı görünüyor" varsayımı — base rule sızması bu varsayımı bozar.
- Modal-scoped override yazarken sadece visual property eklemek (font, color, border) — layout property'leri (`display`, `position`, `height`, `text-align`, `background`) **explicit reset** edilmezse base rule sızar.

### Test kriteri
1. Port edilen modal'ı her iki sayfada açıp screenshot al → pixel-level karşılaştır.
2. Modal içindeki TÜM elementleri DevTools'da inspect, "Computed" tab'de değerleri karşılaştır (declared değil, computed).
3. Modal içindeki her class için iki sayfada da `document.querySelectorAll('.classname').forEach(el => console.log(getComputedStyle(el)))` çalıştırıp diff al.

---

## L01 — Banka kartı şema logoları (Visa / Mastercard / Troy / Amex)
**Kaynak:** Derik v3.11.4 → v3.11.6 patron geri bildirimleri (iki iter).

### Kural
Kredi/banka kartı görselinde şema logoları **UPPER-RIGHT corner**'da, **chip'in karşı köşesinde** durmalıdır. **LOWER-RIGHT pattern'inden kaçınılır** — kartın alt satırı zaten kart sahibi adı + son kullanma tarihi taşır; logo o satıra konursa **çakışma kaçınılmazdır**. Hangi şema render edilirse edilsin (Visa wordmark, Mastercard daireler, Troy lowercase, Amex blok) görsel kutu üst-sağ köşede sabit kalır.

### Neden
- **Visa Brand Standards §4.2** — wordmark upper-right, chip-opposite quadrant.
- **Mastercard Brand Mark Guidelines §3.1** — symbol mark upper-right, minimum 1/8 card-width margin.
- **Türkiye banka kartları:** Garanti BBVA, İş Bankası Maximum, Akbank Axess, Yapı Kredi World — tüm scheme logoları **üst-sağda**. Lower-right boş bırakılır veya bank logosuna ayrılır.
- **Çakışma riski:** Lower-right'a konan logo `padding-right` hack'iyle iki block'u (cardholder + expiry) sıkıştırmaya zorlar; uzun isimlerde overflow / "GEÇERLİLİK" label'ı ile binme yapar.

### Implementation
1. **Şema container'ı `.cc-top` flex satırına yerleştir** — chip-row solda, scheme sağda, `justify-content:space-between` ile otomatik ayrışır.
2. **`.cc-bottom` sadece 2 kolon** taşır: `grid-template-columns:1fr auto` (sol = cardholder, sağ = expiry). Padding hack YOK.
3. **`.cc-exp` text-align:right** ile expiry değeri sağ kenara yapışır.
4. **`.cc-field span`** uzun isimleri `overflow:hidden;text-overflow:ellipsis;white-space:nowrap` ile keser — taşma riski kalmaz.
5. **Tüm SVG şemaları aynı viewBox yüksekliğinde** üretilmeli (örn. `viewBox="0 0 W 32"`) — height farklılığı dikey kayma yapar.
6. **Wordmark SVG'leri sağ-yaslı render** etmeli: `<text x="W" y="..." text-anchor="end">`.
7. JS yalnızca `innerHTML` swap yapar — container box koordinatları/boyutu **asla** değişmez.

### Yanlış pattern (kaçınılacak)
- **Lower-right absolute positioning** (`right:24px;bottom:22px`) + parent grid'e `padding-right:80px` hack — cardholder/expiry sıkışır, çakışır. Bu pattern v3.11.4'te uygulandı, v3.11.6'da kaldırıldı.
- Şemayı `.cc-bottom` grid'in 3. kolonuna koymak — wordmark'lar sola hizalı kalır, daire SVG'si grid hücresinin ortasında oturur, alignment tutarsız olur.
- SVG viewBox'larında farklı yükseklik (28 vs 40 vs 32) — render boyutu eşit olsa da baseline kayar.

### Test kriteri
1. Kart numarasına `4111...` gir → VISA wordmark **üst-sağ köşede**, chip ile aynı yatay hizada.
2. `5555...` gir → Mastercard daireleri aynı kutuda, kayma yok.
3. `9792...` gir → Troy lowercase aynı kutuda.
4. Cardholder alanına 25 karakterli ad yaz → ellipsis ile kesilir, expiry'ye taşmaz.
5. Expiry "12/29" → kartın alt-sağ kenarına yapışık, üstündeki "GEÇERLİLİK" label'ı sağa hizalı.
