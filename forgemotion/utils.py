import re
import time
from urllib.parse import urlparse

from . import config

EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]{2,}$")
LINK_RE = re.compile(r"^https?://", re.IGNORECASE)


def email_valid(v):
    """True kalau bentuk emailnya sah (aturan sama dengan versi web)."""
    return bool(v) and bool(EMAIL_RE.match(v))


def link_valid(raw):
    """
    True kalau magic link kelihatan lengkap:
    diawali http(s):// dan bisa di-parse sebagai URL.
    """
    if not raw or not LINK_RE.match(raw):
        return False
    try:
        hasil = urlparse(raw)
        return bool(hasil.netloc)
    except ValueError:
        return False


def email_disamarkan(email):
    """Sembunyikan sebagian email untuk tampilan, cth: ka***@gmail.com."""
    try:
        nama, domain = email.split("@", 1)
    except ValueError:
        return email
    if len(nama) <= 2:
        nama_tampil = nama[0] + "*" if nama else "*"
    else:
        nama_tampil = nama[:2] + "*" * min(3, max(1, len(nama) - 2))
    return "{}@{}".format(nama_tampil, domain)


class Cooldown:
    """
    Penjaga jeda antar pengiriman ke email yang sama.
    Padanan konstanta COOLDOWN + lastSentAt di js/app.js.
    """

    def __init__(self, detik=None):
        self.detik = detik if detik is not None else config.COOLDOWN
        self._terakhir = {}  # email -> timestamp kirim terakhir

    def sisa(self, email):
        """Sisa detik tunggu untuk email ini (0 = boleh kirim)."""
        t = self._terakhir.get(email)
        if not t:
            return 0
        lewat = int(time.time() - t)
        return max(0, self.detik - lewat)

    def catat(self, email):
        """Tandai email ini baru saja dikirim."""
        self._terakhir[email] = time.time()

    def reset(self):
        self._terakhir.clear()


class Serial:
    """
    Nomor urut kartu formulir, hiasan yang sama dengan versi web:
    'No. 001/AM/2026' — naik tiap proses, dibungkus di 999.
    """

    def __init__(self, mulai=0):
        self._n = mulai % 999

    def berikut(self):
        self._n = (self._n % 998) + 1
        return "No. {:03d}/AM/{}".format(self._n, config.TAHUN)
