# Prompt Video AI (Google Flow / Veo) — Iklan 30 Saat

> **3 klip × 10 saat = 1 iklan lengkap 30 saat**
> Tema: **"Dari Tanah Kosong ke Rumah Impian"** — NH Ivory Home
>
> Setiap klip ada JSON prompt + prompt string (untuk tampal terus ke Flow) +
> teks skrin + voiceover + nota sambungan.

---

## SPESIFIKASI PROJEK

| Perkara | Nilai |
|---|---|
| Jumlah tempoh | 30 saat (3 × 10 saat) |
| Nisbah | **9:16** (menegak — Reels/Stories/TikTok) |
| Resolusi | 1080 × 1920 |
| Bahasa | Bahasa Melayu (voiceover & teks) |
| Lokasi cerita | Perak, Malaysia |
| Nada | Yakin, hangat, tempatan |
| Muzik | Instrumental lembut → bina ke emosi hangat |

### Struktur 30 saat

| Klip | Masa | Peranan | Emosi |
|---|---|---|---|
| **1** | 0–10s | HOOK + MASALAH | Risau, renung |
| **2** | 10–20s | PENYELESAIAN | Harapan, kerja |
| **3** | 20–30s | HASIL + CTA | Gembira, puas |

> **Nota penting:** AI video paling sesuai untuk **B-roll, pemandangan, transisi**.
> Untuk **testimoni pelanggan sebenar**, guna footage sebenar — bukan AI.

---

# KLIP 1 (0–10s) — HOOK + MASALAH

## JSON Prompt

```json
{
  "clip_id": 1,
  "title": "Tanah Kosong — Harapan",
  "duration_seconds": 10,
  "aspect_ratio": "9:16",
  "resolution": "1080x1920",
  "frame_rate": 24,

  "prompt_string": "Cinematic aerial drone shot slowly pushing forward over a large empty plot of flat land in rural Perak, Malaysia at golden morning light. Lush tropical vegetation, oil palm trees and distant limestone hills in the background. A lone middle-aged Malaysian Malay man in his 40s wearing a plain short-sleeve shirt stands at the edge of the land, looking out thoughtfully with hands on his hips, his back partially to camera. Soft warm sunlight, light morning mist, gentle breeze moving the grass. Shot on 35mm film, shallow depth of field, warm earthy color grading, documentary realism. Slow steady forward camera movement, no cuts.",

  "subject": "Middle-aged Malaysian Malay man (40s), plain shirt, standing at edge of empty land",
  "action": "Standing still, looking out at the land thoughtfully, slight breeze in clothing",
  "setting": "Empty flat plot of land, rural Perak Malaysia, oil palm trees, limestone hills, morning mist",
  "camera": {
    "movement": "Slow steady drone push-in, forward",
    "shot_type": "Wide aerial establishing shot",
    "lens": "35mm, shallow depth of field",
    "height": "Medium drone altitude, descending slightly"
  },
  "lighting": "Golden morning light, soft warm, gentle mist, low sun angle",
  "style": "Cinematic documentary realism, 35mm film look",
  "color_grading": "Warm earthy tones, soft greens and golds",
  "mood": "Contemplative, hopeful, slightly uncertain",
  "audio": {
    "ambient": "Morning birdsong, gentle wind through grass, distant insects",
    "music": "Soft solo piano, slow and reflective, low volume",
    "voiceover": null
  },

  "text_overlay": [
    {
      "time": "0.5s-4s",
      "text": "ADA TANAH SENDIRI?",
      "style": "Bold white text, large, center-top, subtle dark shadow",
      "animation": "Fade in with slight scale up"
    },
    {
      "time": "5s-9s",
      "text": "Tapi tak tahu macam mana nak mula?",
      "style": "Smaller white text, center-bottom, semi-transparent dark bar behind",
      "animation": "Slide up fade in"
    }
  ],

  "voiceover": {
    "language": "Bahasa Melayu",
    "script": "Ada tanah sendiri... tapi tak tahu macam mana nak mula bina?",
    "tone": "Tenang, empati, sedikit bertanya",
    "timing": "0.8s - 6s"
  },

  "negative_prompt": "text, watermark, logo, distorted faces, extra fingers, cartoon, anime, oversaturated, blurry, shaky camera, night, rain, snow"
}
```

