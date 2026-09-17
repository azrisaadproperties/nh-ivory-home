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

## 6. PENTING: DUPLICATE SAHAJA TIDAK CUKUP

> **Soalan yang betul:** kalau kreatif itu yang tarik minat audiens, apa gunanya
> duplicate kempen menang tetapi tukar kreatif?

Jawapannya: **anda betul — kreatif ialah pembolehubah terbesar.** Nasihat "duplicate
dan tukar kreatif" hanya sebahagian cerita. Ini penjelasan penuh.

### 6.1 Apa yang sebenarnya diwarisi bila duplicate

| Elemen | Diwarisi? | Nota |
|---|---|---|
| Lokasi, umur, jantina | ✅ Ya | Targeting |
| Interest / detailed targeting | ✅ Ya | Targeting |
| Custom / Lookalike audience | ✅ Ya | Targeting |
| Objective & optimization | ✅ Ya | Struktur |
| Penempatan (placement) | ✅ Ya | Struktur |
| **Kreatif** | ❌ **Tidak** | Anda tukar |
| **Tawaran (offer)** | ❌ **Tidak** | Anda tukar |
| Sejarah engagement iklan | ❌ Tidak | Mula dari kosong |

> **Kesimpulan:** anda hanya mewarisi **siapa** yang disasarkan — bukan **apa** yang
> membuatkan mereka berhenti scroll.

### 6.2 Jadi apa gunanya duplicate?

Ia **mengasingkan pembolehubah** (isolate variables).

```
Kempen asal  = Audien A × Kreatif X × Tawaran X  → RM6.06
Kempen baharu = Audien A × Kreatif Y × Tawaran Y  → ???
```

Anda sudah **tahu audien A murah**. Jadi bila anda tukar kreatif, anda tidak perlu
pening fikir audiens. Fokus pada kreatif & tawaran sahaja.

**Ini bukan jaminan murah** — ia hanya menghapuskan satu pembolehubah.

### 6.3 KENAPA kempen anda murah? (analisis)

Ini yang perlu difahami sebelum tiru apa-apa:

| Kempen | Kos | Tawaran | Spesifik? |
|---|---|---|---|
| TANAH CHANGKAT JERING | RM3.27 | Tanah untuk dijual | ✅ **Sangat spesifik** (lokasi tepat) |
| Property & Refinance 15/9 | RM6.06 | Perkhidmatan refinance | 🟡 Separuh |
| Agriculture Changkat Jering | RM7.29 | Tanah pertanian | ✅ Spesifik |
| Property & Refinance 17/9 | RM7.38 | Refinance | 🟡 Separuh |

**Pola:** kempen termurah adalah yang **spesifik + nyata + ada lokasi**.
Bukan iklan generik "kami ada perkhidmatan".

> **Pengajaran:** yang murah bukan audiens sahaja — tetapi **kombinasi**
> audiens + tawaran yang sangat spesifik.

### 6.4 Cara betul: TIRU FORMULA, bukan sekadar audiens

Jangan sekadar duplicate. **Tiru pola kreatif yang menang.**

| Iklan asal (murah) | Iklan bina rumah (tiru pola) |
|---|---|
| "TANAH CHANGKAT JERING" — lokasi tepat | "Bina Rumah Di Ipoh — Bermula RM13X,000" |
| Gambar tanah sebenar | Gambar tanah kosong → rumah siap |
| Harga/ukuran nyata | Harga nyata + saiz nyata |
| Nama tempat disebut | Nama kawasan disebut |

**Contoh kreatif yang meniru pola:**

```
❌ GENERIK (mahal):
"Kami kontraktor bina rumah. Hubungi kami."
→ Tiada lokasi, tiada harga, tiada kekhususan

✅ SPESIFIK (murah):
"Pemilik tanah di Ipoh — kami bina rumah anda bermula RM13X,000.
Lihat projek kami di Chemor dan Batu Gajah."
→ Ada lokasi, ada harga, ada bukti
```

### 6.5 Ujian yang betul (A/B)

Jangan andaikan. Uji secara terkawal:

| Ujian | Audien | Kreatif | Soalan |
|---|---|---|---|
| Ujian 1 | Sama | **Berbeza** | Kreatif mana lebih murah? |
| Ujian 2 | **Berbeza** | Sama | Audien mana lebih murah? |

**Ujian 1** — itulah yang anda buat bila duplicate kempen menang dan tukar kreatif.
Ini **sah** dan berguna, tetapi sedar ia menguji **kreatif**, bukan audiens.

> **Peraturan:** tukar **satu pembolehubah sahaja** setiap ujian. Kalau tukar
> audiens DAN kreatif sekali, anda tak akan tahu mana yang menyebabkan perbezaan.

### 6.6 Ringkasan seksyen ini

| Soalan | Jawapan |
|---|---|
| Adakah kreatif yang tarik minat? | **Ya** — ia pembolehubah terbesar |
| Jadi apa guna duplicate? | Ia mewarisi **targeting** yang sudah terbukti murah |
| Adakah ia jaminan? | **Tidak** — hanya menghapuskan 1 pembolehubah |
| Yang paling penting? | Faham **KENAPA** murah, kemudian **tiru formula** |
| Formula murah anda? | **Spesifik + lokasi nyata + harga nyata + bukti** |

---

## 7. KESILAPAN BIASA

| Kesilapan | Betulkan |
|---|---|
| Tukar audiens pada kempen yang sudah menang | **Jangan** — duplicate dan tukar kreatif sahaja |
| Upload senarai tanpa format betul | Guna `60123456789`, bukan `0123456789` |
| Guna Lookalike 10% (terlalu luas) | Mula 1%, naik jika perlu |
| Tak exclude yang sudah isi borang | Buat Custom Audience "Lead" dan **exclude** |
| Campur semua segmen dalam 1 ad set | Pisahkan: tunai / loan / LPPSA |
| Reka audiens baharu setiap kali | Guna yang sudah terbukti murah |

---

## 8. RINGKASAN

| Perkara | Jawapan |
|---|---|
| Apa itu audiens? | Siapa yang nampak iklan anda |
| Set di mana? | **Ad Set** (bukan Campaign, bukan Ad) |
| "Guna audiens Property & Tanah" | **Duplicate** kempen yang murah, tukar kreatif sahaja |
| Custom Audience | Upload senarai pelanggan (telefon/email) ke Meta |
| Lookalike 1% | Meta cari orang serupa pelanggan anda |
| Aset anda | Senarai pelanggan refinance & property — kontraktor biasa tiada |
| Perlu pixel? | Untuk audiens laman web — ya (pasang esok) |
