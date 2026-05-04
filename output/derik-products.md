# Derik Ürün Görsel Kataloğu

Tüm ürün görselleri için tek doğruluk kaynağı (single source of truth).

URL formatı: `https://images.unsplash.com/photo-{ID}?w=400&h=400&fit=crop&q=80`

## Aktif Görsel Havuzu (8 ID — test edilmiş)

| ID | Konu | Kullanım Bağlamı |
|---|---|---|
| `1474979266404-7eaacbcd87c5` | Zeytinyağı şişesi | Zeytinyağları kategorisi, Erken Hasat, Klasik, generic bottle |
| `1632934237526-79b9b09b3a47` | Yeşil zeytinler | Halhalı Yeşil Zeytin |
| `1593001872095-7d5b3868fb1d` | Halhalı siyah zeytin | Zeytinler kategorisi, Halhalı Özel Üretim |
| `1620706857370-e1b9770e8bb1` | Zeytinyağı + bitki | Soğuk Sıkım, Doğal Ürünler, Organik |
| `1607006677595-ee20fd96574e` | Sabun | Zeytinyağlı Sabun, Sabunlar kategorisi |
| `1549049950-48d5887197a0` | Hediye seti / kutu | Hediye Setleri, Mini Kutu |
| `1639667402194-bdcc7e1c0e8f` | Zeytinyağı + ahşap kaşık | Teneke 5L, Aile Boyu 1L, premium |
| `1601001435957-74f0958a93c5` | Zeytin dalı / olive grove | Hikayemiz, Üretim, Yeni Hasat, Kurumsal |

## Ürün → Görsel Eşleşmesi (alt text bazlı)

| Ürün adı (alt) | ID | Sayfalar |
|---|---|---|
| Erken Hasat Naturel Sızma Zeytinyağı 500ml | `1474979266404-7eaacbcd87c5` | index, magaza, urun-detay, siparis-gecmisim, siparis-detay |
| Erken Hasat Premium 250ml / 1L | `1474979266404-7eaacbcd87c5` | index, magaza, urun-detay |
| Klasik Natürel Sızma 750ml | `1474979266404-7eaacbcd87c5` | index, magaza, urun-detay |
| Halhalı Yeşil Zeytin 1kg / 500g | `1632934237526-79b9b09b3a47` | index, siparis-gecmisim, siparis-detay |
| Halhalı Özel Üretim 750ml | `1593001872095-7d5b3868fb1d` | magaza |
| Soğuk Sıkım Zeytinyağı 1L | `1620706857370-e1b9770e8bb1` | index, magaza, urun-detay |
| Organik Natürel Sızma 500ml | `1620706857370-e1b9770e8bb1` | magaza |
| Zeytinyağlı Sabun 3'lü Set | `1607006677595-ee20fd96574e` | index, uretim |
| Hediye Seti Premium / Mini | `1549049950-48d5887197a0` | index, magaza, siparis-gecmisim, siparis-detay |
| Teneke 5L Zeytinyağı / Aile Boyu | `1639667402194-bdcc7e1c0e8f` | index, magaza, urun-detay |
| Halhalı zeytinleri / üretim | `1601001435957-74f0958a93c5` | hikayemiz, uretim |

## Kategori Görselleri (anasayfa)

| Kategori | ID |
|---|---|
| Zeytinyağları | `1474979266404-7eaacbcd87c5` |
| Zeytinler | `1593001872095-7d5b3868fb1d` |
| Sabunlar | `1607006677595-ee20fd96574e` |
| Doğal Ürünler | `1620706857370-e1b9770e8bb1` |
| Hediye Setleri | `1549049950-48d5887197a0` |
| Kurumsal | `1601001435957-74f0958a93c5` |

## Img Tag Standartları

Her `<img>` aşağıdaki attribute'lara sahip olmalı:

```html
<img src="https://images.unsplash.com/photo-{ID}?w=400&h=400&fit=crop&q=80"
     alt="Türkçe ürün adı"
     loading="lazy"
     width="400"
     height="400">
```

CSS `object-fit: cover` parent kapsayıcıdaki `.thumb`, `.product .img-wrap`, `.cat`, `.banner` üzerinden uygulanır.

## Boyut Varyantları

URL'deki `w=` ve `h=` parametreleri context'e göre değişir, ama Unsplash CDN dinamik resize yaptığı için 400x400 default yeterli — tarayıcı CSS ile küçültür. Tek istisna review modal'ında `w=200&h=200` (modal thumb 60-80px).

## Güncelleme Süreci

Yeni ürün eklendiğinde:
1. Bu dosyaya satır ekle
2. Yeni ID gerekiyorsa Unsplash'te lisans uyumlu görsel bul, ID'yi test et
3. Tüm sayfalarda alt-text → ID eşleşmesi rules güncelle (`output/_fix_images.py` benzeri script tutuluyorsa)
