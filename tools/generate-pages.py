#!/usr/bin/env python3
# ============================================================
#  Penjana halaman lokasi & blog — NH Ivory Home Sdn. Bhd.
#  Jalankan:  python3 tools/generate-pages.py
# ============================================================

import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

SITE = "https://azrisaadproperties.github.io/nh-ivory-home"
WHATSAPP = "601163364664"
FORM_B64 = "aHR0cHM6Ly9mb3Jtc3VibWl0LmNvL2FqYXgvYThkYjcyMTI1NWZjZTAyMTA3ZjUzNzNiMWIwZTVkYTk="
CC_B64 = "YXpyaW1kc2FhZEBnbWFpbC5jb20="
PHONE_DISPLAY = "011-6336 6464"

# ------------------------------------------------------------
# TRACKING — isi ID di sini sahaja, kemudian jalankan penjana
# ------------------------------------------------------------
# Meta Pixel ID (Facebook/Instagram) — contoh: "1234567890123456"
META_PIXEL_ID = ""
# Google Analytics 4 Measurement ID — contoh: "G-XXXXXXXXXX"
GA4_ID = ""

# ------------------------------------------------------------
# DATA LOKASI
# ------------------------------------------------------------
LOCATIONS = [
    {
        "slug": "bina-rumah-ipoh",
        "place": "Ipoh",
        "state": "Perak",
        "district": "Kinta",
        "geo": ("4.5975", "101.0901"),
        "title": "Kontraktor Bina Rumah & Banglo Di Ipoh, Perak | NH Ivory Home",
        "desc": "Kontraktor bina rumah dan banglo atas tanah sendiri di Ipoh dan seluruh daerah Kinta. Tunai, loan bank atau LPPSA. Bermula RM13X,000. Konsultasi percuma.",
        "h1": "Kontraktor Bina Rumah &amp; Banglo Di Ipoh, Perak",
        "intro": "Ada tanah sendiri di sekitar Ipoh dan mahu bina rumah atau banglo? NH Ivory Home Sdn. Bhd. ialah kontraktor bina rumah di Ipoh yang membantu anda dari urusan pelan, kelulusan Majlis Bandaraya Ipoh (MBI), pembiayaan bank atau LPPSA, sehinggalah serah kunci.",
        "areas": ["Ipoh", "Bercham", "Chemor", "Klebang", "Meru", "Tambun", "Ampang", "Gunung Rapat", "Simpang Pulai", "Tanjung Rambutan", "Lahat", "Pusing", "Sungai Siput", "Chemor"],
        "sections": [
            ("Tanah Di Ipoh — Apa Yang Perlu Anda Tahu", [
                "Harga tanah di sekitar Ipoh terus meningkat, terutamanya di kawasan seperti Meru, Klebang, Bandar Meru Raya dan Ampang. Jika anda sudah memiliki tanah, membina rumah sendiri biasanya jauh lebih berbaloi berbanding membeli rumah siap.",
                "Kebanyakan tanah di Kinta terdiri daripada bekas tanah pertanian, tanah lot banglo, atau tanah kampung yang perlu ditukar syarat. Kami biasa menguruskan permohonan tukar syarat tanah pertanian kepada tanah bangunan melalui pihak berkuasa tempatan.",
            ]),
            ("Pengalaman Kami Di Daerah Kinta", [
                "Kami telah menyiapkan projek di kawasan Chemor dan sekitarnya. Antara cabaran biasa di Kinta ialah paras air bawah tanah yang tinggi di kawasan bekas lombong, serta keperluan cerun yang selamat di kawasan berbukit seperti Gunung Rapat dan Ampang.",
                "Setiap projek kami mulakan dengan lawatan tapak dan ujian tanah untuk menentukan jenis asas yang sesuai — sama ada asas pad, asas jalur, atau cerucuk.",
            ]),
            ("Kelulusan MBI & Proses Serahan", [
                "Projek pembinaan di Ipoh memerlukan kelulusan Pelan Bangunan daripada Majlis Bandaraya Ipoh (MBI). Kami menyediakan pelan arkitek, pelan struktur dan pelan sanitari, kemudian menguruskan penyerahan serta pematuhan syarat kelulusan.",
                "Selepas kelulusan, kami menguruskan permohonan CCC (Certificate of Completion and Compliance) supaya rumah anda sah untuk diduduki dan boleh disambung bekalan elektrik serta air.",
            ]),
        ],
        "faqs": [
            ("Berapa kos bina rumah di Ipoh?", "Bermula RM13X,000 untuk rumah satu tingkat secara tunai, bergantung kepada reka bentuk, saiz dan spesifikasi. Kadar biasa bagi banglo di Ipoh ialah antara RM130 hingga RM200 sekaki persegi."),
            ("Boleh bina atas tanah pertanian di Ipoh?", "Boleh, tetapi tanah perlu ditukar syarat kepada tanah bangunan terlebih dahulu. Kami boleh membantu urusan permohonan tukar syarat dengan pihak berkuasa."),
            ("Berapa lama kelulusan pelan di MBI?", "Biasanya 3 hingga 6 bulan bergantung kepada kelengkapan dokumen dan keadaan tapak. Kami akan mengemas kini status permohonan anda dari semasa ke semasa."),
        ],
        "project_note": "Projek kami di Chemor (daerah Kinta)",
        "image": "projek-5037.webp",
        "nearby": ["bina-rumah-batu-gajah", "bina-rumah-kampar", "bina-rumah-seri-iskandar"],
    },
    {
        "slug": "bina-rumah-seri-iskandar",
        "place": "Seri Iskandar",
        "state": "Perak",
        "district": "Perak Tengah",
        "geo": ("4.3579", "100.9671"),
        "title": "Kontraktor Bina Rumah Di Seri Iskandar, Perak | NH Ivory Home",
        "desc": "Ibu pejabat kami di Seri Iskandar. Kontraktor bina rumah dan banglo atas tanah sendiri di Perak Tengah. Tunai, loan bank atau LPPSA. Konsultasi percuma.",
        "h1": "Kontraktor Bina Rumah Di Seri Iskandar &amp; Perak Tengah",
        "intro": "Seri Iskandar ialah tempat ibu pejabat kami. NH Ivory Home Sdn. Bhd. berpangkalan di Bandar Seri Iskandar sejak 2020 dan telah membina rumah serta banglo di seluruh Perak Tengah — termasuk Bota, Lambor Kanan, Parit dan Kampung Gajah.",
        "areas": ["Bandar Seri Iskandar", "Bota", "Lambor Kanan", "Parit", "Kampung Gajah", "Pasir Salak", "Changkat Lada", "Tanjung Belanja", "Bota Kanan", "Lambor Kiri", "Kuala Bikam"],
        "sections": [
            ("Ibu Pejabat Kami Di Seri Iskandar", [
                "Pejabat kami terletak di No 70A, Persiaran SIBC 4, Bandar Seri Iskandar. Ini bermakna anda boleh datang terus ke pejabat untuk sesi perbincangan, melihat contoh pelan, dan berbincang dengan pasukan kami secara bersemuka.",
                "Kerana kami berpangkalan di sini, lawatan tapak dan tindakan susulan di kawasan Perak Tengah dibuat dengan lebih pantas.",
            ]),
            ("Projek Siap Di Perak Tengah", [
                "Antara projek kami yang sedang berjalan ialah di Desa Seri Iskandar dan Lambor Kanan. Kami juga menerima banyak pertanyaan daripada pemilik tanah di Bota dan Parit yang mahu membina rumah pertama di atas tanah warisan keluarga.",
                "Kawasan Seri Iskandar berkembang pesat dengan kehadiran Universiti Teknologi PETRONAS dan pelbagai perindustrian, jadi permintaan rumah sendiri di sini semakin tinggi.",
            ]),
            ("Tanah Warisan & Pecah Sempadan", [
                "Banyak tanah di Perak Tengah ialah tanah pusaka yang belum dipecah sempadan. Kami boleh membantu anda memahami keperluan pecah sempadan sebelum pembinaan, serta menyediakan pelan yang sesuai dengan saiz lot anda.",
            ]),
        ],
        "faqs": [
            ("Boleh saya datang ke pejabat di Seri Iskandar?", "Boleh. Sesi perbincangan percuma di pejabat kami di Bandar Seri Iskandar, atau kami boleh datang ke lokasi tanah anda."),
            ("Berapa kos bina rumah di Seri Iskandar?", "Bermula RM13X,000 untuk rumah satu tingkat. Harga akhir bergantung kepada reka bentuk, saiz dan spesifikasi yang anda pilih."),
            ("Adakah anda membina di Bota dan Parit?", "Ya. Kami meliputi seluruh daerah Perak Tengah termasuk Bota, Parit, Lambor Kanan, Kampung Gajah dan Pasir Salak."),
        ],
        "project_note": "Projek kami di Desa Seri Iskandar dan Lambor Kanan",
        "image": "projek-5033.webp",
        "nearby": ["bina-rumah-ipoh", "bina-rumah-kampar", "bina-rumah-teluk-intan"],
    },
    {
        "slug": "bina-rumah-batu-gajah",
        "place": "Batu Gajah",
        "state": "Perak",
        "district": "Kinta",
        "geo": ("4.4700", "101.0400"),
        "title": "Kontraktor Bina Rumah Di Batu Gajah, Perak | NH Ivory Home",
        "desc": "Kontraktor bina rumah dan banglo atas tanah sendiri di Batu Gajah, Perak. Tunai, loan bank atau LPPSA. Bermula RM13X,000. Konsultasi percuma.",
        "h1": "Kontraktor Bina Rumah &amp; Banglo Di Batu Gajah",
        "intro": "Batu Gajah ialah lokasi strategik antara Ipoh dan Seri Iskandar. Kami membantu pemilik tanah di Batu Gajah, Pusing, Tanjung Tualang dan sekitarnya membina rumah impian dengan harga telus dan kerja mengikut jadual.",
        "areas": ["Batu Gajah", "Pusing", "Tanjung Tualang", "Gopeng", "Tronoh", "Kota Bharu", "Malim Nawar", "Changkat", "Bemban"],
        "sections": [
            ("Projek Kami Di Batu Gajah", [
                "Kami telah menyiapkan projek banglo di Batu Gajah dan sedang membina di Tanjung Tualang. Kawasan ini menjadi pilihan ramai kerana harga tanah lebih berpatutan berbanding Ipoh, tetapi jarak ke bandar masih dekat.",
                "Banyak tanah di sekitar Batu Gajah ialah bekas tanah lombong dan tanah pertanian. Ujian tanah adalah langkah wajib sebelum kami mula membina.",
            ]),
            ("Asas Yang Betul Untuk Tanah Bekas Lombong", [
                "Tanah bekas lombong di sekitar Batu Gajah, Tronoh dan Pusing mempunyai ciri tanah yang berbeza — ada yang berpasir, ada yang lembut dan mendap. Kami melakukan ujian penembusan tanah untuk menentukan kedalaman asas yang selamat.",
                "Untuk tanah lembut, kami biasanya menggunakan asas jalur yang lebih dalam atau cerucuk mikro bagi mengelakkan rumah retak pada masa hadapan.",
            ]),
        ],
        "faqs": [
            ("Berapa kos bina rumah di Batu Gajah?", "Bermula RM13X,000 untuk rumah satu tingkat. Kadar biasa bagi banglo di daerah Kinta ialah RM130 hingga RM200 sekaki persegi."),
            ("Tanah saya bekas lombong, boleh bina?", "Boleh. Kami akan lakukan ujian tanah terlebih dahulu untuk menentukan jenis asas yang sesuai, kemudian berikan sebut harga berdasarkan hasil ujian tersebut."),
            ("Adakah anda membina di Tanjung Tualang?", "Ya. Kami mempunyai projek yang sedang berjalan di Tanjung Tualang dan meliputi seluruh kawasan sekitar Batu Gajah."),
        ],
        "project_note": "Projek kami di Batu Gajah dan Tanjung Tualang",
        "image": "projek-5044.webp",
        "nearby": ["bina-rumah-ipoh", "bina-rumah-kampar", "bina-rumah-seri-iskandar"],
    },
    {
        "slug": "bina-rumah-kampar",
        "place": "Kampar",
        "state": "Perak",
        "district": "Kampar",
        "geo": ("4.3167", "101.1500"),
        "title": "Kontraktor Bina Rumah Di Kampar & Gopeng, Perak | NH Ivory Home",
        "desc": "Kontraktor bina rumah dan banglo atas tanah sendiri di Kampar, Gopeng, Tronoh dan Tanjung Tualang. Tunai, loan bank atau LPPSA. Konsultasi percuma.",
        "h1": "Kontraktor Bina Rumah Di Kampar &amp; Gopeng",
        "intro": "Kampar berkembang pesat dengan kehadiran Universiti Tunku Abdul Rahman (UTAR). Kami membantu pemilik tanah di Kampar, Gopeng, Tronoh dan Malim Nawar membina rumah serta banglo yang selesa untuk keluarga atau disewakan kepada pelajar.",
        "areas": ["Kampar", "Gopeng", "Tronoh", "Malim Nawar", "Mambang Di Awan", "Tanjung Tualang", "Kota Bharu", "Kopisan", "Sungai Durian"],
        "sections": [
            ("Peluang Rumah Sewa Untuk Pelajar UTAR", [
                "Dengan kehadiran UTAR, permintaan sewa rumah di sekitar Kampar kekal tinggi. Ramai pemilik tanah membina rumah berbilang bilik atau rumah dua tingkat khusus untuk disewakan kepada pelajar.",
                "Kami boleh mereka bentuk rumah dengan susun atur bilik yang optimum supaya hasil sewa lebih maksimum, tanpa mengorbankan keselesaan keluarga anda sendiri.",
            ]),
            ("Tanah Di Gopeng & Tronoh", [
                "Kawasan Gopeng dan Tronoh banyak tanah bekas lombong bijih timah. Sama seperti Batu Gajah, ujian tanah perlu dilakukan sebelum menentukan jenis asas.",
                "Kami juga biasa menangani cabaran tapak yang berhampiran kawasan berbukit di Gopeng, termasuk keperluan tembok penahan dan saliran yang betul.",
            ]),
        ],
        "faqs": [
            ("Berapa kos bina rumah di Kampar?", "Bermula RM13X,000 untuk rumah satu tingkat secara tunai. Harga bergantung kepada reka bentuk, saiz dan spesifikasi."),
            ("Boleh bina rumah untuk disewakan kepada pelajar?", "Boleh. Kami boleh cadangkan susun atur dengan lebih banyak bilik dan kemudahan yang sesuai untuk penyewa pelajar."),
            ("Adakah anda membina di Gopeng dan Tronoh?", "Ya. Kami meliputi seluruh daerah Kampar termasuk Gopeng, Tronoh, Malim Nawar dan Tanjung Tualang."),
        ],
        "project_note": "Projek kami di Tanjung Tualang (daerah Kampar)",
        "image": "projek-5035.webp",
        "nearby": ["bina-rumah-ipoh", "bina-rumah-batu-gajah", "bina-rumah-seri-iskandar"],
    },
    {
        "slug": "bina-rumah-kuala-kangsar",
        "place": "Kuala Kangsar",
        "state": "Perak",
        "district": "Kuala Kangsar",
        "geo": ("4.7700", "100.9400"),
        "title": "Kontraktor Bina Rumah Di Kuala Kangsar, Perak | NH Ivory Home",
        "desc": "Kontraktor bina rumah dan banglo atas tanah sendiri di Kuala Kangsar, Manong, Sauk dan Padang Rengas. Tunai, loan bank atau LPPSA. Konsultasi percuma.",
        "h1": "Kontraktor Bina Rumah &amp; Banglo Di Kuala Kangsar",
        "intro": "Kuala Kangsar ialah bandar diraja Perak yang tenang dan sesuai untuk membina rumah keluarga. Kami telah membina di Kuala Kangsar dan Manong, dan membantu pemilik tanah di sekitar Sauk, Padang Rengas serta Karai.",
        "areas": ["Kuala Kangsar", "Manong", "Sauk", "Padang Rengas", "Karai", "Sayong", "Lenggong", "Kota Lama Kiri", "Chenderoh", "Sungai Siput"],
        "sections": [
            ("Projek Kami Di Kuala Kangsar & Manong", [
                "Kami mempunyai projek yang sedang berjalan di Kuala Kangsar dan Manong. Pendekatan kami ialah menyesuaikan reka bentuk dengan bentuk tanah dan persekitaran setempat.",
                "Banyak tanah di sekitar Kuala Kangsar terletak berhampiran Sungai Perak. Untuk kawasan sebegini, kami memberi perhatian tambahan kepada asas, saliran dan ketinggian lantai.",
            ]),
            ("Reka Bentuk Sesuai Iklim & Budaya Setempat", [
                "Rumah di Kuala Kangsar sering dibina dengan bumbung tinggi dan siling tinggi untuk pengudaraan yang lebih baik. Kami menawarkan 100+ pilihan reka bentuk yang boleh diubah suai mengikut citarasa anda.",
                "Jika anda mahu unsur tradisional Melayu Perak digabungkan dengan reka bentuk moden, kami boleh menyesuaikan fasad dan susun atur.",
            ]),
        ],
        "faqs": [
            ("Berapa kos bina banglo di Kuala Kangsar?", "Bermula RM13X,000 untuk rumah satu tingkat. Banglo moden dengan spesifikasi lebih tinggi biasanya bermula sekitar RM250,000 ke atas."),
            ("Tanah saya dekat Sungai Perak, boleh bina?", "Boleh. Kami akan menilai keadaan tapak dan mencadangkan asas serta ketinggian lantai yang sesuai untuk mengelakkan masalah air."),
            ("Adakah anda membina di Manong dan Sauk?", "Ya. Kami meliputi seluruh daerah Kuala Kangsar termasuk Manong, Sauk, Padang Rengas dan Karai."),
        ],
        "project_note": "Projek kami di Kuala Kangsar dan Manong",
        "image": "projek-5036.webp",
        "nearby": ["bina-rumah-ipoh", "bina-rumah-taiping", "bina-rumah-seri-iskandar"],
    },
    {
        "slug": "bina-rumah-taiping",
        "place": "Taiping",
        "state": "Perak",
        "district": "Larut Matang & Selama",
        "geo": ("4.8500", "100.7333"),
        "title": "Kontraktor Bina Rumah Di Taiping, Perak | NH Ivory Home",
        "desc": "Kontraktor bina rumah dan banglo atas tanah sendiri di Taiping, Kamunting, Simpang dan Selama. Tunai, loan bank atau LPPSA. Konsultasi percuma.",
        "h1": "Kontraktor Bina Rumah &amp; Banglo Di Taiping",
        "intro": "Taiping terkenal sebagai bandar paling banyak hujan di Semenanjung. NH Ivory Home Sdn. Bhd. membina rumah di Taiping, Kamunting, Simpang dan Selama dengan spesifikasi yang tahan terhadap cuaca lembap dan hujan tinggi.",
        "areas": ["Taiping", "Kamunting", "Simpang", "Aulong", "Kuala Sepetang", "Trong", "Batu Kurau", "Selama", "Pengkalan Hulu", "Matang"],
        "sections": [
            ("Bina Rumah Di Kawasan Hujan Tinggi", [
                "Purata hujan tahunan Taiping melebihi 4,000 mm — antara yang tertinggi di Malaysia. Ini bermakna pembinaan rumah di Taiping memerlukan perhatian serius terhadap kalis air, saliran dan pemilihan bahan.",
                "Kami menggunakan lapisan kalis air berkualiti pada bumbung, bilik air dan dinding luar, serta memastikan sistem saliran hujan direka dengan kapasiti yang mencukupi.",
            ]),
            ("Pemilihan Bahan Untuk Iklim Lembap", [
                "Untuk kawasan lembap, kami mengesyorkan bahan yang tahan karat dan kulat — seperti rangka bumbung yang dicat anti-karat, tingkap aluminium berkualiti, dan cat luar yang tahan kelembapan.",
                "Kami juga menambah pengudaraan siling dan ruang bawah bumbung untuk mengurangkan kelembapan dalam rumah.",
            ]),
        ],
        "faqs": [
            ("Berapa kos bina rumah di Taiping?", "Bermula RM13X,000 untuk rumah satu tingkat. Kos mungkin lebih tinggi sedikit jika tapak memerlukan kerja cerun atau saliran tambahan."),
            ("Bagaimana anda menangani masalah hujan di Taiping?", "Kami menggunakan lapisan kalis air berkualiti, bahan tahan karat, dan sistem saliran hujan berkapasiti tinggi. Ini termasuk dalam spesifikasi pakej kami."),
            ("Adakah anda membina di Selama dan Kamunting?", "Ya. Kami meliputi seluruh daerah Larut Matang dan Selama termasuk Kamunting, Simpang, Aulong dan Kuala Sepetang."),
        ],
        "project_note": "",
        "image": "projek-5038.webp",
        "nearby": ["bina-rumah-kuala-kangsar", "bina-rumah-ipoh", "bina-rumah-penang"],
    },
    {
        "slug": "bina-rumah-manjung",
        "place": "Manjung",
        "state": "Perak",
        "district": "Manjung",
        "geo": ("4.2000", "100.6700"),
        "title": "Kontraktor Bina Rumah Di Manjung & Sitiawan, Perak | NH Ivory Home",
        "desc": "Kontraktor bina rumah dan banglo di Sitiawan, Seri Manjung, Lumut, Beruas dan Pantai Remis. Tunai, loan bank atau LPPSA. Konsultasi percuma.",
        "h1": "Kontraktor Bina Rumah Di Manjung &amp; Sitiawan",
        "intro": "Daerah Manjung berkembang pesat dengan industri marin dan pelabuhan Lumut. Kami telah membina di Beruas dan membantu pemilik tanah di Sitiawan, Seri Manjung, Ayer Tawar serta Pantai Remis membina rumah sendiri.",
        "areas": ["Sitiawan", "Seri Manjung", "Lumut", "Beruas", "Ayer Tawar", "Pantai Remis", "Changkat Keruing", "Pangkor", "Bruas", "Kampung Koh"],
        "sections": [
            ("Pembinaan Di Kawasan Pesisir Pantai", [
                "Kawasan Manjung yang berhampiran laut terdedah kepada udara masin yang mempercepatkan proses karat. Untuk rumah di Lumut, Pantai Remis dan sekitar pesisir, kami menggunakan bahan tahan karat pada struktur bumbung, paip dan pengikat.",
                "Kami juga mempertimbangkan arah angin dan paras air laut semasa merancang orientasi rumah dan saliran.",
            ]),
            ("Projek Kami Di Beruas", [
                "Kami mempunyai projek yang sedang berjalan di Beruas. Kebanyakan tanah di kawasan ini ialah tanah pertanian atau tanah kampung yang perlu disediakan sebelum pembinaan.",
                "Kami membantu dari peringkat pembersihan tapak, ujian tanah, sehinggalah kerja struktur dan penyiapan.",
            ]),
        ],
        "faqs": [
            ("Berapa kos bina rumah di Manjung?", "Bermula RM13X,000 untuk rumah satu tingkat. Untuk kawasan pesisir, kos bahan tahan karat mungkin menambah sedikit kepada jumlah kos."),
            ("Boleh bina di kawasan berhampiran laut?", "Boleh. Kami menggunakan bahan tahan karat dan lapisan perlindungan tambahan untuk rumah di kawasan pesisir pantai."),
            ("Adakah anda membina di Beruas dan Pantai Remis?", "Ya. Kami meliputi seluruh daerah Manjung termasuk Sitiawan, Seri Manjung, Lumut, Beruas, Ayer Tawar dan Pantai Remis."),
        ],
        "project_note": "Projek kami di Beruas (daerah Manjung)",
        "image": "projek-5032.webp",
        "nearby": ["bina-rumah-teluk-intan", "bina-rumah-seri-iskandar", "bina-rumah-penang"],
    },
    {
        "slug": "bina-rumah-teluk-intan",
        "place": "Teluk Intan",
        "state": "Perak",
        "district": "Hilir Perak",
        "geo": ("4.0259", "101.0213"),
        "title": "Kontraktor Bina Rumah Di Teluk Intan, Perak | NH Ivory Home",
        "desc": "Kontraktor bina rumah dan banglo di Teluk Intan, Hutan Melintang, Bagan Datuk dan Langkap. Tunai, loan bank atau LPPSA. Konsultasi percuma.",
        "h1": "Kontraktor Bina Rumah &amp; Banglo Di Teluk Intan",
        "intro": "Kami telah menyiapkan Banglo Purewhite di Teluk Intan. NH Ivory Home Sdn. Bhd. berpengalaman membina di kawasan tanah rendah Hilir Perak — termasuk Hutan Melintang, Langkap, Chikus dan Bagan Datuk.",
        "areas": ["Teluk Intan", "Hutan Melintang", "Bagan Datuk", "Langkap", "Chikus", "Sungai Sumun", "Selekoh", "Rungkup", "Bagan Sungai Burong"],
        "sections": [
            ("Projek Kami Di Teluk Intan", [
                "Kami telah menyiapkan projek Banglo Purewhite di Teluk Intan yang kini diduduki oleh keluarga pelanggan kami. Projek ini membuktikan kemampuan kami membina di kawasan tanah rendah dengan asas yang betul.",
                "Salah satu cabaran utama di Hilir Perak ialah paras air bawah tanah yang tinggi dan risiko banjir di kawasan tertentu.",
            ]),
            ("Asas & Ketinggian Lantai Untuk Tanah Rendah", [
                "Untuk tanah rendah dan lembut di sekitar Teluk Intan, kami biasanya menaikkan ketinggian lantai melebihi paras banjir rekod, serta menggunakan asas yang direka khas berdasarkan hasil ujian tanah.",
                "Kami juga mengesyorkan longkang perimeter dan saliran bertutup untuk mengelakkan air bertakung di sekeliling rumah.",
            ]),
        ],
        "faqs": [
            ("Berapa kos bina rumah di Teluk Intan?", "Bermula RM13X,000 untuk rumah satu tingkat. Kos asas mungkin lebih tinggi jika tanah sangat lembut atau perlu ditinggikan."),
            ("Tanah saya selalu ditenggelami air, boleh bina?", "Boleh. Kami akan menaikkan ketinggian lantai melebihi paras banjir rekod dan membina saliran yang sesuai. Ini akan dibincangkan semasa lawatan tapak."),
            ("Adakah anda membina di Bagan Datuk dan Hutan Melintang?", "Ya. Kami meliputi seluruh daerah Hilir Perak termasuk Hutan Melintang, Bagan Datuk, Langkap dan Chikus."),
        ],
        "project_note": "Projek kami di Teluk Intan (Banglo Purewhite)",
        "image": "projek-5040.webp",
        "nearby": ["bina-rumah-manjung", "bina-rumah-seri-iskandar", "bina-rumah-ipoh"],
    },
    {
        "slug": "bina-rumah-kedah",
        "place": "Kedah",
        "state": "Kedah",
        "district": "Kota Setar & Kuala Muda",
        "geo": ("6.1184", "100.3685"),
        "title": "Kontraktor Bina Rumah Di Kedah (Alor Setar, Sungai Petani) | NH Ivory Home",
        "desc": "Kontraktor bina rumah dan banglo atas tanah sendiri di Kedah — Alor Setar, Sungai Petani, Kulim. Tunai, loan bank atau LPPSA. Konsultasi percuma.",
        "h1": "Kontraktor Bina Rumah Di Kedah",
        "intro": "Selain Perak, kami juga membina di seluruh Kedah termasuk Alor Setar, Sungai Petani, Kulim dan kawasan sekitarnya. Jika anda memiliki tanah di Kedah dan mahu membina rumah, pasukan kami sedia membantu.",
        "areas": ["Alor Setar", "Sungai Petani", "Kulim", "Kota Setar", "Kuala Muda", "Yan", "Pendang", "Pokok Sena", "Bandar Baharu", "Baling"],
        "sections": [
            ("Liputan Kami Di Kedah", [
                "Kami menerima pertanyaan daripada pemilik tanah di seluruh Kedah. Antara kawasan yang paling banyak permintaan ialah Alor Setar, Sungai Petani dan Kulim — kawasan yang berkembang dengan aktiviti perindustrian.",
                "Kami menawarkan perkhidmatan yang sama seperti di Perak: reka bentuk, pelan, kelulusan pihak berkuasa, bantuan pembiayaan, dan pembinaan sehingga serah kunci.",
            ]),
            ("Pilihan Pembiayaan Untuk Pembeli Kedah", [
                "Kami membantu permohonan pinjaman bank dan juga LPPSA khas untuk penjawat awam. Ramai pelanggan kami di Kedah menggunakan LPPSA kerana potongan gaji bulanan lebih mudah diurus.",
                "Bayaran binaan pula mengikut milestone siap kerja — bukan bayaran awal yang besar.",
            ]),
        ],
        "faqs": [
            ("Berapa kos bina rumah di Kedah?", "Bermula RM13X,000 untuk rumah satu tingkat secara tunai. Harga bergantung kepada reka bentuk, saiz dan spesifikasi."),
            ("Boleh guna LPPSA di Kedah?", "Boleh. Kami membantu permohonan LPPSA untuk penjawat awam di seluruh Kedah."),
            ("Kawasan mana di Kedah yang anda liputi?", "Seluruh Kedah termasuk Alor Setar, Sungai Petani, Kulim, Yan, Pendang, Pokok Sena dan Baling."),
        ],
        "project_note": "",
        "image": "projek-5034.webp",
        "nearby": ["bina-rumah-penang", "bina-rumah-taiping", "bina-rumah-ipoh"],
    },
    {
        "slug": "bina-rumah-penang",
        "place": "Pulau Pinang",
        "state": "Pulau Pinang",
        "district": "Seberang Perai",
        "geo": ("5.4164", "100.3327"),
        "title": "Kontraktor Bina Rumah Di Pulau Pinang (Seberang Perai) | NH Ivory Home",
        "desc": "Kontraktor bina rumah dan banglo atas tanah sendiri di Pulau Pinang — Seberang Perai, Bukit Mertajam, Butterworth. Tunai, loan bank atau LPPSA.",
        "h1": "Kontraktor Bina Rumah Di Pulau Pinang",
        "intro": "Kami membina rumah di Pulau Pinang, khususnya di Seberang Perai, Bukit Mertajam, Butterworth, Nibong Tebal dan kawasan sekitar. Harga tanah di pulau yang tinggi menjadikan pembinaan atas tanah sendiri pilihan yang lebih berbaloi.",
        "areas": ["Seberang Perai", "Bukit Mertajam", "Butterworth", "Perai", "Nibong Tebal", "Simpang Ampat", "Batu Kawan", "Kepala Batas", "Tasek Gelugor", "Balik Pulau"],
        "sections": [
            ("Bina Sendiri vs Beli Rumah Siap Di Penang", [
                "Harga rumah siap di Pulau Pinang antara yang tertinggi di Malaysia. Jika anda sudah memiliki tanah — sama ada tanah warisan di Balik Pulau atau lot di Seberang Perai — membina sendiri biasanya memberi nilai yang jauh lebih baik.",
                "Anda juga mendapat kebebasan memilih reka bentuk, saiz bilik dan bahan mengikut keperluan keluarga anda.",
            ]),
            ("Cabaran Tapak Di Penang", [
                "Tanah di Pulau Pinang sering berbukit atau berhampiran laut. Kedua-duanya memerlukan pendekatan asas dan saliran yang berbeza.",
                "Untuk tapak berbukit, kami merancang tembok penahan dan saliran cerun. Untuk kawasan pesisir seperti Batu Kawan dan Butterworth, kami menggunakan bahan tahan karat.",
            ]),
        ],
        "faqs": [
            ("Berapa kos bina rumah di Pulau Pinang?", "Bermula RM13X,000 untuk rumah satu tingkat. Kos mungkin lebih tinggi bergantung kepada keadaan tapak seperti cerun atau kawasan pesisir."),
            ("Boleh bina di tanah warisan di Balik Pulau?", "Boleh. Kami boleh membantu anda memahami keperluan pecah sempadan dan kelulusan pihak berkuasa tempatan sebelum pembinaan."),
            ("Kawasan mana di Penang yang anda liputi?", "Kami meliputi seluruh Pulau Pinang, dengan tumpuan di Seberang Perai, Bukit Mertajam, Butterworth, Nibong Tebal dan Balik Pulau."),
        ],
        "project_note": "",
        "image": "projek-5045.webp",
        "nearby": ["bina-rumah-kedah", "bina-rumah-taiping", "bina-rumah-manjung"],
    },
]

