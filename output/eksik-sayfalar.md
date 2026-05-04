# Derik — Eksik Sayfalar Raporu

**13 mevcut / ~30 hedef** · 2026-05-04

Kaynaklar: `derik-arayüz.docx` (front-end briefing), `derik-back.docx` (sistem briefing), `CLAUDE.md`, `output/derik-conversion-log.md`, root `*.html`. Pattern referansları: kahvedunyasi.com (sade gıda e-ticaret), trendyol.com (e-ticaret işlevsel pattern).

---

## ✅ Mevcut Sayfalar (13)

| # | Dosya | Tip | Briefing maddesi |
|---|---|---|---|
| 1 | `index.html` | Ana sayfa | §4 |
| 2 | `magaza.html` | Kategori listesi | §5 |
| 3 | `urun-detay.html` | Ürün detay | §6 |
| 4 | `hikayemiz.html` | Marka hikayesi | §7 |
| 5 | `uretim.html` | Üretim süreci | §7 |
| 6 | `iletisim.html` | İletişim | §1 |
| 7 | `kurumsal-satis.html` | Kurumsal teklif | §1, §4.7 |
| 8 | `sss.html` | SSS | (tamamlayıcı) |
| 9 | `uyelik-bilgilerim.html` | Hesap > Profil | §10.1 |
| 10 | `siparis-gecmisim.html` | Hesap > Siparişler | §10.1 |
| 11 | `siparis-detay.html` | Hesap > Sipariş detayı | §10.10 |
| 12 | `adreslerim.html` | Hesap > Adresler | §10.1 |
| 13 | `promosyonlarim.html` | Hesap > Kuponlar | §10.7 |

---

## 🔴 Kritik (MVP — checkout akışı + auth + yasal)

E-ticaret çalışır olabilmesi için olmazsa olmaz.

### Auth & üyelik

#### `giris.html` — Üye Girişi / Kayıt
- **Briefing:** §10.1 "Üye olma, Giriş yapma"
- **Pattern:** KD `/uye-girisi` — sol "Giriş" + sağ "Yeni Üye" kolonu (form çift sütun) ya da Trendyol "tab switch" (Giriş / Üye Ol)
- **Kapsam:** Orta. E-mail/şifre + "Beni hatırla" + sosyal (opsiyonel) + "Şifremi unuttum" linki + KVKK onayı.

#### `sifre-sifirlama.html` — Şifre Sıfırlama
- **Briefing:** §10.1, §10.13 "Şifre sıfırlama"
- **Pattern:** KD/Trendyol — tek alan e-mail + "Sıfırlama bağlantısı gönder" + onay ekranı + (token URL ile yeni şifre form)
- **Kapsam:** Sade. 2 ekran (talep + reset).

### Checkout akışı

#### `sepet.html` — Sepet
- **Briefing:** §1, §10.5 — ürün liste + adet ± + kupon kodu + ücretsiz kargo bildirimi + ara toplam/KDV/toplam + hediye paketi/notu seçenekleri + "Ödemeye Geç"
- **Pattern:** KD `/sepet` — sol ürün listesi + sağ özet kartı (sticky)
- **Kapsam:** Karmaşık. Empty state + dolu state. Ücretsiz kargo progress bar ("125 TL kaldı"). Hediye paketi modal'i (varsa).