## Nota sambungan ke Klip 2
- Klip berakhir dengan **kamera menghala ke tanah kosong**
- Klip 2 mula dengan **tanah yang sama, tetapi ada aktiviti pembinaan**
- Pastikan warna & waktu (pagi) sama

---

# KLIP 2 (10–20s) — PENYELESAIAN

## JSON Prompt

```json
{
  "clip_id": 2,
  "title": "Pembinaan — Kami Uruskan",
  "duration_seconds": 10,
  "aspect_ratio": "9:16",
  "resolution": "1080x1920",
  "frame_rate": 24,

  "prompt_string": "Cinematic construction site sequence in rural Perak, Malaysia. Same plot of land now under active construction. A single-storey modern bungalow structure is partially built with concrete columns, brick walls and roof trusses visible. Three Malaysian construction workers wearing safety helmets and high-visibility vests work steadily. One worker lays bricks, another checks a technical drawing, a third operates a small concrete mixer. Slow dynamic drone orbit around the structure at mid-height, revealing progress. Bright late-morning sunlight, clear blue sky, dust particles catching the light. Shot on 35mm film, warm natural color grading, documentary realism. Smooth continuous camera movement, no cuts.",

  "subject": "Malaysian construction workers (3), safety helmets, hi-vis vests, building a bungalow",
  "action": "Workers actively building — laying bricks, checking plans, mixing concrete",
  "setting": "Same land as Clip 1, now a construction site, single-storey bungalow frame, rural Perak",
  "camera": {
    "movement": "Slow drone orbit around structure, clockwise",
    "shot_type": "Medium-wide aerial, then descend to eye-level detail",
    "lens": "35mm, natural perspective",
    "height": "Start mid-drone, descend to ground level by end"
  },
  "lighting": "Bright late-morning sun, clear sky, warm natural light, dust in air",
  "style": "Cinematic documentary realism, 35mm film look",
  "color_grading": "Warm natural, earthy browns and greens, bright highlights",
  "mood": "Productive, hopeful, professional, energetic",
  "audio": {
    "ambient": "Construction sounds — hammering, concrete mixing, distant birds, wind",
    "music": "Instrumental builds gently — acoustic guitar and light percussion, rising",
    "voiceover": null
  },

  "text_overlay": [
    {
      "time": "0.5s-4s",
      "text": "KAMI URUSKAN SEMUA",
      "style": "Bold white text, large, center, dark shadow",
      "animation": "Fade in with slight scale up"
    },
    {
      "time": "4.5s-8.5s",
      "text": "Pelan · Kelulusan · Pembinaan",
      "style": "White text, medium, center-bottom, three words appearing one by one",
      "animation": "Sequential pop-in"
    }
  ],

  "voiceover": {
    "language": "Bahasa Melayu",
    "script": "Dari pelan, kelulusan... sampai pembinaan. Kami uruskan semuanya.",
    "tone": "Yakin, profesional, menenangkan",
    "timing": "1s - 7s"
  },

  "negative_prompt": "text, watermark, logo, distorted faces, extra fingers, cartoon, anime, unsafe workers without helmets, night, rain, snow, western architecture"
}
```

## Nota sambungan ke Klip 3
- Klip 2 berakhir dengan **kamera turun ke aras mata, melihat struktur rumah**
- Klip 3 mula dengan **rumah SIAP dari sudut serupa**
- Guna transition **whip-pan** atau **zoom** untuk kesan "masa berlalu"

---

# KLIP 3 (20–30s) — HASIL + CTA

## JSON Prompt