# ------------------------------------------------------------
# DATA ARTIKEL BLOG
# Blok: ("h2", teks) | ("p", teks) | ("ul", [item]) | ("table", {head, rows}) | ("callout", teks)
# ------------------------------------------------------------
POSTS = [
    {
        "slug": "kos-bina-rumah-perak-2026",
        "title": "Berapa Kos Bina Rumah Di Perak? Panduan Lengkap 2026 | NH Ivory Home",
        "desc": "Pecahan kos bina rumah di Perak 2026: kadar sekaki persegi, kos asas, bahan, kelulusan dan contoh bajet untuk rumah 1 tingkat dan banglo.",
        "h1": "Berapa Kos Bina Rumah Di Perak? Panduan Lengkap 2026",
        "category": "Panduan Kos",
        "date": "2026-09-17",
        "date_display": "17 September 2026",
        "reading": "8 minit",
        "image": "projek-5033.webp",
        "intro": "Salah satu soalan pertama yang ditanya oleh setiap pemilik tanah ialah: berapa kos sebenarnya untuk bina rumah di Perak? Artikel ini memberikan pecahan kos yang jelas supaya anda boleh merancang bajet dengan lebih yakin.",
        "blocks": [
            ("h2", "Kadar Kos Bina Rumah Sekaki Persegi"),
            ("p", "Kos bina rumah di Perak biasanya dikira berdasarkan keluasan lantai dalam kaki persegi (kps). Kadar ini merangkumi struktur, bumbung, dinding, lantai, pendawaian, paip dan kemasan asas."),
            ("p", "Secara umum, kadar di Perak lebih rendah berbanding Kuala Lumpur atau Pulau Pinang, tetapi bergantung juga kepada lokasi, keadaan tapak dan spesifikasi yang anda pilih. Jadual di bawah memberikan gambaran kasar:"),
            ("table", {
                "head": ["Jenis Rumah", "Saiz Anggaran", "Kadar Sekaki Persegi", "Anggaran Kos"],
                "rows": [
                    ["Rumah Sederhana 1 Tingkat", "1,000 – 1,500 kps", "RM130 – RM160", "RM130,000 – RM240,000"],
                    ["Banglo Moden 1 Tingkat", "1,500 – 2,500 kps", "RM160 – RM200", "RM240,000 – RM500,000"],
                    ["Banglo 2 Tingkat", "2,500 – 3,500 kps", "RM180 – RM230", "RM450,000 – RM800,000"],
                ],
            }),
            ("callout", "Angka di atas adalah anggaran kasar. Sebut harga tepat hanya boleh diberikan selepas lawatan tapak dan pengesahan reka bentuk."),
            ("h2", "Apa Yang Menaikkan Kos Binaan?"),
            ("p", "Beberapa faktor boleh menaikkan kos melebihi anggaran awal anda:"),
            ("ul", [
                "Keadaan tapak — tanah lembut, cerun atau bekas lombong memerlukan asas lebih kukuh",
                "Bentuk dan keluasan rumah — lebih banyak sudut dan bumbung kompleks bermakna lebih banyak kerja",
                "Spesifikasi bahan — jubin import, bumbung konkrit dan kayu keras menaikkan kos",
                "Bilangan bilik air — kerja paip dan kalis air bertambah",
                "Kerja luaran — pagar, landskap dan longkang",
            ]),
            ("h2", "Kos Yang Selalu Terlupa Dalam Bajet"),
            ("p", "Selain kos binaan utama, ada beberapa kos sampingan yang sering dilupakan oleh pemilik tanah:"),
            ("ul", [
                "Kos ujian tanah (biasanya RM1,500 – RM3,500)",
                "Kos pelan arkitek dan pelan struktur",
                "Yuran kelulusan pihak berkuasa tempatan",
                "Kos sambungan elektrik dan air (TNB &amp; Air)",
                "Kos pecah sempadan tanah (jika perlu)",
                "Kos CCC (Certificate of Completion and Compliance)",
            ]),
            ("h2", "Cara Menjimatkan Kos Tanpa Mengorbankan Kualiti"),
            ("p", "Ada beberapa cara bijak untuk mengawal kos binaan anda:"),
            ("ul", [
                "Pilih reka bentuk yang sederhana dari segi bentuk bumbung",
                "Gunakan susun atur segi empat yang lebih cekap",
                "Fokus perbelanjaan pada bahagian struktur dan kalis air",
                "Pilih bahan tempatan yang berkualiti",
                "Bina mengikut peringkat jika bajet terhad",
            ]),
            ("h2", "Kesimpulan"),
            ("p", "Kos bina rumah di Perak bermula sekitar RM13X,000 untuk rumah satu tingkat yang sederhana. Kunci utama ialah mendapatkan sebut harga terperinci, kontrak bertulis, dan bayaran mengikut milestone siap kerja."),
            ("p", "Jika anda memiliki tanah di Perak, Kedah atau Pulau Pinang, kami boleh memberikan sebut harga percuma selepas lawatan tapak dan perbincangan reka bentuk."),
        ],
        "faqs": [
            ("Berapa kos minimum bina rumah di Perak?", "Bermula sekitar RM13X,000 untuk rumah satu tingkat bersaiz sederhana secara tunai."),
            ("Adakah harga termasuk kelulusan pelan?", "Sebut harga kami boleh merangkumi kos pelan dan urusan kelulusan. Butiran akan dinyatakan dengan jelas dalam sebut harga bertulis."),
            ("Boleh bina rumah secara berperingkat?", "Boleh. Kami boleh merancang pembinaan mengikut peringkat mengikut kemampuan bajet anda."),
        ],
        "related": ["panduan-loan-bina-rumah", "cara-mohon-lppsA-bina-rumah", "pelan-rumah-banglo-3-bilik"],
    },
    {
        "slug": "panduan-loan-bina-rumah",
        "title": "Panduan Loan Bank Untuk Bina Rumah Atas Tanah Sendiri | NH Ivory Home",
        "desc": "Panduan lengkap loan bank untuk bina rumah atas tanah sendiri: jenis pinjaman, dokumen diperlukan, kelayakan, dan proses kelulusan langkah demi langkah.",
        "h1": "Panduan Loan Bank Untuk Bina Rumah Atas Tanah Sendiri",
        "category": "Pembiayaan",
        "date": "2026-09-10",
        "date_display": "10 September 2026",
        "reading": "7 minit",
        "image": "projek-5036.webp",
        "intro": "Tidak mempunyai wang tunai yang cukup bukan bermakna anda tidak boleh membina rumah. Artikel ini menerangkan cara mendapatkan pembiayaan bank untuk membina rumah di atas tanah sendiri.",
        "blocks": [
            ("h2", "Jenis Pinjaman Untuk Bina Rumah"),
            ("p", "Terdapat dua jenis pinjaman utama yang sesuai untuk membina rumah atas tanah sendiri:"),
            ("ul", [
                "<strong>Pinjaman Perumahan Bina Sendiri</strong> — pinjaman berjangka dengan cagaran tanah dan bangunan yang akan dibina",
                "<strong>Pinjaman Perumahan LPPSA</strong> — khas untuk penjawat awam, dengan ansuran dipotong terus daripada gaji",
            ]),
            ("h2", "Dokumen Yang Diperlukan"),
            ("p", "Bank memerlukan dokumen lengkap untuk memproses permohonan anda. Sediakan senarai berikut lebih awal supaya proses berjalan lancar:"),
            ("ul", [
                "Salinan geran tanah",
                "Pelan bangunan yang diluluskan pihak berkuasa",
                "Sebut harga terperinci daripada kontraktor",
                "Salinan lesen CIDB dan SSM kontraktor",
                "Penyata gaji 3 bulan / penyata bank 6 bulan",
                "Borang cukai (EA / BE) 2 tahun",
                "Salinan kad pengenalan",
                "Penyata KWSP (jika ada)",
            ]),
            ("h2", "Bagaimana Bank Melepaskan Wang Pinjaman"),
            ("p", "Berbeza dengan beli rumah siap, pinjaman bina rumah dilepaskan mengikut peringkat pembinaan. Bank akan menghantar jurunilai untuk mengesahkan setiap peringkat sebelum melepaskan bayaran."),
            ("p", "Peringkat pelepasan biasa: asas, struktur, bumbung, kerja dalaman, dan penyiapan. Ini melindungi anda kerana dana hanya keluar apabila kerja benar-benar siap."),
            ("callout", "Jangan bayar kontraktor secara tunai tanpa kontrak bertulis. Bayaran mengikut milestone melindungi wang anda."),
            ("h2", "Faktor Yang Menentukan Kelulusan"),
            ("p", "Bank menilai beberapa perkara sebelum meluluskan pinjaman bina rumah:"),
            ("ul", [
                "Pendapatan bulanan dan komitmen hutang semasa (DSR)",
                "Nilai tanah dan anggaran nilai rumah siap",
                "Rekod pembayaran pinjaman sebelum ini (CCRIS)",
                "Jenis dan lokasi tanah",
                "Kelayakan kontraktor yang dilantik",
            ]),
            ("h2", "Peranan Kontraktor Dalam Permohonan"),
            ("p", "Bank biasanya memerlukan kontraktor yang berdaftar dan mempunyai lesen sah. Kontraktor perlu menyediakan sebut harga terperinci, salinan lesen CIDB, dan pelan bangunan yang diluluskan."),
            ("p", "NH Ivory Home Sdn. Bhd. berdaftar dengan SSM, CIDB (G4) dan MOF. Kami menyediakan semua dokumen yang diperlukan oleh bank untuk mempercepatkan proses permohonan anda."),
        ],
        "faqs": [
            ("Boleh dapat loan untuk bina rumah atas tanah sendiri?", "Boleh. Bank menawarkan pinjaman perumahan bina sendiri dengan cagaran tanah dan bangunan yang akan dibina."),
            ("Berapa lama proses kelulusan loan?", "Biasanya 2 hingga 4 bulan, bergantung kepada kelengkapan dokumen dan proses penilaian bank."),
            ("Apa itu DSR dan kenapa penting?", "DSR (Debt Service Ratio) ialah nisbah jumlah bayaran hutang bulanan anda berbanding pendapatan. Bank biasanya menetapkan had sekitar 60–70%."),
        ],
        "related": ["cara-mohon-lppsA-bina-rumah", "kos-bina-rumah-perak-2026", "pelan-rumah-banglo-3-bilik"],
    },
    {
        "slug": "cara-mohon-lppsA-bina-rumah",
        "title": "Cara Mohon LPPSA Untuk Bina Rumah (Panduan Penjawat Awam) | NH Ivory Home",
        "desc": "Panduan LPPSA untuk bina rumah atas tanah sendiri: syarat kelayakan penjawat awam, dokumen, proses permohonan dan sebab permohonan ditolak.",
        "h1": "Cara Mohon LPPSA Untuk Bina Rumah (Panduan Penjawat Awam)",
        "category": "Pembiayaan",
        "date": "2026-09-03",
        "date_display": "3 September 2026",
        "reading": "7 minit",
        "image": "projek-5035.webp",
        "intro": "LPPSA (Lembaga Pembiayaan Perumahan Sektor Awam) menawarkan pembiayaan perumahan kepada penjawat awam dengan ansuran yang dipotong terus daripada gaji. Artikel ini menerangkan cara menggunakannya untuk membina rumah atas tanah sendiri.",
        "blocks": [
            ("h2", "Siapa Yang Layak Memohon LPPSA"),
            ("p", "LPPSA terbuka kepada penjawat awam yang sedang berkhidmat dalam perkhidmatan awam Malaysia. Antara kumpulan yang layak termasuk kakitangan kerajaan persekutuan, guru, anggota keselamatan dan kakitangan badan berkanun tertentu."),
            ("p", "Antara syarat umum: berumur tidak melebihi 60 tahun pada akhir tempoh pinjaman, dan masih mempunyai baki tempoh perkhidmatan yang mencukupi."),
            ("h2", "Bolehkah LPPSA Digunakan Untuk Bina Rumah?"),
            ("p", "Boleh. LPPSA menyediakan pembiayaan untuk membina rumah di atas tanah sendiri, bukan hanya untuk membeli rumah siap."),
            ("p", "Pembiayaan merangkumi kos tanah (jika berkenaan) dan kos pembinaan, tertakluk kepada penilaian dan had maksimum yang dibenarkan."),
            ("h2", "Dokumen Yang Diperlukan Untuk LPPSA"),
            ("p", "Sediakan dokumen berikut sebelum memulakan permohonan:"),
            ("ul", [
                "Salinan kad pengenalan",
                "Slip gaji terkini (disahkan)",
                "Surat pengesahan majikan",
                "Salinan geran tanah / dokumen hak milik",
                "Pelan bangunan yang diluluskan",
                "Sebut harga terperinci daripada kontraktor",
                "Salinan lesen SSM dan CIDB kontraktor",
                "Penyata bank 3–6 bulan",
            ]),
            ("h2", "Sebab Permohonan LPPSA Ditolak"),
            ("p", "Antara punca biasa permohonan ditolak:"),
            ("ul", [
                "Dokumen tidak lengkap atau tidak disahkan",
                "Baki tempoh perkhidmatan tidak mencukupi",
                "Komitmen hutang sedia ada terlalu tinggi",
                "Nilai tanah atau bangunan tidak menepati penilaian",
                "Kontraktor tidak berdaftar atau tidak berlesen",
            ]),
            ("h2", "Peranan Kami Dalam Permohonan LPPSA"),
            ("p", "Kami membantu pelanggan penjawat awam menyediakan dokumen kontraktor yang diperlukan oleh LPPSA — termasuk sebut harga terperinci, pelan bangunan yang diluluskan, dan salinan lesen SSM serta CIDB."),
            ("p", "Kami juga boleh menyelaras dengan pihak LPPSA untuk memastikan semua dokumen teknikal lengkap sebelum penyerahan."),
        ],
        "faqs": [
            ("Adakah LPPSA boleh digunakan untuk bina rumah?", "Boleh. LPPSA membiayai pembinaan rumah di atas tanah sendiri, tertakluk kepada penilaian dan had yang dibenarkan."),
            ("Berapa lama proses LPPSA?", "Biasanya 3 hingga 6 bulan bergantung kepada kelengkapan dokumen dan kelulusan."),
            ("Boleh guna LPPSA jika tanah atas nama pasangan?", "Tertakluk kepada syarat LPPSA. Kami boleh membantu anda memahami keperluan dokumen untuk kes sebegini."),
        ],
        "related": ["panduan-loan-bina-rumah", "kos-bina-rumah-perak-2026", "pelan-rumah-banglo-3-bilik"],
    },
    {
        "slug": "pelan-rumah-banglo-3-bilik",
        "title": "5 Idea Pelan Rumah Banglo 3 Bilik Yang Popular Di Perak | NH Ivory Home",
        "desc": "Idea pelan rumah banglo 3 bilik tidur yang popular di Perak — susun atur, keluasan, anggaran kos dan tip memilih pelan yang sesuai.",
        "h1": "5 Idea Pelan Rumah Banglo 3 Bilik Yang Popular Di Perak",
        "category": "Reka Bentuk",
        "date": "2026-08-27",
        "date_display": "27 Ogos 2026",
        "reading": "6 minit",
        "image": "projek-5044.webp",
        "intro": "Rumah banglo 3 bilik tidur ialah pilihan paling popular dalam kalangan keluarga muda di Perak. Ia cukup luas untuk keluarga kecil, tetapi kosnya masih terkawal. Ini 5 idea susun atur yang paling banyak diminta oleh pelanggan kami.",
        "blocks": [
            ("h2", "Mengapa 3 Bilik Tidur?"),
            ("p", "Rumah 3 bilik tidur memberikan keseimbangan yang baik antara kos dan keselesaan: satu bilik utama, satu bilik untuk anak, dan satu bilik yang boleh dijadikan bilik tetamu atau bilik kerja."),
            ("p", "Dari segi kos, rumah 3 bilik biasanya dalam lingkungan 1,000 hingga 1,500 kaki persegi — saiz yang paling berbaloi untuk dibina di atas tanah sendiri."),
            ("h2", "5 Susun Atur Yang Popular"),
            ("p", "Berikut ialah susun atur yang paling kerap diminta oleh pelanggan kami di Perak, Kedah dan Pulau Pinang:"),
            ("ul", [
                "<strong>Susun atur lurus (linear)</strong> — ruang tamu, ruang makan dan dapur dalam satu garisan. Paling kos efektif dan mudah dibina.",
                "<strong>Susun atur L</strong> — ruang tamu di satu sisi, bilik tidur di sisi lain. Memberi sedikit privasi antara ruang tetamu dan ruang peribadi.",
                "<strong>Konsep terbuka (open plan)</strong> — dapur, ruang makan dan ruang tamu tanpa dinding pemisah. Sesuai untuk keluarga yang suka berkumpul.",
                "<strong>Dua sayap (dual wing)</strong> — bilik utama di satu sayap, bilik anak di sayap lain. Sesuai untuk keluarga yang mahukan privasi lebih.",
                "<strong>Rumah berbumbung tinggi</strong> — siling tinggi di ruang tamu untuk pengudaraan lebih baik. Popular di kawasan panas dan lembap.",
            ]),
            ("h2", "Tip Memilih Pelan Yang Sesuai"),
            ("p", "Sebelum memilih pelan, pertimbangkan perkara berikut:"),
            ("ul", [
                "Orientasi matahari — elakkan bilik tidur utama menghadap barat",
                "Arah angin — susun tingkap untuk pengudaraan silang",
                "Bilangan bilik air — dua bilik air lebih selesa untuk keluarga",
                "Ruang simpanan — stor dan almari terbina dalam menjimatkan ruang",
                "Keluasan tanah — pastikan rumah tidak terlalu besar untuk lot anda",
                "Ruang letak kereta — pertimbangkan jika anda ada 2 kenderaan",
            ]),
            ("h2", "Kesimpulan"),
            ("p", "Pelan rumah banglo 3 bilik tidur boleh disesuaikan mengikut citarasa dan bajet anda. Kami menyediakan 100+ pilihan reka bentuk yang boleh diubah suai, dan anda boleh melihatnya semasa sesi perbincangan percuma."),
        ],
        "faqs": [
            ("Berapa keluasan rumah 3 bilik yang sesuai?", "Biasanya antara 1,000 hingga 1,500 kaki persegi, bergantung kepada saiz tanah dan keperluan keluarga."),
            ("Boleh ubah pelan mengikut citarasa sendiri?", "Boleh. Kami menyediakan 100+ pilihan reka bentuk yang boleh diubah suai mengikut keperluan anda."),
            ("Berapa kos bina rumah 3 bilik di Perak?", "Bermula sekitar RM13X,000 untuk susun atur sederhana, bergantung kepada saiz dan spesifikasi."),
        ],
        "related": ["kos-bina-rumah-perak-2026", "panduan-loan-bina-rumah", "cara-mohon-lppsA-bina-rumah"],
    },
]

