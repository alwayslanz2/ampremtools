# ForgeMotion CLI — Aktivasi Alight Motion Premium via Magic Link

Tool terminal Python untuk mengaktifkan Alight Motion Premium lewat
magic link email. Ini adalah versi **tools Python** dari project
website ForgeMotion (HTML5) — alurnya sama persis, tampilannya
berpindah dari browser ke terminal:

```
LOGIN AKUN → email → magic link masuk di Gmail → tempel link ke tools
           → verifikasi → provision → stempel [ SUKSES / GAGAL ]
```


## Keunggulan

| Fitur                   | Keterangan                                          |
|-------------------------|-----------------------------------------------------|
| Wajib akun (login)      | Gerbang login di depan; tanpa akun sah, tools menolak jalan |
| Expired per akun        | Tiap akun punya tanggal kedaluwarsa (zona WIB) |
| Limit harian aktivasi   | Kuota aktivasi premium per hari per akun, tercatat server-side |
| Tanpa dependensi        | Pure Python stdlib — tidak perlu `pip install` apa pun |
| Jalan di mana saja      | Windows, Linux, Mac, Android (Termux)               |
| Mode auto-flow          | Satu menu untuk alur lengkap tanpa pindah-pindah    |
| Stempel visual          | `[ SUKSES ]` / `[ GAGAL ]` ala stempel versi web    |
| Cooldown otomatis       | Jeda 15 detik antar pengiriman, sama seperti versi web |
| Pesan ramah             | Pesan error santai berbahasa Indonesia              |

## Sistem akun, expired & limit harian

### Aturan akses


1. **Tanggal kedaluwarsa** — setiap akun punya kolom `expired`
   (format `YYYY-MM-DD`, zona WIB, berlaku sampai akhir hari itu).
   Lewat tanggal tersebut, login otomatis ditolak.
2. **Status akun** — akun bisa diblokir manual (`status: blocked`)
   tanpa harus dihapus.
3. **Limit harian** — kolom `daily_limit` membatasi jumlah AKTIVASI
   PREMIUM yang sukses per hari per akun (reset otomatis tiap tengah
   malam WIB). Isi `-1` untuk tanpa batas. Setiap aktivasi sukses
   dicatat ke `usage` di database — tidak bisa diakali dengan hapus
   aplikasi atau ganti perangkat.
4. Kirim magic link (menu [2]) TIDAK memotong kuota — kuota hanya
   terpakai saat aktivasi premium benar-benar sukses.


## Syarat

- Python **3.7** atau lebih baru. Tidak ada syarat lain.
- Koneksi internet (untuk cek akun & menghubungi server).

Cek versi Python:

```bash
python --version       # Windows
python3 --version      # Linux / Termux / Mac
```

## Cara pakai

### Pilihan 1 — launcher cepat

| Platform            | Perintah / cara                          |
|---------------------|------------------------------------------|
| Windows             | dobel-klik `run.bat`                     |
| Linux / Termux / Mac| `chmod +x run.sh && ./run.sh` (chmod cukup sekali) |


### Cara Install
```tutorial install
$ pkg update
$ pkg upgrade
$ pkg install python3
$ pkg install colorama
$ pip install colorama
$ pkg install git
$ git clone https://github.com/alwayslanz2/ampremtools.git
$ cd ampremtools
$ python3 main.py
```
### Pilihan 2 — langsung dengan Python

```bash
python main.py           # Windows
python3 main.py          # Linux / Termux / Mac
python -m forgemotion    # alternatif: sebagai modul
```

### Alur pemakaian (menu 1 — Aktivasi Premium)

1. Buka tools, **login** dengan username + password akun kamu
   (password tidak ditampilkan saat diketik).
2. Cek kartu akun: masa berlaku & sisa kuota aktivasi hari ini.
3. Pilih menu **[1] Aktivasi Premium**.
4. Masukkan **alamat email aktif** — magic link langsung dikirim.
5. Buka **Gmail**, cari email terbaru dari ForgeMotion.
   Belum muncul? Intip folder **Promosi** atau **Spam**.