#### `odeme.html` — Ödeme / Checkout
- **Briefing:** §1, §10.9
- **Pattern:** Trendyol/KD — accordion stepper: 1) Adres seç (radio + yeni ekle modal — adreslerim.html'deki modal yeniden kullanılır) 2) Teslimat (kargo seçimi) 3) Ödeme (kart formu / havale / 3D secure iframe placeholder) + sağ sticky özet
- **Kapsam:** Karmaşık. Sayfanın yarısı bu sticky.

#### `odeme-basarili.html` — Sipariş Onay
- **Briefing:** §10.10 "Sipariş alındı"
- **Pattern:** KD/Trendyol — büyük tik + "Siparişiniz alındı (DRK-XXXXX)" + sipariş özeti + "Sipariş takibine git" CTA
- **Kapsam:** Sade. Tek state.

#### `odeme-basarisiz.html` — Ödeme Hatası (opsiyonel ama önerilir)
- **Briefing:** §10.9 "Ödeme başarılı / başarısız ekranı"
- **Pattern:** Hata mesajı + sebep + "Tekrar dene" CTA
- **Kapsam:** Sade.

### Yasal sayfalar (footer linklerinin tamamı zaten yok)

Tek bir `legal-template.html` mantığında 5 sayfa — yapısı aynı, içerik farklı.

#### `kargo-teslimat.html`
- **Briefing:** Footer Yardım kolonu, §10.8
- **Pattern:** KD `/kargo-ve-teslimat` — başlık + 4-6 bölüm (kargo süresi tablosu, ücretler, teslimat bölgesi, ücretsiz kargo şartı)
- **Kapsam:** Sade.

#### `iade-degisim.html`
- **Briefing:** Footer + §10.12 "İade ve iptal sistemi"
- **Pattern:** KD `/iade-ve-degisim` + Trendyol `/iade-ve-iptal` — adım listesi (hesabımdan iade talebi → kargo → onay → iade) + iade nedenleri + IBAN talep formu (opsiyonel)
- **Kapsam:** Sade-orta. İade akışı yazılı; gerçek formu hesap altında.

#### `mesafeli-satis.html`, `gizlilik.html`, `kvkk.html`, `cerez-politikasi.html`
- **Briefing:** Footer Yasal kolonu
- **Pattern:** KD `/kvkk` — uzun metin sayfası, sol içindekiler navigasyonu (opsiyonel)
- **Kapsam:** Sade. Hukuki metin (Hukuk danışmanından alınacak; placeholder kullanılabilir).

---

## 🟡 Orta Öncelik (UX tamamlayıcılar + alt kategoriler)

#### `favoriler.html` — Favori Listem
- **Briefing:** §10.1 "Favori ürünleri görüntüleme"
- **Pattern:** Trendyol `/favorilerim` — magaza grid'i ama "favoriden çıkar" + "sepete ekle" kart aksiyonu, empty state ile
- **Kapsam:** Sade. magaza.html'in basitleştirilmiş varyasyonu. Header'daki kalp ikonu zaten yönlendirme bekliyor.

#### `iade-taleplerim.html` — Hesap > İadelerim
- **Briefing:** §10.1, §10.12
- **Pattern:** Trendyol "İade Taleplerim" — sipariş gecmisi gibi liste + her satır: durum (Talebi Alındı/İnceleniyor/Onaylandı/Reddedildi/Tamamlandı) + detay
- **Kapsam:** Orta. Hesap sidebar'a yeni link, sayfa siparis-gecmisim'e benzer.

#### `iade-olustur.html` veya iade modal
- **Briefing:** §10.12 — sipariş seçimi + ürün checkbox + iade nedeni dropdown + açıklama + foto upload + IBAN
- **Pattern:** Trendyol "İade Talebi Oluştur" — multi-step
- **Kapsam:** Orta. Modal mı ayrı sayfa mı kararı: ayrı sayfa daha iyi (uzun form + foto upload).

#### `arama.html` — Arama Sonuçları
- **Briefing:** §10.17 — site içi arama, otomatik öneri, kategoriye göre filtreleme
- **Pattern:** KD/Trendyol `/arama?q=zeytinyagi` — magaza layout + "X için Y sonuç" başlığı + öneri/popüler aramalar (boş sonuç state)
- **Kapsam:** Orta. Header arama ikonu boşa gidiyor şu an.

#### Kategori sayfaları (alt kategoriler) — `zeytinler.html`, `sabunlar.html`, `dogal-urunler.html`, `hediye-setleri.html`
- **Briefing:** §1, §5 site haritası
- **Pattern:** magaza.html clone + filter "Kategori" pre-selected
- **Kapsam:** Sade. magaza.html'i parametrik yap (`?kategori=sabunlar`) yeterli olabilir; ayrı dosya açmak yerine.

#### `hakkimizda.html` — Hakkımızda
- **Briefing:** §1, §8 "Markanın amacı ve vizyonu" — hikayemiz'den farklı, daha kurumsal
- **Pattern:** KD `/hakkimizda` — kurucu, vizyon, değerler, ekip
- **Kapsam:** Sade. hikayemiz.html template'i + farklı içerik. (Ya da menüden kaldırılır, hikayemiz yeterli kabul edilir — patron kararı)

---

## 🟢 Faz 2 (production öncesi son aşama)

#### `404.html` — Sayfa Bulunamadı
- Sade. Marka tonlu mesaj + "Anasayfaya dön" + popüler kategoriler.

#### `magazalar.html` — Fiziksel Mağazalar
- Header dropdown'da "Mağazalar" linki var ama sayfa yok. Harita + adres listesi. (Briefing'de yok; patron kararına bağlı — fiziksel satış noktası var mı?)

