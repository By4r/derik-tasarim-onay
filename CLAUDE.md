# Derik Tasarım Konsepti — Claude Kuralları

## Proje Özeti
- **Marka:** Derik Zeytinyağı (Mardin / Derik kökenli, Halhalı zeytini)
- **Aşama:** Statik HTML konsept tasarımı (henüz production değil)
- **Patron:** Yasin Bey (Dada İstanbul) — onay merci
- **Repo:** https://github.com/By4r/derik-tasarim-onay
- **Canlı:** https://derik-tasarim-onay.netlify.app
- **Auto-deploy:** GitHub main branch → Netlify (30-60 sn)

## Mevcut Sayfalar (kök dizinde)
- `index.html` — Ana sayfa (Hero, Kategoriler, Banner, Yeni Çıkanlar, Çok Satanlar)
- `magaza.html` — Zeytinyağları kategori listesi (filtre + 12 ürün + pagination)
- `urun-detay.html` — Ürün detay (Erken Hasat 500ml örnek)
- `hikayemiz.html` — Hakkımızda > Hikayemiz (3 section)
- `uretim.html` — Hakkımızda > Üretim (3 kategori paragraf akışı)
- `iletisim.html` — İletişim (form + harita)
- `kurumsal-satis.html` — Kurumsal Satış (teklif formu)
- `sss.html` — Sıkça Sorulan Sorular (kategorili accordion)
- `referans/index.html` — KD klonu (DOKUNULMAYACAK, skill referansı)

## Tasarım Tokenları (CSS Variables)

### Renkler
- `--primary-700: #3B4A2A` — koyu zeytin yeşili (header, butonlar, ana CTA)
- `--primary-900: #2A3520` — en koyu (vurgu)
- `--primary-800: #6B7A3F` — orta yeşil (hover)
- `--bg: #FAF6EE` — krem zemin (sayfa)
- `--bg-soft: #F2EBDC` — açık krem (section ayraç)
- `--bg-card: #FAF9F5` — kart zemin
- `--accent-gold: #C9A55B` — altın vurgu (badge, CTA accent, ribbon)
- `--text: #2A1F14` — koyu kahve (ana metin)
- `--text-2: #6B5847` — gri-kahve (ikincil metin)
- `--border: #E8DFC9` — açık bej (border, divider)

### Tipografi
- Font: Inter + system fallback
- Body: 16px / line-height 1.6
- H1: 36-48px, weight 700, letter-spacing -0.025em
- H2 (section): 36px, weight 700
- Eyebrow caps: 12-13px, letter-spacing 0.18em, uppercase
- Pricing: 22-28px, weight 700, --primary-700

### Spacing
- Section padding: 96px desktop, 56px tablet
- Container max-width: 1320px
- Container padding: 32px desktop, 24px tablet, 16px mobile

### Border Radius Scale
- `--r-sm` (6-8px) — input, button, küçük badge
- `--r-md` (10-12px) — kart, banner kart
- `--r-lg` (16-20px) — büyük section, hero
- Pill (999px) sadece: search bar, küçük badge'ler

## İkonlar
- Font Awesome 6 Free (CDN: https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css)
- Tüm SVG ikonlar FA 6 class'ları ile yazılır (örn. `<i class="fa-solid fa-magnifying-glass"></i>`)

## Header (8 sayfa birebir aynı)
Yapı (yukarıdan aşağıya):

1. **Top ribbon (3 sütun):**
   - Sol: "Kurumsal Hediyeler · kurumlara özel fiyatlarla [link]"
   - Orta: "750 TL ÜZERİ KARGO ÜCRETSİZ · YENİ HASAT ÜRÜNLERİ STOKTA" (KARGO ÜCRETSİZ altın renk)
   - Sağ: X kapat butonu (JS ile gizle)
   - Zemin: --primary-700, krem metin, h≈36px
2. **Header top sağ:** "Kurumsal Satış" düz link + "Hakkımızda ▾" dropdown (Hikayemiz, Üretim, Mağazalar)
3. **Header row 1:**
   - Sol: Logo "Derik" düz yazı (placeholder)
   - Orta: Ana menü 5 link tek satır (ZEYTİNYAĞLARI · ZEYTİNLER · SABUNLAR · DOĞAL ÜRÜNLER · HEDİYE SETLERİ)
   - Sağ: İkon set (arama + kullanıcı + kalp + sepet — sepet üstünde altın rozet "0")

