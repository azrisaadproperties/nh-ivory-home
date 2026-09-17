# RINGKASAN PROJEK — Laman Web NH Ivory Home Sdn. Bhd.

> Dokumen ini untuk dijadikan konteks / arahan dalam Gemini Gem (atau AI assistant lain).
> Ia menerangkan projek secara menyeluruh supaya AI boleh membantu mengemas kini laman web ini.

---

## 1. KONTEKS BISNES

| Perkara | Nilai |
|---|---|
| Nama Syarikat | **NH Ivory Home Sdn. Bhd.** |
| No. Syarikat (SSM) | `20200101283 (1369193-H)` |
| Lesen CIDB | `G4 · 0120210118-WP066824` |
| MOF | Berdaftar |
| Beroperasi sejak | 02 Jun 2020 |
| Ibu Pejabat | No 70A, Persiaran SIBC 4, Bandar Seri Iskandar, 32610 Seri Iskandar, Perak |
| Kawasan perkhidmatan | Perak, Kedah, Pulau Pinang |
| Perkhidmatan | Bina rumah & banglo atas tanah sendiri |
| Kaedah bayaran | Tunai, Loan Bank, LPPSA |
| Harga mula | RM13X,000 (angka rasmi dipaparkan bertopeng oleh syarikat) |
| Reka bentuk | 100+ pilihan |
| Pelanggan | 2000++ |
| Rating Google | 4.9 / 5 (36 review) |
| Sosial | FB `NHhomeconstruction` · IG `nhivoryhome_` · TikTok `nhivoryhome_` · YouTube `@NHIVORYHOMESDNBHD` |

**Projek sebenar yang dirujuk di laman:** Chemor, Desa Seri Iskandar, Lambor Kanan, Beruas, Manjung, Kuala Kangsar, Manong, Tanjung Tualang, Batu Gajah, Teluk Intan.

**Video testimoni sebenar (YouTube):**
- `3b99AdeMBm0` — Pn Hasmah & Tn Noor Azli · Banglo Purewhite · Teluk Intan
- `LQ4S8xInyRo` — Pn Nadia & Tn Huzaime · Banglo Stellar · Beruas
- `dQCfAOQyIXU` — Tn Alias & Isteri · Banglo Amaya · Chemor
- `hFpAzdWM1x8` — Pn Hjh Aishah & Tn Hj Saiful · Banglo Audela · Batu Gajah

---

## 2. PERANAN & TUJUAN LAMAN

Laman ini ialah **sales funnel** untuk menjana lead pemilik tanah yang mahu membina rumah.

**Aliran funnel:**
```
Iklan (Meta/Google) → Landing Page → Baca offer → Isi borang 3 medan
→ Email + CC ke sales → WhatsApp terbuka dengan mesej pra-isi → Appointment
```

**Sasaran:** pemilik tanah di Perak/Kedah/Penang yang mahu bina rumah secara **tunai** atau **loan/LPPSA**.

**Pemilik projek:** pasukan jualan (bukan syarikat induk). Nombor WhatsApp & email adalah milik pasukan jualan.

---

## 3. URL & HOSTING

| Perkara | Nilai |
|---|---|
| Laman live | `https://azrisaadproperties.github.io/nh-ivory-home/` |
| Repositori | `https://github.com/azrisaadproperties/nh-ivory-home` (PUBLIC) |
| Hosting | GitHub Pages (branch `main`, folder `/`) |
| Deploy | Auto — setiap `git push`, live dalam 1–2 minit |
| HTTPS | Ya (enforced) |
| Platform alternatif | Cloudflare Pages, Netlify, Vercel, cPanel |

**Fail penting hosting:** `.nojekyll` (JANGAN padam), `404.html`.

---

## 4. TEKNOLOGI & ARSITEKTUR

- **Static HTML + CSS + JavaScript** — tiada framework, tiada build step, tiada npm
- Semua laluan fail **relatif** (berfungsi di sub-folder GitHub Pages)
- Mobile-first responsive
- Deploy = upload fail sahaja