#### `bayilik.html` — Bayilik Başvurusu (opsiyonel)
- Kurumsal satış'tan ayrı, distribütörlük formu. Briefing'de yok.

#### `mini-sepet-drawer` (sayfa değil — global component)
- Sepet ikonuna tıklayınca yan panel — şu an direkt sepet sayfasına gidiyor.

#### `live-chat-widget` (component)
- Briefing'de WhatsApp önerisi var; canlı destek widget yerine WhatsApp floating buton yeterli olabilir.

---

## 💡 Skill'in Tespit Ettiği Ek Sayfalar (briefing'de yer almayan)

- **Newsletter onay sayfası** (`bulten-onay.html`) — KVKK gereği opt-in onay ekranı, e-mail tıklanırsa landing.
- **E-bülten abonelik formu** — footer'a inline + ayrı sayfa gerekirse.
- **Ürün karşılaştırma** (`karsilastir.html`) — KD'de yok, Trendyol'da var. Zeytinyağı için kategori başına 2-3 ürün karşılaştırma. Düşük öncelikli.
- **Blog** (`blog.html` + `blog-yazi.html`) — SEO açısından değerli (zeytinyağı kullanım/reçete içerikleri); ileride.
- **Yorumlarım** (`yorumlarim.html`) — Hesap altına ayrı sayfa: kullanıcının yazdığı tüm değerlendirmeler. Trendyol var, KD yok. Düşük.

---

## 🔗 Bağlantı Haritası — Mevcut Element → Eksik Sayfa

| Element / konum | Şu an | Olması gereken |
|---|---|---|
| Header `<a href="#hesap">` user ikon | `uyelik-bilgilerim.html`'e gidiyor + dropdown | Login değilse `giris.html`'e yönlendir |
| Header arama ikonu | `<a href="#ara">` ölü link | `arama.html` + arama paneli/modal |
| Header kalp ikonu | `<a href="#favoriler">` ölü link | `favoriler.html` |
| Header sepet ikonu | `<a href="#sepet">` ölü link | `sepet.html` (veya drawer aç) |
| Header dropdown "Mağazalar" | `<a href="#magazalar">` ölü link | `magazalar.html` veya menüden çıkar |
| Header ana menü (Zeytinler/Sabunlar/Doğal/Hediye) | Hash linkler `#zeytinler` vb. | Kategori sayfaları veya `magaza.html?kategori=X` |
| Footer "Sıkça Sorulan Sorular" | `sss.html` ✅ | OK |
| Footer "İade ve Değişim" | `<a href="#iade">` | `iade-degisim.html` |
| Footer Yasal kolonu (KVKK/Gizlilik/Mesafeli/Çerez) | `<a href="#">` ölü 4 link | 4 ayrı yasal sayfa |
| Footer "Hakkımızda" | `<a href="#hakkimizda">` ölü | `hakkimizda.html` veya `hikayemiz.html`'e yönlendir |
| Hesap sidebar "Çıkış Yap" | `<a href="#">` ölü | `giris.html`'e yönlendir + session clear |
| Sipariş kart "Detaylar" | `siparis-detay.html?id=X` ✅ | OK |
| Sipariş kart "Kargo Takip" | Modal ✅ | OK |
| Sipariş kart "Değerlendir" | Modal ✅ | OK |
| `urun-detay.html` "Sepete Ekle" | `bumpCart()` JS counter | Gerçek sepet → `sepet.html` flow |
| `urun-detay.html` "Hemen Al" | (yok / ölü) | Direkt `odeme.html`'e |
| Promosyon "Kullan" | Clipboard copy ✅ | OK |
| `kurumsal-satis.html` form | Netlify Forms ✅ | OK |

---

## 📋 Global Component Eksikleri (sayfa değil ama gerekli)

