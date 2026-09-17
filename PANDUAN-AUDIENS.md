# Panduan Audiens Meta Ads — NH Ivory Home

> Penjelasan apa itu "audiens", 3 jenis audiens, dan cara guna data anda sendiri
> untuk turunkan kos iklan.

---

## 1. APA ITU "AUDIENS"?

**Audiens = siapa yang akan nampak iklan anda.**

Dalam Meta Ads, anda pilih audiens di peringkat **Ad Set** (bukan Campaign, bukan Ad).

```
Kempen (Campaign)     → tetapkan objektif & bajet
  └── Ad Set          → tetapkan AUDIENS, lokasi, umur, penempatan  ← di sini
        └── Ad        → kreatif (gambar/video) & teks
```

---

## 2. TIGA JENIS AUDIENS

| Jenis | Apa | Contoh untuk anda |
|---|---|---|
| **1. Saved Audience** | Anda set manual: lokasi, umur, minat | Perak, 30–60, minat "Hartanah" |
| **2. Custom Audience** | Dari **data anda sendiri** | Senarai pelanggan refinance anda |
| **3. Lookalike Audience** | Orang **serupa** dengan Custom Audience | 1% penduduk Malaysia yang paling serupa dengan pelanggan anda |

> **Keutamaan kos (murah → mahal):**
> Custom Audience (paling murah) → Lookalike → Saved Audience (broad)

---

## 3. APA YANG SAYA MAKSUD — 3 CADANGAN

### A. "Guna audiens Property & Tanah yang murah"

**Maksud:** salin setting targeting dari kempen anda yang **sudah terbukti murah**
(Property & Refinance RM6.06, TANAH CHANGKAT JERING RM3.27) — jangan reka audiens baharu.

**Cara paling mudah — DUPLICATE:**

1. Buka **Ads Manager**
2. Cari kempen `Property & Refinance 15/9/26 - 01` (yang RM6.06)
3. Tanda kotak di sebelahnya
4. Klik **Duplicate**
5. Buka kempen salinan itu → tukar:
   - **Nama** → `[LEAD] Bina Rumah — Perak`
   - **Kreatif** → gambar/video bina rumah
   - **Teks** → tawaran "Ada tanah? Kami bina."
   - **Destinasi** → WhatsApp
6. **Jangan tukar audiens** — biar sama
7. Publish

> **Kenapa:** audiens itu sudah terbukti murah. Kalau anda tukar, anda mula dari kosong.

**Cara manual (kalau nak tahu settingnya):**
1. Buka kempen → klik **Ad Set**
2. Lihat bahagian **Audience**
3. Catat: Lokasi, Umur, Jantina, Detailed targeting, Exclusions
4. Bila buat kempen baharu, isi setting yang sama

---

### B. Custom Audience dari senarai pelanggan anda

Ini **aset paling bernilai** yang anda ada — dan kontraktor biasa tiada.

**Kenapa berkesan:** orang yang sudah pernah berurusan dengan anda
(property, refinance) lebih mudah percaya dan beli.

#### Langkah 1 — Sediakan senarai
Buat fail Excel/CSV dengan 2 lajur:

| phone | email |
|---|---|
| 60123456789 | ali@gmail.com |
| 60198887777 | siti@gmail.com |

> **Nota format telefon:** guna kod negara tanpa `+` atau `0` di depan.
> Contoh: `60123456789` (bukan `0123456789`, bukan `+60123456789`)

#### Langkah 2 — Upload ke Meta
1. Buka **business.facebook.com/audiences**
2. Klik **Create Audience** → **Custom Audience**
3. Pilih **Customer List**
4. Klik **Next**
5. Namakan: `Pelanggan Refinance — [bulan/tahun]`
6. Upload fail CSV anda
7. Meta akan **padankan** nombor/email dengan akaun Facebook mereka
8. Klik **Upload & Create**

> **Penting:** Meta tidak dedahkan siapa dalam senarai anda. Ia hanya padankan
> secara automatik (privasi dilindungi).

#### Langkah 3 — Guna
Bila buat kempen baharu, di bahagian **Audience**:
- Pilih **Custom Audiences** → `Pelanggan Refinance`
- Ini akan sasarkan orang yang **sudah kenal anda**