**Pilihan dibuat:** static HTML dipilih supaya laju, murah, mudah deploy, dan tiada dependency.

---

## 5. STRUKTUR FAIL

```
index.html                    Landing page utama (funnel penuh)
thankyou.html                 Halaman selepas hantar borang (noindex)
404.html                      Halaman ralat (self-contained, inline CSS)
robots.txt                    Arahan crawler + rujukan sitemap
sitemap.xml                   Dijana automatik (17 URL)
google757db01ceb8d45b9.html   Fail verification Google Search Console

kawasan/index.html            Hub senarai kawasan
blog/index.html               Hub senarai artikel
bina-rumah-<lokasi>/index.html   10 halaman lokasi
blog/<slug>/index.html           4 artikel blog

css/style.css                 Tema utama (semua halaman)
css/seo.css                   Styling halaman kandungan (lokasi & blog)
js/main.js                    Header, menu, sticky CTA, kalkulator, video, widget WhatsApp, tracking
js/form.js                    Validasi borang, hantar email, redirect WhatsApp
tools/generate-pages.py       Penjana halaman lokasi & blog + sitemap
google-apps-script.js         (Pilihan) simpan lead ke Google Sheets
assets/                       favicon.svg, placeholder.svg, og-image.webp
images/                       logo.png, projek-*.webp, staff.webp, video-*.jpg
PANDUAN-KEMASKINI.md          Panduan kemas kini untuk pasukan
PANDUAN-TRACKING.md           Panduan Meta Pixel & GA4
README.md                     Dokumentasi teknikal
```

**10 halaman lokasi:** `bina-rumah-ipoh`, `bina-rumah-seri-iskandar`, `bina-rumah-batu-gajah`, `bina-rumah-kampar`, `bina-rumah-kuala-kangsar`, `bina-rumah-taiping`, `bina-rumah-manjung`, `bina-rumah-teluk-intan`, `bina-rumah-kedah`, `bina-rumah-penang`

**4 artikel blog:** `kos-bina-rumah-perak-2026`, `panduan-loan-bina-rumah`, `cara-mohon-lppsA-bina-rumah`, `pelan-rumah-banglo-3-bilik`

---

## 6. KONFIGURASI UTAMA (di `window.NH_CONFIG`)

Terdapat dalam `index.html`, `thankyou.html`, dan template `tools/generate-pages.py`.

```js
window.NH_CONFIG = {
  companyName: "NH Ivory Home Sdn. Bhd.",
  whatsapp: "601163364664",              // SEMUA butang & borang
  formEndpointB64: "aHR0cHM6Ly9mb3Jtc3VibWl0LmNvL2FqYXgvYThkYjcyMTI1NWZjZTAyMTA3ZjUzNzNiMWIwZTVkYTk=",
  formCcB64: "YXpyaW1kc2FhZEBnbWFpbC5jb20=",
  appsScriptUrl: "",
  metaPixelId: "",                       // BELUM dipasang
  ga4Id: "G-6J42DTSYZ3",
  thankyouUrl: "thankyou.html"
};
```

**Nilai sebenar (selepas decode):**

| Item | Nilai |
|---|---|
| WhatsApp | `601163364664` (paparan: 011-6336 6464) |
| Endpoint borang | `https://formsubmit.co/ajax/a8db721255fce02107f5373b1b0e5da9` (alias rawak) |
| Email tujuan | azrisaadproperties@gmail.com |
| CC | azrimdsaad@gmail.com |
| GA4 | `G-6J42DTSYZ3` |
| Google verification | `GJwS9dQq0-2aSVOIWlMJwETYgyzF4M3Vlk3kz-L7wO8` |
| Meta Pixel | belum ada |

**Pemalar dalam `tools/generate-pages.py`:** `WHATSAPP`, `FORM_B64`, `CC_B64`, `META_PIXEL_ID`, `GA4_ID`, `GOOGLE_VERIFICATION`, `SITE`, `PHONE_DISPLAY`.

---

## 7. SISTEM DESIGN

