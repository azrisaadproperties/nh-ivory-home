# Panduan Kemas Kini Laman Web

Laman web ini dihoskan di **GitHub Pages**. Setiap kali anda simpan perubahan,
laman akan dikemas kini secara automatik dalam **1–2 minit**.

- **Laman live:** https://azrisaadproperties.github.io/nh-ivory-home/
- **Repositori:** https://github.com/azrisaadproperties/nh-ivory-home

---

## Kaedah A — Guna GitHub terus (tanpa install apa-apa)

Paling mudah. Hanya perlu buka GitHub di browser.

1. Buka https://github.com/azrisaadproperties/nh-ivory-home
2. Klik fail yang mahu diubah (contoh: `index.html`)
3. Klik ikon **pensel (✏️ Edit this file)** di kanan atas
4. Buat perubahan anda
5. Skrol ke bawah → tulis nota ringkas (contoh: "Tukar nombor WhatsApp")
6. Klik **Commit changes**
7. Tunggu 1–2 minit → buka laman web → tekan **Cmd + Shift + R** untuk refresh

---

## Kaedah B — Minta AI (opencode) buat

Beritahu sahaja apa yang perlu diubah, contoh:

> "Tukar harga Banglo Moden jadi RM250,000"
> "Tambah halaman lokasi Bagan Serai"
> "Tukar gambar hero"

AI akan edit, test, dan push sendiri.

---

## Kaedah C — Di komputer sendiri (untuk test dahulu)

```bash
# 1. Dapatkan versi terkini
cd "web design"
git pull

# 2. Test di komputer
python3 -m http.server 8080
# buka http://localhost:8080

# 3. Selepas puas hati, hantar ke live
git add .
git commit -m "nota perubahan"
git push
```

---

## Perkara Yang Selalu Diubah

### 1. Nombor WhatsApp
Fail: `index.html` — cari `window.NH_CONFIG` di bahagian atas:

```js
whatsapp: "601163364664",   // <-- tukar di sini (format 60...)
```

Nombor untuk **paparan** pula ada di beberapa tempat — cari `011-6336 6464` dan ganti semua.

### 2. Harga Pakej
Fail: `index.html` — cari `id="pakej"`:

```html
<p class="price"><span>RM13X,000</span></p>
```

Ganti dengan harga sebenar. Jika tiada angka, kekalkan `Sebut Harga`.

### 3. Gambar
Letak gambar baharu ke dalam folder `images/` dengan **nama fail yang sama**,
contoh `images/projek-5035.webp`. Tidak perlu ubah kod.

| Fail | Kegunaan |
|---|---|
| `images/logo.png` | Logo di header & footer |
| `images/projek-*.webp` | Gambar projek |
| `images/video-*.jpg` | Thumbnail video |
| `assets/og-image.webp` | Gambar pratonton bila link dikongsi |

### 4. Teks di halaman utama
Fail: `index.html` — cari seksyen berkenaan:

| Seksyen | Cari |
|---|---|
| Hero | `id="hero"` |
| Tentang Kami | `id="tentang"` |
| Pakej & Harga | `id="pakej"` |
| Tunai / Loan / LPPSA | `id="loan"` |
| Projek & Testimoni | `id="projek"` |
| Video | `id="video"` |
| Kawasan | `id="kawasan"` |
| FAQ | `id="faq"` |
| Borang | `id="borang"` |

### 5. Testimoni Google
Fail: `index.html` — cari `class="card google-review"`.

### 6. Tambah Halaman Lokasi / Artikel Blog
Fail: `tools/generate-pages.py`

1. Cari senarai `LOCATIONS` (untuk kawasan) atau `POSTS` (untuk artikel)
2. Salin satu blok sedia ada dan ubah isinya
3. Jalankan:

```bash
python3 tools/generate-pages.py
```

Semua halaman dan `sitemap.xml` akan dijana semula secara automatik.

### 7. Meta Pixel & Google Analytics
Fail: `index.html` — cari:

```js
metaPixelId: "{{META_PIXEL_ID}}",   // ganti dengan ID Meta Pixel
ga4Id: "{{GA4_ID}}",                // ganti dengan ID GA4
```

Untuk halaman lokasi/blog, jalankan semula `tools/generate-pages.py` selepas
mengedit nilai di dalam fail penjana (cari `META_PIXEL_ID` di `tools/generate-pages.py`).

---

## Jika Laman Tidak Dikemas Kini

1. Tunggu 2–3 minit lagi (GitHub perlu masa rebuild)
2. Tekan **Cmd + Shift + R** (Mac) atau **Ctrl + Shift + R** (Windows) untuk hard refresh
3. Semak status deploy:
   ```bash
   gh api "repos/azrisaadproperties/nh-ivory-home/pages/builds/latest" --jq '.status, .commit'
   ```
   Status sepatutnya `built`.

---

## Perkara Penting

- **Jangan** padam fail `.nojekyll` — ia diperlukan untuk GitHub Pages
- **Jangan** tukar nama fail secara rawak — pautan akan rosak
- Setiap `git push` = laman live dikemas kini secara automatik
- Simpan salinan gambar asal beresolusi tinggi di luar repo (backup)