**Cadangan:** guna audiens ini untuk **retargeting** tawaran "bina rumah kedua"
(keluarkan ekuiti rumah untuk bina).

---

### C. Lookalike 1% — cari orang SERUPA pelanggan anda

**Maksud:** Meta cari orang di Malaysia yang **ciri-cirinya paling serupa**
dengan senarai pelanggan anda.

#### Syarat
- Custom Audience anda perlu ada **sekurang-kurangnya 100 orang** yang dipadankan
- Lebih besar senarai, lebih tepat Lookalike

#### Langkah
1. Buka **business.facebook.com/audiences**
2. Klik **Create Audience** → **Lookalike Audience**
3. **Source:** pilih `Pelanggan Refinance — [bulan/tahun]`
4. **Country:** Malaysia
5. **Audience size:** **1%** (paling serupa; 2–3% lebih luas tetapi kurang tepat)
6. Klik **Create Audience**

#### Cara guna
Di Ad Set → Audience → **Custom Audiences** → pilih `Lookalike (MY, 1%) — Pelanggan Refinance`

> **Cadangan:** mula dengan 1%. Kalau audiens terlalu kecil (reach rendah),
> naik ke 2–3%.

---

## 4. AUDIENS LAIN YANG ANDA BOLEH BUAT (PERCUMA)

Semua ini dibina **automatik** oleh Meta Pixel & engagement — tiada upload perlu:

| Custom Audience | Syarat | Guna untuk |
|---|---|---|
| **Pelawat laman web 30 hari** | Perlu Meta Pixel | Retargeting — orang yang lihat tapi tak isi borang |
| **Tonton video 50%** | Perlu iklan video | Retargeting minat |
| **Engagement Page/IG 365 hari** | Ada Page | Retargeting hangat |
| **Orang hantar borang** | Perlu Pixel event `Lead` | **EXCLUDE** dari retargeting |
| **Pembeli/klien lama** | Upload senarai | Lookalike + cross-sell |

> **Meta Pixel belum dipasang** — jadi audiens laman web belum boleh dibuat.
> Pasang esok, kemudian bina audiens ini.

---

## 5. STRUKTUR AUDIENS YANG DISYORKAN

```
Kempen: [LEAD] Bina Rumah — Perak
│
├── Ad Set 1: Lookalike 1% — Pelanggan Refinance     ← paling panas
├── Ad Set 2: Interest Tanah/Hartanah + Perak        ← saved audience
├── Ad Set 3: Broad Perak (30–60)                    ← biar Meta cari sendiri
└── Ad Set 4: Penjawat Awam (LPPSA)                  ← segmen khas

Kempen: [RETARGET] Bina Rumah
│
├── Ad Set 1: Pelawat laman 30 hari (EXCLUDE yang isi borang)
├── Ad Set 2: Tonton video 50%
└── Ad Set 3: Engagement Page/IG 365 hari
```

---

## 6. KESILAPAN BIASA

| Kesilapan | Betulkan |
|---|---|
| Tukar audiens pada kempen yang sudah menang | **Jangan** — duplicate dan tukar kreatif sahaja |
| Upload senarai tanpa format betul | Guna `60123456789`, bukan `0123456789` |
| Guna Lookalike 10% (terlalu luas) | Mula 1%, naik jika perlu |
| Tak exclude yang sudah isi borang | Buat Custom Audience "Lead" dan **exclude** |
| Campur semua segmen dalam 1 ad set | Pisahkan: tunai / loan / LPPSA |
| Reka audiens baharu setiap kali | Guna yang sudah terbukti murah |

---

## 7. RINGKASAN

| Perkara | Jawapan |
|---|---|
| Apa itu audiens? | Siapa yang nampak iklan anda |
| Set di mana? | **Ad Set** (bukan Campaign, bukan Ad) |
| "Guna audiens Property & Tanah" | **Duplicate** kempen yang murah, tukar kreatif sahaja |
| Custom Audience | Upload senarai pelanggan (telefon/email) ke Meta |
| Lookalike 1% | Meta cari orang serupa pelanggan anda |
| Aset anda | Senarai pelanggan refinance & property — kontraktor biasa tiada |
| Perlu pixel? | Untuk audiens laman web — ya (pasang esok) |