| Token | Nilai |
|---|---|
| Merah utama | `#C8102E` |
| Merah gelap | `#8E0B20` |
| Merah lembut | `#FDECEF` |
| Emas (aksen) | `#C9A227` |
| Gelap | `#1A1A1A` |
| Latar lembut | `#F7F7F8` |
| Garis | `#E5E7EB` |
| Heading font | Poppins (600/700/800) |
| Body font | Inter (400/500/600) |

Butang `.btn-primary` (merah), `.btn-outline` (merah garis), `.btn-wa` (hijau WhatsApp), `.btn-ghost`, `.btn-ghost-dark`.

---

## 8. SUSUNAN FUNNEL (index.html)

1. **Hero** — H1 "Bina Rumah Impian Di Atas Tanah Sendiri Anda", CTA, trust badges, gambar projek sebenar
2. **Tentang Kami** — syarikat bumiputera, Seri Iskandar, badge SSM/CIDB/MOF
3. **Masalah** — 4 ketakutan pelanggan (kontraktor lari duit, kos naik, lewat siap, kelulusan rumit)
4. **Kenapa Kami** — 6 value prop
5. **Pakej & Harga** — 3 kad (Rumah Sederhana / Banglo Moden / Banglo 2 Tingkat)
6. **Tunai · Loan Bank · LPPSA** — 3 kad + kalkulator ansuran
7. **Proses** — 5 langkah
8. **Projek & Testimoni** — 8 gambar projek sebenar + rating Google 4.9 + 4 review sebenar
9. **Video Testimoni** — 4 video YouTube (click-to-play)
10. **Kawasan** — pautan ke 10 halaman lokasi
11. **FAQ** — 7 soalan (accordion)
12. **Borang** — 3 medan sahaja
13. **Footer** + widget WhatsApp terapung

**ID seksyen:** `#hero` `#tentang` `#masalah` `#kenapa` `#pakej` `#loan` `#kalkulator` `#proses` `#projek` `#video` `#kawasan` `#faq` `#borang`

---

## 9. BORANG (PENTING)

**Hanya 3 medan:** Nama Penuh, No. WhatsApp, Lokasi Tanah.

**Aliran semasa hantar:**
1. Validasi (nama ≥3 aksara, telefon format Malaysia, lokasi ≥3 aksara)
2. Honeypot anti-bot (medan `website`)
3. Hantar ke FormSubmit (email + CC) — guna alias rawak, email tidak kelihatan dalam kod
4. Event `Lead` dipicu (Meta Pixel + GA4)
5. Redirect ke WhatsApp `601163364664` dengan mesej pra-isi (nama, no telefon, lokasi)
6. UTM parameter (utm_source/medium/campaign/content/term, fbclid, gclid) ditangkap dan dihantar

**Nota:** FormSubmit sudah **diaktifkan**. Jangan tukar endpoint melainkan perlu.

---

## 10. TRACKING

| Event | Bila | Fungsi |
|---|---|---|
| `PageView` | Setiap halaman | Kira trafik |
| `Lead` | Borang dihantar | **Conversion utama** |
| `Contact` | Klik WhatsApp / popup | Kira minat hubungi |
| `InitiateCheckout` | Klik CTA pakej/tunai/loan | Kira minat pakej |
| `ViewContent` | Video dimainkan | Kira minat kandungan |

Fungsi global: `window.nhTrack(namaEvent, params)` dalam `js/main.js`.
GA4 event name di-lowercase automatik.

---

## 11. SEO

**Setiap halaman ada:** title unik, meta description, canonical, Open Graph, Twitter Card, geo meta (MY-08), structured data.

**Structured data:** `GeneralContractor` (index), `FAQPage`, `VideoObject`, `Service` (lokasi), `BlogPosting` (blog), `BreadcrumbList`.

**Status Google:**
- Search Console: **terverifikasi** (kaedah HTML file)
- Sitemap: **dihantar & dibaca** (17 URL)
- GA4: **aktif**

---

## 12. PENJANA HALAMAN (tools/generate-pages.py)

Semua halaman lokasi, blog, hub, dan `sitemap.xml` dijana dari satu fail ini.

