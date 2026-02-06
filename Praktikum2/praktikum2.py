#---------------------------------------------------------------------------
# Praktikum 2 : Konsep ADT dan File Handling (Studi Kasus)
# Latihan 1 : Membuat Fungsi Load Data
#---------------------------------------------------------------------------

# variabel menyimpan data file
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} #inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #ambil data perbaris dan hilangkan new line
            nim, nama, nilai = baris.split(",") #ambil data per item data
            data_dict[nim] = {"nama": nama, "nilai": int(nilai)} #masukkan dalam dictionary
    return data_dict

#buka_data = baca_data(nama_file)
#print("Jumlah data terbaca:", len(buka_data))

#---------------------------------------------------------------------------
# Praktikum 2 : Konsep ADT dan File Handling (Studi Kasus)
# Latihan 2: Membuat Fungsi Menampilkan Data
#---------------------------------------------------------------------------

def tampilkan_data(data_dict):
    #membuat header tabel
    print("======= DAFTAR MAHASISWA =======")
    print(f"{'NIM' : <10} | {'NAMA' : <10} | {'NILAI' : <10}")

    print("-"*35) #membuat garis

    #menampilkan isi datanya
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim : <10} | {nama : <10} | {int(nilai) : >5}")

#tampilkan_data(buka_data) #memanggil fungsi untuk menampilkan data

#---------------------------------------------------------------------------
# Praktikum 2 : Konsep ADT dan File Handling (Studi Kasus)
# Latihan 3: Membuat Fungsi Mencari Data
#---------------------------------------------------------------------------

#membuat fungsi pencarian data
def cari_data(data_dict):
    #pencarian data berdasarkan nim sebagai key dictionary
    #membuat input nim mahasiswa yang akan dicari
    nim_cari = input("Masukkan NIM mahasiswa yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("======= Data Mahasiswa Ditemukan =======")
        print(f"NiM       : {nim_cari}")
        print(f"Nama      : {nama}")
        print(f"Nilai     : {nilai}")
    else:
        print("Data tidak ditemukan. Pastikan nim yang dimasukkan benar")

#memanggil fungsi cari data
#cari_data(buka_data)

#---------------------------------------------------------------------------
# Praktikum 2 : Konsep ADT dan File Handling (Studi Kasus)
# Latihan 4: Membuat Fungsi Update Data
#---------------------------------------------------------------------------

#membuat fungsi update data
def ubah_data(data_dict):

    #awali dulu dengan mencari nim/data mahasiswa yang ingin diupdate
    nim = input("Masukkan NIM mahasiswa yang ingin diubah datanya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan")
        return

    try:
        nilai_baru = int(input("Masukkan nilai baru 0-100 : ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")

    if  nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100. Update dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#memanggil fungsi ubah data
#ubah_data(buka_data)

#---------------------------------------------------------------------------
# Praktikum 2 : Konsep ADT dan File Handling (Studi Kasus)
# Latihan 5: Membuat Fungsi Menyimpan Data pada File
#---------------------------------------------------------------------------

#membuat fungsi menyimpan data ke file
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

#memanggil fungsi simpan data
#simpan_data(nama_file, buka_data)
print("/nData Berhasil disimpan ke file", nama_file)

#---------------------------------------------------------------------------
# Praktikum 2 : Konsep ADT dan File Handling (Studi Kasus)
# Latihan 5: Membuat Menu Interaktif
#---------------------------------------------------------------------------

def main():
    #load data otomatis saat program dimulai
    buka_data = baca_data(nama_file)

    while True:
        print("======= MEMU DATA MAHASISWA =======")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Ubah Data Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan== "3":
            ubah_data(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
            print("Data berhasil disimpan")
        elif pilihan == "0":
            print("Program Selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