# ------------------------------------------------------------
# TEMPLATE
# ------------------------------------------------------------
def head(title, desc, canonical, root, geo=None, og_type="website", published=None, image=None):
    geo_meta = ""
    if geo:
        geo_meta = f'''
  <meta name="geo.region" content="MY-08">
  <meta name="geo.placename" content="{geo[2]}">
  <meta name="geo.position" content="{geo[0]};{geo[1]}">
  <meta name="ICBM" content="{geo[0]}, {geo[1]}">'''
    article_meta = ""
    if published:
        article_meta = f'''
  <meta property="article:published_time" content="{published}">
  <meta property="article:section" content="Panduan Bina Rumah">'''
    og_image = image or f"{SITE}/assets/og-image.webp"
    return f'''<!DOCTYPE html>
<html lang="ms">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#ED1C24">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <link rel="canonical" href="{canonical}">{geo_meta}

  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="NH Ivory Home Sdn. Bhd.">
  <meta property="og:locale" content="ms_MY">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{og_image}">
  <meta property="og:url" content="{canonical}">{article_meta}

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{og_image}">

  <link rel="icon" href="{root}assets/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{root}css/style.css">
  <link rel="stylesheet" href="{root}css/seo.css">

  <script>
    window.NH_CONFIG = {{
      companyName: "NH Ivory Home Sdn. Bhd.",
      whatsapp: "{WHATSAPP}",
      formEndpointB64: "{FORM_B64}",
      formCcB64: "{CC_B64}",
      appsScriptUrl: "",
      metaPixelId: "{META_PIXEL_ID}",
      ga4Id: "{GA4_ID}",
      thankyouUrl: "{root}thankyou.html"
    }};
  </script>
  <script>
    if (window.NH_CONFIG.metaPixelId) {{
      !function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
      n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;
      n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
      t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,
      document,'script','https://connect.facebook.net/en_US/fbevents.js');
      fbq('init', window.NH_CONFIG.metaPixelId);
      fbq('track', 'PageView');
    }}
  </script>
  <script>
    if (window.NH_CONFIG.ga4Id) {{
      var gs = document.createElement('script');
      gs.async = true;
      gs.src = 'https://www.googletagmanager.com/gtag/js?id=' + window.NH_CONFIG.ga4Id;
      document.head.appendChild(gs);
      window.dataLayer = window.dataLayer || [];
      window.gtag = function(){{ dataLayer.push(arguments); }};
      gtag('js', new Date());
      gtag('config', window.NH_CONFIG.ga4Id);
    }}
  </script>
</head>
<body>
'''