### YOK olan elementler
- TR/EN dil switcher (kaldırıldı)
- Telefon barı (kaldırıldı, sadece footer'da)
- KD'deki .fav-btn beyaz oval (display:none)
- Geniş search input (sadece ikon)

## Footer (8 sayfa birebir aynı)
- Sol: Logo "Derik" + tagline "Mardin Derik'ten sofranıza." + adres + sosyal medya (FA brands)
- Kategoriler kolonu (5 link): Zeytinyağları, Zeytinler, Sabunlar, Doğal Ürünler, Hediye Setleri
- Kurumsal kolonu (5 link): Hakkımızda, Derik'in Hikâyesi, Üretim Sürecimiz, Kurumsal Satış, İletişim
- Yardım kolonu (3 link): Sıkça Sorulan Sorular, İade ve Değişim, İletişim
- Footer alt: telif metni + KVKK/Gizlilik/Mesafeli Satış/Çerez Politikası

## Web Replicator Skill
- **Konum:** `.claude/skills/web-replicator/`
- **Görev:** Verilen URL'in tasarım dilini fetch + analyze + generate edip iteratif olarak yaklaştırır
- **5 Faz Pipeline:** FETCH → ANALYZE → GENERATE → COMPARE → ITERATE
- **Tetikleyici:** "site referans al", "URL'in tasarım dilini kopyala", "site X'i clone et"
- **Çıktılar:**
  - `output/{site}-template.html` — generic BRAND placeholder'lı template
  - `output/{site}-design-tokens.md` — renk/font/spacing tokenları
  - `output/{site}-iteration-log.md` — iterasyon notları + sed komutu
- **Test edilmiş:** kahvedunyasi.com (4 iter, başarılı)
- **Aktif kullanım örnekleri:** hikayemiz, uretim, kurumsal-satis, sss sayfaları KD'den çıkarıldı

## Çıktıların Konumu
- **Deploy edilen:** kök dizin (`index.html`, `magaza.html`, vb.)
- **Mirror:** `output/derik-anasayfa.html` (skill referansı için)
- **Skill referansı:** `output/kahvedunyasi-template.html` (DOKUNULMAYACAK)
- **Tokens:** `output/kahvedunyasi-design-tokens.md`
- **Log:** `output/derik-conversion-log.md` (her v#.# için bir bölüm)

## Workflow Kuralları
1. **Plan mode'a geç** (Shift+Tab) — büyük işler için her zaman, küçük revize için skip OK
2. **Auto mode'da implement** — manuel onay yerine
3. **Tüm prompt'lar `=== DEPLOY ===` bloğu ile biter** — bittiğinde `git add + commit + push` otomatik yapılır
4. **Commit mesajları İngilizce DEĞİL — Türkçe ve "v#.# açıklama" formatında** (örn. "v2.7.2 katalog kaldır, form radius fix")
5. **3 sayfada (artık 8 sayfada) header/footer birebir aynı** — herhangi bir değişiklik tüm sayfalara uygulanır
6. **Skill aktif kullanılır:** yeni KD-türevi sayfa eklenirken (`web-replicator skill aktif et, X URL'ini fetch et`)

## Yapılan Versiyonlar (kronolojik)
- **v1** — Derik ilk konsept (kahve dünyası tarzı, BRAND→Derik dönüşüm)
- **v2** — KD'ye yaklaştırma + 3 sayfa (FA ikonlar, top ribbon 3-col, search bar, sepet rozeti, magaza, urun-detay)
- **v2.1** — Header revize (search ikon, ana menü orta, dropdown'lar sağ üst, section sıralama)
- **v2.2** — Radius scale + magaza filtre paneli düzeltme
- **v2.3** — Buton radius + Hakkımızda dropdown spacing + filter sticky fix
- **v2.4** — hikayemiz.html (skill ile KD referansı)
- **v2.4.1** — hikayemiz section 1 altındaki büyük görsel kaldırıldı
- **v2.4.2** — Ürün kartlarındaki beyaz elips (.fav-btn) kaldırıldı
- **v2.4.3** — fav-btn arka plan kaldırıldı, görseller geri geldi, kalp sağ üst sade
- **v2.5** — uretim.html (skill, paragraf akışı, kart yok)
- **v2.5.1** — uretim KD'ye yakınlaştırıldı (skill iter)
- **v2.5.2** — uretim son ekstra üretim tesisi görseli kaldırıldı
- **v2.6** — iletisim.html (Netlify Forms + Google Maps)
- **v2.6.1** — iletisim yeşil hero kaldırıldı
- **v2.7** — kurumsal-satis.html (skill ile)
- **v2.7.1** — kurumsal-satis KD'ye yakınlaştırıldı
- **v2.7.2** — katalog kaldır, form radius fix, ambalaj checkbox kaldır, telefon input grup fix
- **v2.8** — sss.html (skill ile, accordion + kategoriler)

## Park Edilen Görevler (sonradan)
- **Canlı Destek floating buton** — KD'de sağ alt köşede vardı, Derik'te sonra
- **Mega menu** — kategori hover'da alt menü
- **Slider auto-rotate** — hero banner otomatik geçiş
- **Sepet drawer aç-kapa** — sepet ikonuna tıklayınca yan panel
- **Real product API** — şu an statik veri
- **Logo SVG** — şu an "Derik" düz yazı, ileride stilize logo
- **Çoklu adres CRUD** — production aşamasında admin paneli ile
- **Mağazalar sayfası** — Hakkımızda > Mağazalar dropdown linki var ama sayfa yok

## Önemli Notlar
- **macOS Finder drag = move (kopyala değil)** — Option+drag ile kopyala. Dosyayı yanlışlıkla başka klasöre sürüklersen Code "file disappeared" hatası verir.
- **Tarayıcıda dosya açıkken Code yazamayabilir** — Bazı durumlarda. Öyle bir hata gelirse tab'ı kapat.
- **Netlify auto-deploy 30-60 sn** — `git push` sonrası bu süre kadar bekle, sonra hard refresh (Cmd+Shift+R)
- **Tüm yeni sayfalarda** header (top ribbon + telefon barsız + dropdown'lar) ve footer aynı yapıda olmalı, 8 sayfa senkron

## Skill Tetikleyici Tipik Komutlar
- "Şu URL'i referans al, Derik'e uyarla" → web-replicator aktif olur
- "X sayfasını skill ile iterate et" → 2-3 ek iterasyon
- "Y URL'i fetch + analyze et" → sadece bilgi toplama
