# Web Replicator — Öğrenilen Pattern'ler

## L01 — Banka kartı şema logoları (Visa / Mastercard / Troy / Amex)
**Kaynak:** Derik v3.11.4 patron geri bildirimi.

### Kural
Kredi/banka kartı görselinde şema logoları **HER ZAMAN** kartın **sağ alt köşesinde sabit pozisyonda** olmalıdır. Hangi şema render edilirse edilsin (Visa wordmark, Mastercard daireler, Troy lowercase, Amex blok) görsel kutu **aynı koordinatta** kalır — yer değiştirmez.

### Neden
- **Visa Brand Standards §4.2** — wordmark, kart üzerinde sabit margin ile sağ-alt köşede.
- **Mastercard Brand Mark Guidelines §3.1** — symbol mark, fixed-margin right-bottom.
- Kullanıcı algısı: alignment kayması "ucuz/amatör" hissi verir; banka kartı pattern'i premium tutarlılık gerektirir.

### Implementation
1. **Tek bir scheme container** (`.cc-scheme`) — `position:absolute; right:24px; bottom:22px; height:32px`.
2. **Tüm SVG şemaları aynı viewBox yüksekliğinde** üretilmeli (örn. `viewBox="0 0 W 32"`) — height farklılığı dikey kayma yapar.
3. **Wordmark SVG'leri sağ-yaslı render** etmeli: `<text x="W" y="..." text-anchor="end">` — viewBox sağ kenarına glyph'i yapıştır. Aksi halde aynı container içinde "VISA" sola, "Mastercard" daireleri ortaya düşer.
4. JS yalnızca `display:none/block` veya `innerHTML` swap yapar — container box'ın koordinatları/boyutu **asla** değişmez.
5. Parent (kart yüzü) `position:relative` veya `position:absolute` olmalı — scheme container'ın positioning context'i.

### Yanlış pattern (kaçınılacak)
- Şemayı `.cc-bottom` grid'in son kolonuna koymak — wordmark'lar sola hizalı kalır, daire SVG'si grid hücresinin ortasında oturur, alignment tutarsız olur.
- SVG viewBox'larında farklı yükseklik (28 vs 40 vs 32) — render boyutu eşit olsa da baseline kayar.

### Test kriteri
3 farklı şema (4xxx, 5xxx, 9xxx ile başlayan numaralar) için kartın sağ alt köşesinden screenshot al — logoların görsel sağ kenarı 1px hassasiyetle aynı pikselde olmalı.