def header(root):
    return f'''
  <header class="site-header" id="siteHeader">
    <div class="container header-inner">
      <a href="{root}index.html" class="brand" aria-label="NH Ivory Home Sdn. Bhd.">
        <img src="{root}images/logo.png" alt="NH Ivory Home Sdn. Bhd." class="brand-logo" width="192" height="32">
      </a>
      <nav class="nav" aria-label="Navigasi utama">
        <a href="{root}index.html">Utama</a>
        <a href="{root}index.html#pakej">Pakej</a>
        <a href="{root}kawasan/">Kawasan</a>
        <a href="{root}blog/">Blog</a>
        <a href="{root}index.html#faq">FAQ</a>
      </nav>
      <a href="#borang" class="btn btn-primary btn-sm header-cta">Konsultasi Percuma</a>
      <button class="nav-toggle" id="navToggle" aria-label="Buka menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>
'''

def cta_form(root):
    return f'''
    <section class="section section-cta" id="borang">
      <div class="container form-grid">
        <div class="form-copy">
          <span class="kicker kicker-light">Langkah Seterusnya</span>
          <h2>Konsultasi Secara Percuma</h2>
          <p>Cukup isi <strong>3 maklumat sahaja</strong> — nama, nombor WhatsApp dan lokasi tanah. Maklumat terus dihantar ke WhatsApp kami.</p>
          <ul class="check-list check-light">
            <li>Percuma, tiada komitmen</li>
            <li>Perbincangan pelan &amp; bajet</li>
            <li>Bantuan loan bank &amp; LPPSA</li>
          </ul>
          <div class="contact-quick">
            <p><strong>WhatsApp:</strong> <a href="#" class="js-wa-link">{PHONE_DISPLAY}</a></p>
            <p>Semua pertanyaan akan dijawab terus oleh pasukan jualan kami di WhatsApp.</p>
          </div>
        </div>

        <form class="lead-form" id="leadForm" novalidate>
          <h3 class="form-title">Isi 3 Maklumat Ini</h3>
          <p class="form-sub">Kami akan hubungi anda di WhatsApp untuk konsultasi percuma.</p>
          <div class="field">
            <label for="nama">Nama Penuh *</label>
            <input type="text" id="nama" name="nama" required autocomplete="name" placeholder="Contoh: Ahmad bin Ali">
            <span class="error" data-error-for="nama"></span>
          </div>
          <div class="field">
            <label for="telefon">No. WhatsApp *</label>
            <input type="tel" id="telefon" name="telefon" required autocomplete="tel" inputmode="numeric" placeholder="01X-XXX XXXX">
            <span class="error" data-error-for="telefon"></span>
          </div>
          <div class="field">
            <label for="lokasi">Lokasi Tanah *</label>
            <input type="text" id="lokasi" name="lokasi" required placeholder="Contoh: Seri Iskandar, Perak">
            <span class="error" data-error-for="lokasi"></span>
          </div>
          <input type="text" name="website" class="honeypot" tabindex="-1" autocomplete="off" aria-hidden="true">
          <button type="submit" class="btn btn-wa btn-lg btn-block" id="submitBtn">Hantar Ke WhatsApp</button>
          <p class="form-note">Maklumat anda akan dihantar ke WhatsApp kami dan salinan ke email. Kami tidak berkongsi maklumat anda.</p>
          <p class="form-status" id="formStatus" role="status" aria-live="polite"></p>
        </form>
      </div>
    </section>
'''

