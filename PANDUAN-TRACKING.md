# Panduan Tracking: Meta Pixel & GA4

Kedua-duanya adalah **ID percuma** daripada Facebook dan Google. Anda hanya perlu
salin 2 ID, beri kepada saya, dan saya pasang.

**Kenapa perlu?**
- **Meta Pixel** — untuk iklan Facebook/Instagram. Ia memberitahu Facebook siapa yang
  hantar borang, supaya iklan boleh dioptimumkan dan anda boleh buat *retargeting*.
- **GA4** — untuk tahu dari mana pelawat datang, halaman mana popular, berapa ramai
  yang isi borang.

Kedua-duanya **percuma** dan **tidak wajib** untuk laman berfungsi. Laman tetap
berjalan tanpanya — cuma anda tidak nampak data.

---

## BAHAGIAN 1 — Meta Pixel ID

Masa diperlukan: ~10 minit. Perlu akaun Facebook.

### Langkah

1. Buka **https://business.facebook.com/events_manager**
2. Log masuk dengan akaun Facebook anda
3. Jika diminta, pilih / cipta **Business Account** (isi nama: NH Ivory Home)
4. Klik **"Connect data sources"** (butang hijau)
5. Pilih **Web**
6. Pilih **Facebook Pixel** → **Connect**
7. Namakan pixel: `NH Ivory Home Website`
8. Masukkan URL laman: `azrisaadproperties.github.io`
9. Klik **Continue**
10. Anda akan nampak **ID Pixel** — satu **nombor panjang (15–16 digit)**, contoh:

    ```
    1234567890123456
    ```

11. **Salin nombor itu** dan hantar kepada saya.

### Kalau anda sudah ada Pixel
Buka Events Manager → **Data sources** → klik pixel anda → ID ada di bahagian atas.

---

## BAHAGIAN 2 — GA4 Measurement ID

Masa diperlukan: ~10 minit. Perlu akaun Google (boleh guna Gmail).

### Langkah

1. Buka **https://analytics.google.com**
2. Log masuk dengan akaun Google
3. Klik **"Start measuring"**
4. **Account name**: `NH Ivory Home`
5. Klik **Next** → **Property name**: `Laman Web NH Ivory Home`
6. Pilih **Reporting time zone**: `Malaysia (GMT+8)`
7. Pilih **Currency**: `Malaysian Ringgit (RM)`
8. Klik **Next** → pilih **Web**
9. **Website URL**: `https://azrisaadproperties.github.io/nh-ivory-home/`
   **Stream name**: `Laman Web Utama`
10. Klik **Create stream**
11. Anda akan nampak **Measurement ID** — format begini:

    ```
    G-XXXXXXXXXX
    ```

12. **Salin ID itu** dan hantar kepada saya.

---

## BAHAGIAN 3 — Hantar kepada saya

Cukup hantar dalam format ini:

```
Meta Pixel: 1234567890123456
GA4: G-XXXXXXXXXX
```

Saya akan:
1. Masukkan ID ke dalam laman
2. Jana semula semua 17 halaman
3. Push ke GitHub (live dalam 1–2 minit)
4. Uji dan sahkan event berfungsi

---

## Event Yang Sudah Dipasang

Laman ini sudah menghantar event berikut secara automatik. Anda tidak perlu buat apa-apa:

| Event | Bila dihantar | Guna untuk |
|---|---|---|
| `PageView` | Setiap lawatan halaman | Kira trafik |
| `Lead` | Bila borang dihantar | **Conversion utama** — untuk optimasi iklan |
| `Contact` | Klik butang WhatsApp / popup | Kira minat hubungi |
| `InitiateCheckout` | Klik CTA pakej / tunai / loan | Kira minat pakej |
| `ViewContent` | Video testimoni dimainkan | Kira minat kandungan |

---

## Selepas Dipasang — Di Facebook Ads

Bila anda buat kempen iklan, pilih:

- **Conversion event**: `Lead`
- **Optimization goal**: `Leads`

Ini akan memberitahu Facebook supaya cari orang yang **berkemungkinan besar isi borang**,
bukan sekadar klik. Kos lead biasanya turun 30–50%.

---

## Soalan Lazim

**Perlu bayar?**
Tidak. Kedua-duanya percuma sepenuhnya.

**Kalau saya tak mahu buat sekarang?**
Tidak mengapa. Laman tetap berfungsi. Boleh pasang bila-bila masa.

**Boleh saya buat sendiri?**
Boleh — buka `index.html`, cari `metaPixelId: ""` dan `ga4Id: ""`, isi ID di situ,
kemudian untuk halaman lokasi/blog, edit `tools/generate-pages.py` (cari
`META_PIXEL_ID = ""` dan `GA4_ID = ""`) dan jalankan:

```bash
python3 tools/generate-pages.py
git add . && git commit -m "Tambah tracking" && git push
```

**Risau data pelanggan?**
Meta Pixel dan GA4 hanya merekod tingkah laku di laman (halaman dilihat, butang diklik).
Ia **tidak** menghantar nama atau nombor telefon anda ke Facebook/Google.
