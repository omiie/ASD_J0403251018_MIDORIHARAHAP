# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama  : Midori Harahap
# NIM   : J0403251018
# Kelas : TPL A2/P2
# ==========================================================

# -----------------------------------
# Konstanta nama file
# -----------------------------------
nama_file = "stok_barang.txt"

# -----------------------------------
# Fungsi: Membaca data dari file
# -----------------------------------
def baca_stok(nama_file):
    stok_dict = {} # Inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() # ambil data perbaris dan hilangkan new line
            kode_barang, nama_barang, stok = baris.split(",") # ambil data per item data
            stok_dict[kode_barang] = {"nama": nama_barang, "stok": int(stok)} # masukkan dalam dictionary
    return stok_dict
buka_data = baca_stok(nama_file)

# -----------------------------------
# Fungsi: Menyimpan data ke file
# -----------------------------------