- **Cookie banner** — KVKK gereği. Sayfanın altında sticky bar + "Kabul et" / "Reddet" / "Tercihler" + ilk ziyaret'te localStorage flag.
- **Login wall / auth gate** — Hesap sayfaları (uyelik, siparis, adres, promosyon, favoriler, iade) login değilse `giris.html?next=...`'a redirect.
- **WhatsApp floating buton** — sağ alt köşe. Briefing §1 ve §3'te isteniyor.
- **Mobile hamburger menü** — şu an <1024px'te ana nav gizli, hamburger açılırı yok.
- **Mini sepet drawer** — sepet ikonu yan panel açar (alternatif: `sepet.html`).
- **Toast/notification system** — şu an sadece `promosyonlarim.html`'de var; sepete ekle/favorilere ekle vb. her yerde lazım.
- **Search dropdown** (otomatik öneri) — header arama ikonu açılır panel + öneri listesi.
- **Newsletter footer formu** — şu an yok, footer'a satır eklenmeli.
- **Breadcrumb component** — `crumb` zaten var ama her sayfada elle yazılıyor; ortak parça yapılabilir (build script ile).
- **Skeleton loader** (production) — async ürün/sipariş listesi için.

---

## 🤔 Patrona Karar Bekleyen Sorular

1. **Hakkımızda ayrı bir sayfa mı, hikayemiz yeterli mi?** Briefing'de ikisi de listelenmiş ama içerik örtüşüyor.
2. **Fiziksel mağaza var mı?** Header'da "Mağazalar" linki var; yoksa menüden çıkarılsın.
3. **Login provider tercihi** — sadece e-mail/şifre mi, yoksa Google/Facebook sosyal login de mi? (Google önerilir; Apple iOS için gerekirse.)
4. **Kapıda ödeme aktif mi?** Briefing §10.9 "opsiyonel" diyor.
5. **Hediye paketi seçeneği** — sepet'te mi, ürün detay'da mı, ödeme'de mi? KD ödeme'de, Trendyol sepet'te.
6. **Üye olmadan alışveriş (guest checkout)** — destekleniyor mu? Trendyol var, KD yok.
7. **Yorum onay süreci** — kullanıcı yorumu admin moderasyonundan geçmeli mi (spam/hakaret koruması)?
8. **B2B kurumsal müşteri özel fiyat** — admin tarafından açılan kurumsal hesap için ürün kart fiyatları farklı mı görünmeli?
9. **Hediye notu ne uzunlukta?** (160 karakter SMS gibi mi, 500 karakter mektup gibi mi?)
10. **Çoklu dil desteği** — TR-only mi, EN paralel mi? (Mevcut kararla TR-only kaldırıldı; teyit?)
11. **Alt kategori sayfaları** ayrı dosya mı, `magaza.html?kategori=X` parametrik mi?
12. **Yasal sayfa metinleri** — hukuk danışmanından alınacak mı, GPT taslak yeterli mi?

---

## 📊 Özet

| Kategori | Adet |
|---|---|
| ✅ Mevcut | **13** |
| 🔴 Kritik (MVP) | **11** (giriş, şifre-sıfırlama, sepet, ödeme, ödeme-başarılı, ödeme-başarısız, kargo-teslimat, iade-değişim, mesafeli-satış, gizlilik, KVKK, çerez) → 11 |
| 🟡 Orta | **8** (favoriler, iade-taleplerim, iade-oluştur, arama, 4 alt kategori, hakkımızda) |
| 🟢 Faz 2 | **3** (404, mağazalar, bayilik) |
| **Toplam hedef (sayfa)** | **~32** |
| Global component eksikleri | 10 (sayfa değil) |
| Patrona karar bekleyen | 12 soru |

**Tahmini iş yükü:** Kritik MVP 11 sayfa: ~3-4 oturum (sepet+ödeme en yoğun). Orta: 1-2 oturum. Yasal sayfa metinleri patrondan/hukuktan gelmeden iskelet bırakılabilir.

**Önerilen sıra:**
1. Login/Kayıt + Şifre sıfırlama (auth temeli)
2. Sepet → Ödeme → Sipariş onay (checkout zinciri)
3. Yasal 5 sayfa (template + içerik placeholder)
4. Favoriler + Arama (header ikonları çalışsın)
5. İade akışı (hesap modülü tamamlansın)
6. Alt kategori sayfaları + 404 + global component'ler