def footer(root):
    loc_links = "".join(
        f'<li><a href="{root}{l["slug"]}/">{l["place"]}</a></li>' for l in LOCATIONS
    )
    post_links = "".join(
        f'<li><a href="{root}blog/{p["slug"]}/">{p["h1"].split("(")[0].strip()}</a></li>' for p in POSTS[:3]
    )
    return f'''
  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <img src="{root}images/logo.png" alt="NH Ivory Home Sdn. Bhd." class="footer-logo" width="228" height="38">
        <p class="footer-desc">
          NH Ivory Home Sdn. Bhd. adalah syarikat pembinaan yang disahkan oleh CIDB Malaysia (G4),
          ibu pejabat di Seri Iskandar, Perak. Kami mengkhususkan diri dalam membina rumah banglo
          di tanah persendirian di Perak, Kedah &amp; Pulau Pinang.
        </p>
      </div>
      <div>
        <h4>Kawasan Kami</h4>
        <ul class="footer-list">{loc_links}</ul>
      </div>
      <div>
        <h4>Panduan</h4>
        <ul class="footer-list">{post_links}
          <li><a href="{root}blog/">Semua Artikel</a></li>
        </ul>
      </div>
      <div>
        <h4>Hubungi</h4>
        <ul class="footer-list">
          <li>WhatsApp: <a href="#" class="js-wa-link">{PHONE_DISPLAY}</a></li>
          <li class="footer-addr">Ibu Pejabat: No 70A, Persiaran SIBC 4, Bandar Seri Iskandar, 32610 Seri Iskandar, Perak</li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>&copy; <span id="year"></span> NH Ivory Home Sdn. Bhd. (1369193-H) Hak cipta terpelihara.</p>
      <p class="disclaimer">Harga dan tempoh adalah anggaran dan tertakluk kepada terma &amp; syarat.</p>
    </div>
  </footer>

  <div class="wa-widget">
    <div class="wa-popup" id="waPopup" role="dialog" aria-label="Pertanyaan WhatsApp">
      <div class="wa-popup-head">
        <span class="wa-avatar" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2z"/></svg>
        </span>
        <div class="wa-popup-title">
          <strong>NH Ivory Home</strong>
          <small><span class="wa-dot" aria-hidden="true"></span> Biasanya membalas dalam beberapa minit</small>
        </div>
        <button type="button" class="wa-popup-close" id="waPopupClose" aria-label="Tutup">&times;</button>
      </div>
      <div class="wa-popup-body">
        <p class="wa-bubble">Hai! Nak konsultasi percuma bina rumah atas tanah sendiri? Isi 3 maklumat ini, kami terus balas di WhatsApp.</p>
        <form id="quickForm" novalidate>
          <div class="field"><input type="text" name="nama" placeholder="Nama penuh" required autocomplete="name" aria-label="Nama penuh"><span class="error" data-error-for="nama"></span></div>
          <div class="field"><input type="tel" name="telefon" placeholder="No. WhatsApp" required autocomplete="tel" inputmode="numeric" aria-label="No. WhatsApp"><span class="error" data-error-for="telefon"></span></div>
          <div class="field"><input type="text" name="lokasi" placeholder="Lokasi tanah" required aria-label="Lokasi tanah"><span class="error" data-error-for="lokasi"></span></div>
          <input type="text" name="website" class="honeypot" tabindex="-1" autocomplete="off" aria-hidden="true">
          <button type="submit" class="btn btn-wa btn-block">Hantar Ke WhatsApp</button>
          <p class="form-status" role="status" aria-live="polite"></p>
        </form>
      </div>
    </div>
    <button type="button" class="wa-float" id="waFloat" aria-label="Buka pertanyaan WhatsApp" aria-expanded="false" aria-controls="waPopup">
      <span class="wa-float-ring" aria-hidden="true"></span>
      <span class="wa-float-ring wa-float-ring--2" aria-hidden="true"></span>
      <span class="wa-float-icon" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2z"/></svg>
      </span>
      <span class="wa-float-label" id="waLabel">Tanya kami</span>
    </button>
  </div>

  <script src="{root}js/main.js" defer></script>
  <script src="{root}js/form.js" defer></script>
</body>
</html>
'''