6. Salin **magic link** dari email (di HP: tekan lama link →
   *Salin alamat link*; di laptop: klik kanan → *Copy link address*).
7. Tempel link lengkap ke tools (harus diawali `https://`).
8. Tools memverifikasi lalu mengaktifkan premium otomatis —
   tunggu stempel **[ SUKSES ]**. Kuota harian otomatis terpakai 1.
9. Buka aplikasi Alight Motion. Kalau fiturnya belum kebuka semua,
   tutup dulu aplikasinya lalu buka lagi.

### Menu lain

| Menu | Fungsi                                                        |
|------|---------------------------------------------------------------|
| [1]  | Aktivasi premium lengkap (memakai kuota harian)               |
| [2]  | Kirim magic link saja (verifikasi menyusul lewat menu 3)      |
| [3]  | Verifikasi magic link yang sudah dikirim sebelumnya (pakai kuota) |
| [4]  | Cek status server pengirim (online / offline, tampilan ringkas) |
| [5]  | Info akun & kuota: masa berlaku, pemakaian, riwayat aktivasi  |
| [0]  | Keluar                                                        |

Tekan `Ctrl + C` kapan pun untuk membatalkan dengan aman.

## Struktur project

```
forgemotion-python/
├── main.py                  ← pintu masuk utama (python main.py)
├── run.sh                   ← launcher Linux / Termux / Mac
├── run.bat                  ← launcher Windows (dobel-klik)
├── requirements.txt         ← kosong: tanpa dependensi eksternal
├── README.md                ← file ini
└── forgemotion/             ← paket utama tools
    ├── __init__.py          ← metadata paket
    ├── __main__.py          ← dukungan `python -m forgemotion`
    ├── config.py            ← konfigurasi terpusat (token GitHub, repo, server, cooldown)
    ├── auth.py              ← gerbang akun: login, expired, limit harian (GitHub DB)
    ├── api.py               ← klien API upstream (kirim / verifikasi / provision)
    ├── utils.py             ← validasi email & magic link, cooldown, nomor serial
    ├── ui.py                ← tampilan terminal (login, kartu akun, stempel, spinner)
    └── app.py               ← alur interaktif (login → menu → langkah aktivasi)
```

## Pertanyaan yang sering muncul

**Lupa password / username?**
Hubungi pemilik tools — (menu [3]) tanpa perlu akses ke perangkat kamu.

**Akun saya kedaluwarsa, kenapa tidak bisa login?**
Begitulah aturannya — masa aktif akun habis. Minta pemilik tools
memperpanjang tanggal `expired` langsung bisa
login lagi tanpa install ulang.

**Kok muncul "Kuota aktivasi hari ini sudah habis"?**
Itu limit harian AKUN kamu (bukan kuota server). Setiap aktivasi
premium yang sukses memakai 1 jatah; jatah reset otomatis tiap
tengah malam WIB. Lihat sisa kuota lewat menu [5].

**Magic link-nya gak masuk-masuk?**
Tiga penyebab paling sering: email salah ketik, link nyangkut di
folder spam/promosi, atau server lagi ramai. Tunggu 1–2 menit, cek
spam, lalu kirim ulang lewat menu [2] atau [1].

**Kok muncul "Kuota server lagi penuh"?**
Jatah harian server pengirim sudah habis. Kuota reset sekitar
19.00 WIB — besok bisa dicoba lagi.

**Email aktivasi saya disimpan?**
Tidak. Tools ini tidak menyimpan email aktivasi — email cuma lewat
sekali untuk proses aktivasi. Yang tercatat di database user hanya
jumlah aktivasi per tanggal.

**Ini tool resmi Alight Motion?**
Bukan. ForgeMotion berdiri sendiri dan tidak ada hubungannya dengan
pengembang Alight Motion.