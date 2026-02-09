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
    """
    Membaca data stok dari file teks
    """
    stok_dict = {} # Inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() # ambil data perbaris dan hilangkan new line
            kode_barang, nama_barang, stok = baris.split(",") # ambil data per item data
            stok_dict[kode_barang] = {"nama": nama_barang, "stok": int(stok)} # masukkan dalam dictionary
    return stok_dict

# -----------------------------------
# Fungsi: Menyimpan data ke file
# -----------------------------------
def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks
    """
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode_barang in sorted(stok_dict.keys()):
            nama_barang = stok_dict[kode_barang]["nama"]
            stok = stok_dict[kode_barang]["stok"]
            file.write(f"{kode_barang},{nama_barang},{stok}\n")

# -----------------------------------
# Fungsi: Menampilkan semua data
# -----------------------------------
def tampilkan_semua(stok_dict):
    """
    Menampilkan semua barang di stock_dict
    """
    print("======= DAFTAR BARANG =======")
    # membuat header tabel
    print(f"{'KODE' : <10} | {'NAMA' : <15} | {'STOK' : <5}")
    print("-"*35) # membuat garis

    # menampilkan isi datanya
    if stok_dict:
        for kode_barang in sorted(stok_dict.keys()):
            nama_barang = stok_dict[kode_barang]["nama"]
            stok = stok_dict[kode_barang]["stok"]
            print(f"{kode_barang : <10} | {nama_barang : <15} | {stok : >5}")
    else:
        print("stok kosong.")

# -----------------------------------
# Fungsi: Cari barang berdasarkan kode
# -----------------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang
    """
    kode = input("Masukkan Kode Barang: ").strip()
    if kode in stok_dict:
        nama_barang = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]

        print("======= Data Barang Ditemukan =======")
        print(f"Kode      : {kode}")
        print(f"Nama      : {nama_barang}")
        print(f"Stok      : {stok}")
    else:
        print("Barang tidak ditemukan.")

# -----------------------------------
# Fungsi: Tambah Barang Baru
# -----------------------------------
def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict
    """
    kode = input("Masukkan kode barang baru: ").strip()
    nama = input("Masukkan nama barang baru: ").strip()
    
    # Validasi kode tidak boleh duplikat
    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return

    # Input stok awal integer
    try:
        stok_awal = int(input("Masukkan stok awal : ").strip())
    except ValueError:
        print("Stok harus berupa angka.")
        return

    # Simpan ke dictionary
    stok_dict[kode] = {
        "nama" : nama,
        "stok" : stok_awal
    }

    print("Barang berhasil ditambahkan.")

# -----------------------------------
# Fungsi: Update Stok Barang
# -----------------------------------
def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah atau kurangi)
    Stok tidak boleh menjadi negatif
    """
    kode_barang = input("Masukkan kode barang yang ingin diupdate: ").strip()

    # Cek apakah kode barang ada di dictionary
    if kode_barang not in stok_dict:
        print("Kode barang tidak ditemukan.")
        return

    # Menu jenis update
    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    try:
        jumlah = int(input("Masukkan jumlah: ").strip())
    except ValueError:
        print("Jumlah harus berupa angka.")

    if pilihan == "1":
        stok_dict[kode_barang]["stok"] += jumlah
        print("Stok berhasil ditambahkan.")
    elif pilihan == "2":
        if stok_dict[kode_barang]["stok"] - jumlah < 0:
            print("Error: Stok tidak boleh negatif.")
            return
        stok_dict[kode_barang]["stok"] -= jumlah
        print("Stok berhasil dikurangi.")
    else:
        print("Pilihan tidak valid.")
    
# -----------------------------------
# Fungsi: Program Utama
# -----------------------------------
def main():
    # Membaca data dari file saat program dimulai
    stok_barang = baca_stok(nama_file)

    while True:
        print("\n=== MENU STOK KANTIN ===") 
        print("1. Tampilkan semua barang") 
        print("2. Cari barang berdasarkan kode") 
        print("3. Tambah barang baru") 
        print("4. Update stok barang") 
        print("5. Simpan ke file") 
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_stok(nama_file, stok_barang)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()