def ldjson(obj):
    return f'  <script type="application/ld+json">\n{json.dumps(obj, ensure_ascii=False, indent=2)}\n  </script>\n'

def breadcrumb_ld(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u}
            for i, (n, u) in enumerate(items)
        ],
    }

def business_ref():
    return {"@type": "GeneralContractor", "@id": f"{SITE}/#business", "name": "NH Ivory Home Sdn. Bhd."}


# ------------------------------------------------------------
# UTILITI
# ------------------------------------------------------------
import re as _re

def slugify(text):
    t = _re.sub(r"<[^>]+>", "", text)
    t = t.lower()
    t = _re.sub(r"[^a-z0-9]+", "-", t)
    return t.strip("-")

def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("  ditulis:", path.relative_to(ROOT_DIR))

def faq_block(faqs):
    items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    return f'<div class="faq">{items}</div>'

def faq_ld(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }

def render_blocks(blocks):
    out = []
    for kind, val in blocks:
        if kind == "h2":
            out.append(f'<h2 id="{slugify(val)}">{val}</h2>')
        elif kind == "p":
            out.append(f"<p>{val}</p>")
        elif kind == "ul":
            items = "".join(f"<li>{i}</li>" for i in val)
            out.append(f"<ul>{items}</ul>")
        elif kind == "callout":
            out.append(f'<div class="callout">{val}</div>')
        elif kind == "table":
            head = "".join(f"<th>{h}</th>" for h in val["head"])
            rows = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in val["rows"])
            out.append(f"<table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>")
    return "\n".join(out)