**Untuk tambah kawasan baharu:** tambah satu entri dalam senarai `LOCATIONS`
**Untuk tambah artikel:** tambah entri dalam senarai `POSTS`

Setiap entri lokasi ada: `slug`, `place`, `state`, `district`, `geo`, `title`, `desc`, `h1`, `intro`, `areas`, `sections`, `faqs`, `project_note`, `image`, `nearby`.

Setiap entri blog ada: `slug`, `title`, `desc`, `h1`, `category`, `date`, `date_display`, `reading`, `image`, `intro`, `blocks`, `faqs`, `related`.

Blok blog: `("h2", teks)`, `("p", teks)`, `("ul", [item])`, `("table", {head, rows})`, `("callout", teks)`.

**Selepas edit, jalankan:**
```bash
python3 tools/generate-pages.py
```

---

## 13. CARA KEMAS KINI

### Kaedah A — GitHub terus (tanpa tools)
1. Buka repo → klik fail → ikon pensel → edit → Commit changes
2. Tunggu 1–2 minit → hard refresh (Cmd+Shift+R)

### Kaedah B — Minta AI
Beritahu sahaja apa yang perlu diubah.

### Kaedah C — Komputer sendiri
```bash
git pull
# edit fail...
python3 -m http.server 8080   # test
git add . && git commit -m "nota" && git push
```

### Perubahan biasa
| Nak ubah | Fail | Cari |
|---|---|---|
| Nombor WhatsApp | `index.html` | `whatsapp:` |
| Harga pakej | `index.html` | `id="pakej"` |
| Gambar | folder `images/` | nama fail sama |
| Testimoni | `index.html` | `class="card google-review"` |
| Tambah lokasi/blog | `tools/generate-pages.py` | `LOCATIONS` / `POSTS` |
| Meta Pixel / GA4 | `tools/generate-pages.py` + `index.html` | pemalar di atas |

---

## 14. PERATURAN & LARANGAN

- **JANGAN** padam `.nojekyll`
- **JANGAN** tukar nama fail secara rawak (pautan akan rosak)
- **JANGAN** dedahkan email sebenar dalam kod — gunakan alias FormSubmit + base64
- **JANGAN** paparkan nombor telefon syarikat (019-813 1185 / 019-503 1185) — hanya nombor WhatsApp pasukan jualan
- **JANGAN** paparkan email syarikat (info@nhivoryhome.com.my)
- Semua kandungan dalam **Bahasa Melayu**
- Selepas edit `tools/generate-pages.py`, **mesti** jalankan penjana
- Selepas tambah halaman, **mesti** jana semula sitemap (penjana buat automatik)

---

## 15. TUGASAN BELUM SELESAI

| Tugasan | Status |
|---|---|
| Meta Pixel ID | Belum dipasang — perlu ID dari Meta Events Manager |
| Google Business Profile | Belum didaftarkan — paling berkesan untuk SEO tempatan |
| Domain sendiri | Belum — masih guna URL `github.io` |
| Harga sebenar pakej | Masih "Sebut Harga" / "RM13X,000" |
| Testimoni bertulis | Hanya review Google; belum ada testimoni khusus |

---

## 16. ARAHAN UNTUK AI

Apabila membantu projek ini:

1. **Sentiasa guna Bahasa Melayu** untuk kandungan laman
2. **Kekalkan tema merah** `#C8102E` + font Poppins/Inter
3. **Selepas edit penjana**, ingatkan untuk jalankan `python3 tools/generate-pages.py`
4. **Selepas apa-apa perubahan**, cadangkan `git add . && git commit && git push`
5. **Jangan reka fakta** — jika harga/testimoni tidak diberi, gunakan placeholder atau tanya
6. **Kekalkan struktur fail** dan laluan relatif
7. **Uji sebelum push** — sahkan HTML sah, pautan tidak rosak, JSON-LD sah
8. **Untuk kandungan SEO**, tulis 800–1500 patah perkataan, unik, ada pengetahuan tempatan sebenar
9. **Jangan dedahkan** email atau nombor telefon syarikat
10. **Nombor WhatsApp** sentiasa `601163364664`