```json
{
  "clip_id": 3,
  "title": "Rumah Siap — Serah Kunci",
  "duration_seconds": 10,
  "aspect_ratio": "9:16",
  "resolution": "1080x1920",
  "frame_rate": 24,

  "prompt_string": "Cinematic beauty shot of a completed modern single-storey Malaysian bungalow at golden hour. Clean white and grey facade with dark roof, large glass windows, neat landscaping with tropical plants and a paved driveway. Warm interior lights glowing softly through the windows. A young Malaysian Malay family — father, mother wearing hijab, and two children — walk happily toward the front door, the father holding a set of keys. Camera slowly pushes in from a wide exterior shot toward the entrance. Golden hour sunlight, long soft shadows, lens flare, warm orange and amber tones. Shot on 35mm film, shallow depth of field, cinematic color grading. Smooth steady forward movement, no cuts.",

  "subject": "Young Malaysian Malay family (father, mother in hijab, two children) walking to a completed modern bungalow",
  "action": "Family walking happily toward the front door, father holding keys, children skipping",
  "setting": "Completed modern single-storey bungalow, neat landscaping, tropical plants, paved driveway, rural Perak",
  "camera": {
    "movement": "Slow steady push-in, wide to medium",
    "shot_type": "Wide establishing, narrowing to medium",
    "lens": "50mm, shallow depth of field",
    "height": "Eye-level, slight low angle for grandeur"
  },
  "lighting": "Golden hour, warm orange sunlight, long shadows, lens flare, interior lights glowing",
  "style": "Cinematic, premium real estate cinematography, 35mm film look",
  "color_grading": "Warm golden amber, rich and inviting",
  "mood": "Joyful, satisfied, aspirational, warm, family",
  "audio": {
    "ambient": "Children laughing softly, birds, gentle evening breeze",
    "music": "Warm uplifting acoustic — resolves and swells gently, then softens for CTA",
    "voiceover": null
  },

  "text_overlay": [
    {
      "time": "0.5s-4s",
      "text": "SIAP IKUT JADUAL. SERAH KUNCI.",
      "style": "Bold white text, large, center, warm shadow",
      "animation": "Fade in with slight scale up"
    },
    {
      "time": "5s-7.5s",
      "text": "2000+ pelanggan · 4.9★ Google · CIDB G4",
      "style": "Smaller white text, center, semi-transparent dark bar",
      "animation": "Fade in"
    },
    {
      "time": "7.5s-10s",
      "text": "WHATSAPP KAMI SEKARANG\nKonsultasi Percuma",
      "style": "Bold white text on solid red (#C8102E) rounded button, center",
      "animation": "Pop in with slight bounce, subtle pulse"
    }
  ],

  "voiceover": {
    "language": "Bahasa Melayu",
    "script": "Siap ikut jadual. Serah kunci. Ada tanah? WhatsApp kami sekarang — konsultasi percuma.",
    "tone": "Hangat, yakin, mengajak",
    "timing": "1s - 9s"
  },

  "negative_prompt": "text, watermark, logo, distorted faces, extra fingers, deformed hands, cartoon, anime, western architecture, snow, night only"
}
```

---

# CARA GUNA DALAM GOOGLE FLOW

## Langkah
1. Buka **Google Flow**
2. Pilih **Text to Video**
3. Tetapan:
   - Aspect ratio: **9:16**
   - Duration: **10 saat**
   - Resolution: **1080p**
4. Tampal **`prompt_string`** dari JSON di atas
5. Generate — buat **3-4 variasi** setiap klip, pilih terbaik
6. Muat turun 3 klip
7. Gabung dalam **CapCut** ikut turutan 1 → 2 → 3
8. Tambah teks skrin, voiceover, muzik

## Kalau Flow minta format berbeza
Guna hanya bahagian `prompt_string` — itu ayat penuh yang Flow faham.

---

# TEKS & VOICEOVER (RINGKASAN)