def trust_chips(extra_state):
    return f'''
        <ul class="trust-chips">
          <li><strong>2000+</strong> Pelanggan</li>
          <li><strong>CIDB G4</strong> Berdaftar</li>
          <li><strong>MOF</strong> Berdaftar</li>
          <li><strong>4.9&#9733;</strong> Google Review</li>
          <li>Liputan <strong>{extra_state}</strong></li>
        </ul>'''

def inject_ld(page, blocks):
    ld = "".join(ldjson(b) for b in blocks)
    return page.replace("</head>", ld + "</head>", 1)


# ------------------------------------------------------------
# HALAMAN LOKASI
# ------------------------------------------------------------
def render_location(loc):
    root = "../"
    canonical = f"{SITE}/{loc['slug']}/"
    img = f"{SITE}/images/{loc['image']}"
    place, state, district = loc["place"], loc["state"], loc["district"]

    page = head(
        loc["title"], loc["desc"], canonical, root,
        geo=(loc["geo"][0], loc["geo"][1], f"{place}, {state}"),
        image=img,
    )
    page += header(root)
    page += "<main>"

    page += f'''
    <section class="page-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="{root}index.html">Utama</a> <span>/</span>
          <a href="{root}kawasan/">Kawasan</a> <span>/</span>
          <span aria-current="page">{place}</span>
        </nav>
        <h1>{loc["h1"]}</h1>
        <p class="lead">{loc["intro"]}</p>
        <div class="page-actions">
          <a href="#borang" class="btn btn-primary btn-lg">Konsultasi Percuma</a>
          <a href="#" class="btn btn-wa btn-lg js-wa-link">WhatsApp Kami</a>
        </div>{trust_chips(state)}
      </div>
    </section>
'''

    page += '<section class="section"><div class="container"><div class="prose">'
    for h, paras in loc["sections"]:
        page += f"<h2>{h}</h2>"
        for p in paras:
            page += f"<p>{p}</p>"
    page += "</div></div></section>"

    if loc.get("project_note"):
        page += f'''
    <section class="section section-soft">
      <div class="container about-grid">
        <div class="about-media">
          <img src="{root}images/{loc['image']}" alt="{loc['project_note']}" loading="lazy"
               onerror="this.onerror=null;this.src='{root}assets/placeholder.svg'">
        </div>
        <div class="about-copy">
          <span class="kicker">Projek Sebenar</span>
          <h2>{loc['project_note']}</h2>
          <p>Kami bukan sekadar memberikan sebut harga — kami menunjukkan kerja yang telah dan sedang kami laksanakan. Setiap projek diuruskan oleh pasukan sendiri dengan pemantauan berkala.</p>
          <ul class="check-list">
            <li>Bayaran ikut milestone siap kerja</li>
            <li>Laporan progres berkala</li>
            <li>Kontrak bertulis &amp; harga telus</li>
          </ul>
          <a href="#borang" class="btn btn-primary">Dapatkan Sebut Harga Percuma</a>
        </div>
      </div>
    </section>
'''

    chips = "".join(f"<li>{a}</li>" for a in loc["areas"])
    page += f'''
    <section class="section">
      <div class="container">
        <div class="section-head">
          <span class="kicker">Kawasan Liputan</span>
          <h2>Kami Membina Di Seluruh {district}</h2>
          <p>Antara kawasan yang kami liputi di sekitar {place}:</p>
        </div>
        <ul class="area-chips">{chips}</ul>
      </div>
    </section>
'''

    page += f'''
    <section class="section section-soft">
      <div class="container container-narrow">
        <div class="section-head">
          <span class="kicker">Soalan Lazim</span>
          <h2>FAQ — Bina Rumah Di {place}</h2>
        </div>
        {faq_block(loc["faqs"])}
      </div>
    </section>
'''

    page += cta_form(root)

    nearby = [l for l in LOCATIONS if l["slug"] in loc["nearby"]]
    if nearby:
        links = "".join(
            f'<a href="{root}{n["slug"]}/">Bina Rumah Di {n["place"]}<span>{n["district"]}, {n["state"]}</span></a>'
            for n in nearby
        )
        page += f'''
    <section class="section">
      <div class="container">
        <div class="section-head">
          <span class="kicker">Kawasan Berdekatan</span>
          <h2>Kami Juga Membina Di</h2>
        </div>
        <div class="link-grid">{links}</div>
      </div>
    </section>
'''

    page += "</main>"
    page += footer(root)

    ld = [
        breadcrumb_ld([("Utama", f"{SITE}/"), ("Kawasan", f"{SITE}/kawasan/"), (place, canonical)]),
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "serviceType": f"Kontraktor Bina Rumah di {place}",
            "provider": business_ref(),
            "areaServed": {"@type": "City", "name": place},
            "description": loc["desc"],
            "url": canonical,
        },
        faq_ld(loc["faqs"]),
    ]
    return inject_ld(page, ld)


