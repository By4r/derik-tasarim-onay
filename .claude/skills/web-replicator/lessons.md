# Web Replicator — Öğrenilen Pattern'ler

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