| Klip | Teks skrin | Voiceover |
|---|---|---|
| 1 | `ADA TANAH SENDIRI?` → `Tapi tak tahu macam mana nak mula?` | "Ada tanah sendiri... tapi tak tahu macam mana nak mula bina?" |
| 2 | `KAMI URUSKAN SEMUA` → `Pelan · Kelulusan · Pembinaan` | "Dari pelan, kelulusan... sampai pembinaan. Kami uruskan semuanya." |
| 3 | `SIAP IKUT JADUAL. SERAH KUNCI.` → `2000+ · 4.9★ · CIDB G4` → **CTA** | "Siap ikut jadual. Serah kunci. Ada tanah? WhatsApp kami — konsultasi percuma." |

**Voiceover penuh (bersambung):**
```
Ada tanah sendiri... tapi tak tahu macam mana nak mula bina?
Dari pelan, kelulusan... sampai pembinaan. Kami uruskan semuanya.
Siap ikut jadual. Serah kunci.
Ada tanah? WhatsApp kami sekarang — konsultasi percuma.
```
Tempoh: ~22 saat (muat dalam 30 saat dengan ruang bernafas)

---

# MUZIK

| Klip | Muzik |
|---|---|
| 1 | Piano solo, perlahan, reflektif |
| 2 | Gitar akustik + perkusi ringan, mula naik |
| 3 | Akustik hangat, memuncak, kemudian lembut untuk CTA |

**Cari di:** CapCut library, YouTube Audio Library, Pixabay Music
**Cari kata kunci:** "warm acoustic", "hopeful cinematic", "family inspirational"

> Turunkan muzik ke **20–30%** supaya voiceover jelas.

---

# NOTA PENTING TENTANG VIDEO AI

| Perkara | Realiti |
|---|---|
| **Kualiti** | Bagus untuk B-roll & suasana |
| **Ketepatan projek** | AI **tidak** tahu rupa projek sebenar anda |
| **Testimoni** | **Jangan** guna AI — guna orang sebenar |
| **Konsistensi** | Klip AI boleh berbeza antara satu sama lain |
| **Muka manusia** | Kadang cacat — semak tangan & muka sebelum guna |

### Cadangan: CAMPUR AI + FOOTAGE SEBENAR

| Bahagian | Sumber |
|---|---|
| Klip 1 (tanah kosong) | AI — susah nak shoot drone |
| Klip 2 (pembinaan) | **Footage sebenar** — bukti kerja anda |
| Klip 3 (rumah siap) | **Footage sebenar** — projek anda |
| Transition | AI atau CapCut |

> **Paling penting:** video iklan pembinaan mesti nampak **AUTHENTIC**.
> AI untuk pembukaan & suasana; footage sebenar untuk bukti.

---

# SEMAKAN SEBELUM EXPORT

- [ ] Nisbah 9:16, 1080 × 1920
- [ ] Jumlah 30 saat
- [ ] Sarikata ada (Bahasa Melayu)
- [ ] Voiceover jelas (muzik ≤30%)
- [ ] Teks tidak tertutup UI Reels (elak 20% bawah)
- [ ] CTA jelas + butang merah
- [ ] Warna konsisten antara 3 klip
- [ ] Muka & tangan manusia tidak cacat
- [ ] Tiada teks/watermark AI yang tidak diingini

---

# VARIASI UNTUK UJIAN

Buat **3 versi hook berbeza** (Klip 1 sahaja berbeza, Klip 2 & 3 sama):

| Versi | Teks hook | Voiceover hook |
|---|---|---|
| A | `ADA TANAH SENDIRI?` | "Ada tanah sendiri... tapi tak tahu macam mana nak mula?" |
| B | `TAKUT KONTRAKTOR LARI DUIT?` | "Takut bayar deposit... lepas tu kontraktor hilang?" |
| C | `BERMULA RM13X,000` | "Bina rumah atas tanah sendiri — bermula RM13X,000." |

Uji mana hook paling murah. Ini cara paling cepat cari pemenang.
