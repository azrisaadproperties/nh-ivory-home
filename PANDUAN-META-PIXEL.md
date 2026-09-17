# Panduan Meta Pixel — Apa Yang Perlu Ada

> Panduan langkah demi langkah untuk memasang Meta Pixel bagi laman web NH Ivory Home.
> Termasuk jawapan kepada soalan: **perlu ada Facebook Page?**

---

## 1. JAWAPAN RINGKAS

| Soalan | Jawapan |
|---|---|
| Perlu akaun Facebook? | **Ya** — akaun peribadi (percuma), untuk log masuk |
| Perlu Facebook Page? | **Ya, disyorkan** — perlu untuk jalankan iklan |
| Perlu bayar? | **Tidak** — semuanya percuma |
| Perlu akses laman web? | **Ya** — tapi kita sudah ada, saya boleh pasang |
| Perlu domain sendiri? | Tidak wajib, tapi **membantu** (lihat seksyen 6) |

**Masa diperlukan:** 15–20 minit.

---

## 2. PERLU FACEBOOK PAGE? — YA

Ini soalan biasa. Jawapannya:

| Kegunaan | Perlu Page? |
|---|---|
| Buat Meta Pixel sahaja | Secara teknikalnya tidak |
| **Jalankan iklan (Facebook/Instagram Ads)** | **Ya — WAJIB** |
| Letak butang "Hantar Mesej" / "WhatsApp" | Ya |
| Bina kepercayaan pelanggan | Ya |

Sebabnya: setiap iklan di Meta mesti ada **identiti** — iaitu Page. Anda tidak boleh
jalankan iklan tanpa Page.

**Kesimpulan:** buat Page. Ia percuma dan perlu.

---

## 3. DUA PILIHAN PAGE

Syarikat NH Ivory Home **sudah ada** Page rasmi: `facebook.com/NHhomeconstruction`

Anda perlu pilih:

### Pilihan A — Guna Page sedia ada (NH Ivory Home)
**Baik jika:**
- Anda ada akses kepada Page syarikat itu
- Mahu iklan keluar sebagai jenama rasmi (lebih dipercayai)
- Mahu selaras dengan review & follower sedia ada

**Tidak baik jika:**
- Anda tidak ada akses penuh (perlu minta admin tambah anda)
- Pixel akan bercampur dengan data syarikat

### Pilihan B — Buat Page baharu (contoh: "NH Ivory Home — Perak")
**Baik jika:**
- Anda mahu kawalan penuh (pasukan jualan sendiri)
- Anda tidak mahu bergantung pada akses orang lain
- Anda mahu data pixel berasingan untuk kempen anda

**Tidak baik jika:**
- Mula dari kosong (tiada follower, tiada review)

> **Cadangan saya:** jika anda ada akses kepada Page syarikat, **guna Pilihan A** —
> kepercayaan pelanggan lebih tinggi dan iklan lebih murah (engagement sedia ada).
> Jika tidak, **Pilihan B** berfungsi sepenuhnya.

---

## 4. SENARAI SEMAK — APA YANG PERLU ADA

| # | Item | Status |
|---|---|---|
| 1 | Akaun Facebook peribadi | Perlu ada |
| 2 | Meta Business Portfolio (Business Manager) | Cipta (percuma, 5 min) |
| 3 | Facebook Page | Guna sedia ada **atau** buat baharu |
| 4 | Akaun Pengiklanan (Ad Account) | Cipta dalam Business Portfolio |
| 5 | Kaedah pembayaran | Kad kredit/debit untuk iklan |
| 6 | Akses laman web | **Sudah ada** — saya pasang pixel |
| 7 | (Pilihan) Akaun Instagram | Sambung untuk iklan IG |

---

## 5. LANGKAH MEMASANG META PIXEL

### Langkah 1 — Cipta Business Portfolio
1. Buka **https://business.facebook.com**
2. Log masuk dengan akaun Facebook anda
3. Klik **Create account**
4. Isi:
   - Business name: `NH Ivory Home`
   - Your name: (nama anda)
   - Business email: (email anda)
5. Klik **Submit**

### Langkah 2 — Tambah Facebook Page
1. Dalam Business Settings, pergi ke **Accounts → Pages**
2. Klik **Add → Add a Page**
3. Pilih Page sedia ada **atau** klik **Create a new Page**