# ------------------------------------------------------------
# HALAMAN BLOG
# ------------------------------------------------------------
def render_post(post):
    root = "../../"
    canonical = f"{SITE}/blog/{post['slug']}/"
    img = f"{SITE}/images/{post['image']}"

    page = head(
        post["title"], post["desc"], canonical, root,
        og_type="article", published=post["date"], image=img,
    )
    page += header(root)
    page += "<main>"

    toc_items = "".join(
        f'<li><a href="#{slugify(v)}">{v}</a></li>' for k, v in post["blocks"] if k == "h2"
    )

    page += f'''
    <section class="page-hero page-hero--article">
      <div class="container container-narrow">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="{root}index.html">Utama</a> <span>/</span>
          <a href="{root}blog/">Blog</a> <span>/</span>
          <span aria-current="page">{post["category"]}</span>
        </nav>
        <span class="kicker">{post["category"]}</span>
        <h1>{post["h1"]}</h1>
        <div class="article-meta">
          <span>Diterbitkan {post["date_display"]}</span>
          <span>Masa baca: {post["reading"]}</span>
          <span>Oleh NH Ivory Home Sdn. Bhd.</span>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container container-narrow">
        <img class="article-cover" src="{root}images/{post['image']}" alt="{post['h1']}" loading="lazy"
             onerror="this.onerror=null;this.src='{root}assets/placeholder.svg'">
        <p class="lead">{post["intro"]}</p>
        <div class="toc">
          <h2>Isi Kandungan</h2>
          <ol>{toc_items}</ol>
        </div>
        <div class="prose">{render_blocks(post["blocks"])}</div>
      </div>
    </section>

    <section class="section section-soft">
      <div class="container container-narrow">
        <div class="section-head">
          <span class="kicker">Soalan Lazim</span>
          <h2>Soalan Yang Sering Ditanya</h2>
        </div>
        {faq_block(post["faqs"])}
      </div>
    </section>
'''

    page += cta_form(root)

    related = [p for p in POSTS if p["slug"] in post["related"]]
    if related:
        links = "".join(
            f'<a href="{root}blog/{r["slug"]}/">{r["h1"]}<span>{r["category"]} · {r["reading"]}</span></a>'
            for r in related
        )
        page += f'''
    <section class="section">
      <div class="container">
        <div class="section-head">
          <span class="kicker">Baca Seterusnya</span>
          <h2>Artikel Berkaitan</h2>
        </div>
        <div class="link-grid">{links}</div>
      </div>
    </section>
'''

    page += "</main>"
    page += footer(root)

    ld = [
        breadcrumb_ld([("Utama", f"{SITE}/"), ("Blog", f"{SITE}/blog/"), (post["h1"], canonical)]),
        {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": post["h1"],
            "description": post["desc"],
            "image": img,
            "datePublished": post["date"],
            "dateModified": post["date"],
            "inLanguage": "ms-MY",
            "author": business_ref(),
            "publisher": {
                "@type": "Organization",
                "name": "NH Ivory Home Sdn. Bhd.",
                "logo": {"@type": "ImageObject", "url": f"{SITE}/images/logo.png"},
            },
            "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
        },
        faq_ld(post["faqs"]),
    ]
    return inject_ld(page, ld)


# ------------------------------------------------------------
# HALAMAN HUB
# ------------------------------------------------------------
def render_kawasan_hub():
    root = "../"
    canonical = f"{SITE}/kawasan/"
    page = head(
        "Kawasan Kami — Kontraktor Bina Rumah Perak, Kedah & Penang | NH Ivory Home",
        "Senarai kawasan perkhidmatan NH Ivory Home Sdn. Bhd. — kontraktor bina rumah di seluruh Perak, Kedah dan Pulau Pinang.",
        canonical, root,
    )
    page += header(root)
    page += "<main>"

    cards = "".join(
        f'''<a href="{root}{l["slug"]}/">Bina Rumah Di {l["place"]}<span>{l["district"]}, {l["state"]}</span></a>'''
        for l in LOCATIONS
    )

    page += f'''
    <section class="page-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="{root}index.html">Utama</a> <span>/</span>
          <span aria-current="page">Kawasan</span>
        </nav>
        <h1>Kawasan Perkhidmatan Kami</h1>
        <p class="lead">NH Ivory Home Sdn. Bhd. membina rumah dan banglo atas tanah sendiri di seluruh Perak, Kedah dan Pulau Pinang. Pilih kawasan anda untuk maklumat lanjut.</p>
        <div class="page-actions">
          <a href="#borang" class="btn btn-primary btn-lg">Konsultasi Percuma</a>
          <a href="#" class="btn btn-wa btn-lg js-wa-link">WhatsApp Kami</a>
        </div>{trust_chips("Perak · Kedah · Penang")}
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <span class="kicker">Pilih Kawasan</span>
          <h2>Kami Membina Di Kawasan Ini</h2>
        </div>
        <div class="link-grid">{cards}</div>
      </div>
    </section>
'''

    page += cta_form(root)
    page += "</main>"
    page += footer(root)

    ld = [breadcrumb_ld([("Utama", f"{SITE}/"), ("Kawasan", canonical)])]
    return inject_ld(page, ld)


def render_blog_hub():
    root = "../"
    canonical = f"{SITE}/blog/"
    page = head(
        "Blog & Panduan Bina Rumah | NH Ivory Home Sdn. Bhd.",
        "Panduan bina rumah atas tanah sendiri — kos binaan, loan bank, LPPSA dan reka bentuk rumah. Ditulis oleh kontraktor bina rumah Perak, Kedah & Penang.",
        canonical, root,
    )
    page += header(root)
    page += "<main>"

    cards = "".join(
        f'''<a href="{root}blog/{p["slug"]}/">{p["h1"]}<span>{p["category"]} · {p["reading"]} · {p["date_display"]}</span></a>'''
        for p in POSTS
    )

    page += f'''
    <section class="page-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="{root}index.html">Utama</a> <span>/</span>
          <span aria-current="page">Blog</span>
        </nav>
        <h1>Blog &amp; Panduan Bina Rumah</h1>
        <p class="lead">Artikel praktikal untuk membantu anda memahami kos, pembiayaan dan reka bentuk rumah sebelum mula membina di atas tanah sendiri.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <span class="kicker">Semua Artikel</span>
          <h2>Panduan Untuk Pemilik Tanah</h2>
        </div>
        <div class="link-grid">{cards}</div>
      </div>
    </section>
'''

    page += cta_form(root)
    page += "</main>"
    page += footer(root)

    ld = [breadcrumb_ld([("Utama", f"{SITE}/"), ("Blog", canonical)])]
    return inject_ld(page, ld)


# ------------------------------------------------------------
# SITEMAP
# ------------------------------------------------------------
def write_sitemap():
    urls = [(f"{SITE}/", "1.0", "weekly")]
    urls.append((f"{SITE}/kawasan/", "0.9", "monthly"))
    urls.append((f"{SITE}/blog/", "0.8", "weekly"))
    for l in LOCATIONS:
        urls.append((f"{SITE}/{l['slug']}/", "0.9", "monthly"))
    for p in POSTS:
        urls.append((f"{SITE}/blog/{p['slug']}/", "0.7", "monthly"))

    body = ""
    for u, pri, freq in urls:
        body += f"""  <url>
    <loc>{u}</loc>
    <lastmod>2026-09-17</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{pri}</priority>
  </url>\n"""

    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}</urlset>
'''
    write(ROOT_DIR / "sitemap.xml", xml)


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------
def main():
    print("Menjana halaman lokasi...")
    for loc in LOCATIONS:
        write(ROOT_DIR / loc["slug"] / "index.html", render_location(loc))

    print("Menjana halaman blog...")
    for post in POSTS:
        write(ROOT_DIR / "blog" / post["slug"] / "index.html", render_post(post))

    print("Menjana halaman hub...")
    write(ROOT_DIR / "kawasan" / "index.html", render_kawasan_hub())
    write(ROOT_DIR / "blog" / "index.html", render_blog_hub())

    print("Menjana sitemap...")
    write_sitemap()

    print(f"\nSiap. {len(LOCATIONS)} halaman lokasi + {len(POSTS)} artikel blog.")


if __name__ == "__main__":
    main()
