# NH Ivory Home Sdn. Bhd. — Web Sales Funnel

Landing page jualan untuk perkhidmatan **bina rumah / banglo atas tanah sendiri** di
**Perak, Kedah & Pulau Pinang**.

Funnel: **Iklan → Landing Page → Borang → Lead masuk Google Sheets + WhatsApp → Konsultasi Percuma**.

## Info Syarikat (telah dimasukkan)

| Perkara | Nilai |
|---|---|
| Nama Syarikat | NH Ivory Home Sdn. Bhd. |
| No. Syarikat | 20200101283 (1369193-H) |
| Lesen CIDB | G4 · 0120210118-WP066824 |
| MOF | Berdaftar |
| Beroperasi sejak | 02 Jun 2020, Seri Iskandar, Perak |
| Ibu Pejabat | No 70A, Persiaran SIBC 4, Bandar Seri Iskandar, 32610 Seri Iskandar, Perak |
| WhatsApp Lead | 011-6336 6464 (601163364664) |
| Liputan | Perak, Kedah, Pulau Pinang |
| Kaedah binaan | Tunai, Loan Bank, LPPSA |
| Reka bentuk | 100+ pilihan |
| Pelanggan | 2000++ |

Sosial: [Facebook](https://www.facebook.com/NHhomeconstruction/) ·
[Instagram](https://www.instagram.com/nhivoryhome_/) ·
[TikTok](https://www.tiktok.com/@nhivoryhome_) ·
[YouTube](https://www.youtube.com/@NHIVORYHOMESDNBHD) ·
[Telegram](https://t.me/+UbHbsPCZ6D7qQTLB)

## Struktur Fail

```
index.html              Landing page penuh (semua section funnel)
thankyou.html           Halaman selepas hantar borang (conversion page)
404.html                Halaman ralat
robots.txt              Arahan crawler
sitemap.xml             Peta laman (dijana automatik)

kawasan/index.html      Hub senarai kawasan perkhidmatan
blog/index.html         Hub senarai artikel
bina-rumah-<lokasi>/    10 halaman lokasi (Ipoh, Seri Iskandar, Taiping, ...)
blog/<slug>/            4 artikel panduan

css/style.css           Tema merah, responsive mobile-first
css/seo.css             Styling halaman kandungan (lokasi & blog)
js/main.js              Header, menu, sticky CTA, kalkulator, video, widget WhatsApp
js/form.js              Validasi borang, hantar email, sambung WhatsApp
tools/generate-pages.py Penjana halaman lokasi & blog
google-apps-script.js   (Pilihan) simpan lead ke Google Sheets
assets/                 Ikon, imej ganti, OG image
images/                 Logo, gambar projek, pasukan, thumbnail video
```

## Halaman SEO (Lokasi & Blog)

### Halaman Lokasi (10)
`bina-rumah-ipoh/` · `bina-rumah-seri-iskandar/` · `bina-rumah-batu-gajah/` ·
`bina-rumah-kampar/` · `bina-rumah-kuala-kangsar/` · `bina-rumah-taiping/` ·
`bina-rumah-manjung/` · `bina-rumah-teluk-intan/` · `bina-rumah-kedah/` ·
`bina-rumah-penang/`

Setiap halaman mengandungi: pengenalan unik, pengetahuan tempatan (pihak berkuasa
tempatan, keadaan tanah, projek sebenar), senarai kawasan, FAQ khusus lokasi,
borang, dan pautan ke kawasan berdekatan.

### Artikel Blog (4)
- `blog/kos-bina-rumah-perak-2026/`
- `blog/panduan-loan-bina-rumah/`
- `blog/cara-mohon-lppsA-bina-rumah/`
- `blog/pelan-rumah-banglo-3-bilik/`

### Cara Tambah / Kemas Kini Halaman

Semua halaman lokasi & blog dijana daripada satu fail data. Untuk tambah kawasan
atau artikel baharu:

1. Buka `tools/generate-pages.py`
2. Tambah satu entri ke dalam senarai `LOCATIONS` atau `POSTS`
3. Jalankan:

```bash
python3 tools/generate-pages.py
```

Ini akan menjana semula semua halaman, hub, dan `sitemap.xml` secara automatik.

## Susunan Funnel

1. Hero + CTA "Konsultasi Percuma" (harga mula, 2000++ pelanggan, CIDB/MOF/SSM)
2. Tentang Kami (bumiputera, Seri Iskandar, sejak 2020, badge SSM/CIDB/MOF)
3. Masalah pelanggan (kontraktor lari duit, kos naik, lewat siap, kelulusan rumit)
4. Kenapa NH Ivory Home (6 value prop)
5. Pakej & Harga (Rumah Sederhana / Banglo Moden / Banglo 2 Tingkat)
6. Tunai · Loan Bank · LPPSA + kalkulator ansuran
7. Proses 5 langkah
8. Projek terkini (gambar sebenar) + testimoni + link Google Reviews
9. Video testimoni (4 video YouTube sebenar — klik untuk main)
10. FAQ
11. Borang ringkas (nama, no. WhatsApp, lokasi) → terus ke WhatsApp + email
12. Butang WhatsApp terapung beranimasi + popup pertanyaan

## Borang Ringkas

Borang hanya meminta **3 maklumat**: Nama, No. WhatsApp, Lokasi Tanah.

Bila dihantar:
1. Data dihantar ke email `azrisaadproperties@gmail.com` (CC `azrimdsaad@gmail.com`) melalui FormSubmit
2. Pelayar terus dibuka ke WhatsApp `601163364664` dengan mesej pra-isi lengkap
3. Event `Lead` dipicu untuk Meta Pixel / GA4

Butang WhatsApp terapung (kanan bawah) juga membuka **popup pertanyaan** dengan borang ringkas yang sama,
lengkap dengan animasi pulse, bobbing dan label "Tanya kami".

## Setup Pantas

### 1. Isi baki butiran
Buka `index.html` dan `thankyou.html`, cari objek `window.NH_CONFIG` di bahagian `<head>`:

```js
window.NH_CONFIG = {
  companyName: "NH Ivory Home Sdn. Bhd.",
  whatsapp: "601163364664",                      // borang & butang WhatsApp
  formEndpointB64: "aHR0cHM6...",                // endpoint borang (base64)
  formCcB64: "YXpyaW1k...",                      // CC (base64)
  appsScriptUrl: "",                             // pilihan
  metaPixelId: "{{META_PIXEL_ID}}",              // kosongkan jika tiada
  ga4Id: "{{GA4_ID}}",                           // kosongkan jika tiada
  thankyouUrl: "thankyou.html"
};
```

> **Nota privasi:** endpoint borang disimpan dalam bentuk **base64** (`formEndpointB64`,
> `formCcB64`) dan menggunakan **alias rawak FormSubmit** — jadi email sebenar anda
> **tidak kelihatan langsung** dalam kod, walaupun repo ini public.

Cara encode URL/email anda sendiri ke base64:

```bash
python3 -c "import base64;print(base64.b64encode(b'https://formsubmit.co/ajax/ALIAS_ANDA').decode())"
```

### 2. Aktifkan email borang (SUDAH SELESAI)
FormSubmit telah diaktifkan. Alias rawak `a8db721255fce02107f5373b1b0e5da9` digunakan
untuk menghantar lead ke email tujuan, dengan CC ke `azrimdsaad@gmail.com`.

> Jika alamat email bertukar: cipta alias baharu, tukar `FORM_B64` dalam
> `tools/generate-pages.py` dan `formEndpointB64` dalam `index.html`, kemudian jalankan
> `python3 tools/generate-pages.py`.

### 3. (Pilihan) Simpan lead ke Google Sheets
Ikut arahan di dalam `google-apps-script.js`, kemudian tampal URL `/exec` ke `appsScriptUrl`.
Jika dibiarkan kosong, borang tetap berfungsi (email + WhatsApp sahaja).

### 4. Ganti gambar
Gambar sebenar syarikat telah dimuat turun ke `images/`. Ganti bila-bila masa dengan
gambar beresolusi lebih tinggi menggunakan nama fail yang sama.

### 5. Video testimoni
4 video YouTube sebenar telah dipasang dengan teknik *click-to-play* (iframe hanya
dimuatkan apabila diklik, jadi laman kekal laju). Untuk tukar video, edit `data-video-id`
pada setiap `.video-card` dalam `index.html` dan ganti thumbnail `images/video-<id>.jpg`.

| Video | Pelanggan | Lokasi |
|---|---|---|
| `3b99AdeMBm0` | Pn Hasmah & Tn Noor Azli | Banglo Purewhite · Teluk Intan |
| `LQ4S8xInyRo` | Pn Nadia & Tn Huzaime | Banglo Stellar · Beruas |
| `dQCfAOQyIXU` | Tn Alias & Isteri | Banglo Amaya · Chemor |
| `hFpAzdWM1x8` | Pn Hjh Aishah & Tn Hj Saiful | Banglo Audela · Batu Gajah |

### 6. Testimoni & Google Reviews
Seksyen testimoni memaparkan **rating 4.9/5 daripada 36 review Google** dan 4 review
sebenar dari profil Google Business NH Ivory Home:

| Pengulas | Bintang | Bila |
|---|---|---|
| Muzi Darwish | 5 | 4 bulan lalu |
| Sinarto Khiron | 5 | Setahun lalu |
| Akmal Harith Azhar (Local Guide) | 5 | Setahun lalu |
| Ira Syira | 5 | Sebulan lalu |

Untuk menambah/mengemas kini review, edit blok `<article class="card google-review">`
dalam `index.html` (di dalam seksyen `#projek`).

## Placeholder Yang Masih Perlu Diisi

| Placeholder | Keterangan |
|---|---|
| `{{META_PIXEL_ID}}` | ID Meta Pixel untuk tracking iklan |
| `{{GA4_ID}}` | ID Google Analytics 4 |
| `{{DOMAIN_ANDA}}` | Domain laman (untuk Open Graph) |
| `{{MASA_RESPON}}` | Masa respons kepada lead (contoh: "30 minit") |
| `{{HARGA_BANGLO}}` | Harga anggaran banglo moden (contoh: RM250,000) |
| `{{HARGA_2TINGKAT}}` | Harga anggaran banglo 2 tingkat |

> **Perhatian:** Harga permulaan dipaparkan sebagai **RM13X,000** mengikut laman web
> rasmi syarikat. Sila sahkan angka sebenar sebelum kempen iklan dijalankan.

## Tracking
- Event `PageView` — setiap lawatan
- Event `Lead` — dihantar dari `form.js` apabila borang atau popup dihantar
- Event `Contact` — klik butang WhatsApp terapung / popup / sticky
- Event `InitiateCheckout` — klik CTA pakej / tunai / loan / LPPSA
- Event `ViewContent` — video testimoni dimainkan

> `thankyou.html` dikekalkan sebagai halaman pilihan (tidak digunakan dalam aliran
> semasa kerana borang terus membuka WhatsApp).

## Ujian Tempatan

```bash
python3 -m http.server 8080
```

Kemudian buka `http://localhost:8080`.

## SEO — Apa Yang Sudah Dipasang

| Item | Status |
|---|---|
| Title & meta description dioptimum | ✅ |
| Canonical URL | ✅ |
| `robots.txt` (thankyou.html disekat) | ✅ |
| `sitemap.xml` (termasuk imej & video) | ✅ |
| Structured data `GeneralContractor` (NAP, geo, areaServed, SSM/CIDB, rating) | ✅ |
| Structured data `FAQPage` (7 soalan) | ✅ |
| Structured data `VideoObject` (4 video) | ✅ |
| Open Graph + Twitter Card + og:image mutlak | ✅ |
| Meta geo (MY-08, koordinat) | ✅ |
| Alt text pada semua imej | ✅ |
| Preload hero + `fetchpriority=high` | ✅ |
| Responsive mobile-first + HTTPS | ✅ |

## SEO — Tugasan Manual (PALING PENTING)

### 1. Google Search Console
1. Buka https://search.google.com/search-console
2. Tambah property jenis **URL prefix**: `https://azrisaadproperties.github.io/nh-ivory-home/`
3. Sahkan pemilikan (paling mudah: **HTML tag** — tampal tag dalam `<head>` `index.html`)
4. **Sitemaps** → hantar `sitemap.xml`
5. **URL Inspection** → masukkan URL laman → **Request Indexing**

### 2. Google Business Profile (paling berkesan untuk "kontraktor bina rumah Perak")
- Pastikan profil di https://business.google.com lengkap 100%
- Kategori: **General Contractor** / **Home Builder**
- Isi kawasan perkhidmatan: Perak, Kedah, Pulau Pinang
- Muat naik 20+ gambar projek & video
- **Kumpul review setiap bulan** — ini penyumbang ranking #1 untuk carian tempatan
- Balas setiap review (Google suka ini)
- Buat post mingguan (projek siap, tip bina rumah)

### 3. Custom Domain (wajib untuk SEO serius)
Sub-folder `github.io` lemah untuk SEO. Beli domain dan tukar `canonical`, `og:url`,
`robots.txt`, `sitemap.xml`, dan semua URL dalam JSON-LD.

### 4. Kandungan (ini yang akan rank)
Satu landing page sahaja **tidak akan rank** untuk kata kunci komersial. Perlu halaman sokongan:

- `/bina-rumah-ipoh/`
- `/bina-rumah-taiping/`
- `/bina-rumah-kuala-kangsar/`
- `/bina-rumah-seri-iskandar/`
- `/bina-rumah-manjung/`
- `/bina-rumah-kedah/`
- `/bina-rumah-penang/`
- Blog: "Berapa Kos Bina Rumah Di Perak 2026?", "Panduan Loan Bina Rumah", "Cara Mohon LPPSA", "Pelan Rumah Banglo 3 Bilik"

Setiap halaman: 800–1500 patah perkataan, unik, + CTA + borang.

### 5. Backlink & sitasi tempatan
- Daftar di direktori kontraktor Malaysia (CIDB, MOF, Yellow Pages MY, Foursquare)
- Konsistenkan NAP (Nama, Alamat, Telefon) di semua tempat
- Artikel/guest post di portal hartanah
- Pastikan pautan dari laman rasmi `nhivoryhome.com.my` ke laman ini

### Realiti SEO
- SEO ambil masa **3–6 bulan** untuk nampak hasil
- Untuk lead **segera**, kekalkan Meta/Google Ads
- SEO + Ads = strategi terbaik (SEO turunkan kos lead jangka panjang)

## Deploy Ke GitHub Pages

Laman ini sudah disediakan untuk GitHub Pages:

- `.nojekyll` — halang GitHub memproses fail dengan Jekyll
- `404.html` — halaman ralat yang membawa pengunjung balik ke laman utama
- Semua laluan fail adalah **relatif**, jadi ia berfungsi walaupun dihoskan di sub-folder
  (`username.github.io/nama-repo/`)

### Langkah

```bash
# 1. Cipta repo di GitHub (contoh: nh-ivory-home)
gh repo create nh-ivory-home --public --source=. --remote=origin

# 2. Commit & push
git add .
git commit -m "Laman web sales funnel NH Ivory Home"
git push -u origin main
```

Kemudian di GitHub:

1. Buka repo → **Settings** → **Pages**
2. Di bawah **Build and deployment** → **Source**, pilih **Deploy from a branch**
3. **Branch**: `main` · **Folder**: `/ (root)` → **Save**
4. Tunggu 1–2 minit. Laman akan hidup di `https://<username>.github.io/nh-ivory-home/`

### Domain sendiri (disyorkan untuk iklan)

1. Beli domain (contoh: `nhivoryhome-lead.com`)
2. Di GitHub **Pages** → **Custom domain**, taip domain anda → **Save**
3. Di penyedia domain, tambah rekod DNS:

   | Jenis | Nama | Nilai |
   |---|---|---|
   | A | @ | 185.199.108.153 |
   | A | @ | 185.199.109.153 |
   | A | @ | 185.199.110.153 |
   | A | @ | 185.199.111.153 |
   | CNAME | www | `<username>.github.io` |

4. Tunggu DNS propagate, kemudian tanda **Enforce HTTPS**

### Selepas deploy

- Ganti `{{DOMAIN_ANDA}}` dalam `index.html` dengan domain sebenar
- Endpoint borang sudah guna **alias rawak FormSubmit** — email anda tidak kelihatan dalam kod
  (sudah dilaksanakan)
- Uji hantar borang sebenar dan pastikan email + WhatsApp berfungsi

## Platform Lain
Netlify, Cloudflare Pages, Vercel atau hosting cPanel — semua fail boleh dimuat naik
terus tanpa proses build.