### Langkah 3 — Buat Akaun Pengiklanan
1. **Accounts → Ad accounts → Add → Create a new ad account**
2. Namakan: `NH Ivory Home Ads`
3. Mata wang: **MYR**
4. Zon masa: **Malaysia (GMT+8)**
5. Tambah kaedah pembayaran

### Langkah 4 — Cipta Pixel
1. Buka **https://business.facebook.com/events_manager**
2. Klik **Connect data sources** → **Web**
3. Pilih **Facebook Pixel** → **Connect**
4. Nama pixel: `NH Ivory Home Website`
5. URL laman: `azrisaadproperties.github.io`
6. Klik **Continue**
7. **Salin ID Pixel** — nombor panjang 15–16 digit

**Contoh format ID:**
```
1234567890123456
```

8. **Hantar ID itu kepada saya** — saya pasang dalam semua 18 halaman

---

## 6. DOMAIN VERIFICATION (PENTING untuk iOS)

Ini langkah yang ramai terlepas. Ia penting untuk:
- **Aggregated Event Measurement** (iOS 14.5+) — tanpa ini, sebahagian event dari
  pengguna iPhone tidak dapat diukur
- Keutamaan event (contoh: `Lead` diutamakan berbanding `PageView`)

### Cara verify
1. **Business Settings → Brand Safety → Domains**
2. Klik **Add** → taip: `azrisaadproperties.github.io`
3. Pilih kaedah **Meta-tag verification**
4. Meta akan bagi kod seperti:
   ```html
   <meta name="facebook-domain-verification" content="abc123..." />
   ```
5. **Hantar kod itu kepada saya** — saya pasang dalam semua halaman
6. Klik **Verify**

> **Nota:** GitHub Pages tidak membenarkan kita ubah DNS, jadi kaedah **meta-tag**
> adalah satu-satunya pilihan. Ia berfungsi.
>
> Kalau nanti anda guna **domain sendiri**, verification jadi lebih mudah.

---

## 7. SELEPAS PIXEL DIPASANG

### Di Events Manager
- Buka **Test Events** — lawat laman web anda, event akan muncul secara langsung
- Event yang patut nampak: `PageView`, `Lead`, `Contact`, `InitiateCheckout`, `ViewContent`

### Di Ads Manager
Bila buat kempen:
| Tetapan | Nilai |
|---|---|
| Objective | **Leads** |
| Conversion event | **Lead** |
| Optimization | **Conversions** |
| Placement | Advantage+ (automatik) |

Ini memberitahu Meta supaya cari orang yang **berkemungkinan besar isi borang**,
bukan sekadar klik. Kos lead biasanya **turun 30–50%**.

---

## 8. APA SAYA PERLUKAN DARI ANDA

Hantar dalam format ini:

```
Meta Pixel ID: 1234567890123456
Domain verification tag: <meta name="facebook-domain-verification" content="..." />
```

Saya akan:
1. Pasang dalam `index.html`, `thankyou.html`, dan `tools/generate-pages.py`
2. Jana semula 16 halaman lokasi & blog
3. Push ke GitHub (live 1–2 minit)
4. Uji dan sahkan event berfungsi

---

## 9. SOALAN LAZIM

**Perlu kad kredit untuk buat pixel?**
Tidak. Kad hanya perlu bila anda mula jalankan iklan (bayar). Buat pixel adalah percuma.

**Boleh pasang pixel tanpa Page?**
Secara teknikalnya boleh (dalam Events Manager), tapi anda tidak boleh jalankan iklan.
Jadi buat Page.

**Kalau saya tukar Page kemudian, kena buat pixel baharu?**
Tidak. Pixel boleh dikongsi antara Page dan Ad Account dalam Business Portfolio yang sama.

**Perlu Instagram?**
Tidak wajib, tapi jika ada, sambungkan — iklan akan keluar di IG juga (biasanya lebih murah).

**Berapa lama sampai data masuk?**
Test Events: **serta-merta**. Laporan penuh: **24–48 jam**.

**Risau data pelanggan?**
Meta Pixel hanya merekod tingkah laku di laman (halaman dilihat, butang diklik).
Ia **tidak** menghantar nama atau nombor telefon pelanggan anda.
