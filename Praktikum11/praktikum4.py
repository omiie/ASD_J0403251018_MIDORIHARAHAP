#----------------------------------
# Praktikum 4
# Nama  = Midori Harahap
# NIM   = J0403251018
# Kelas = TPL A2
#----------------------------------

#Studi Kasus Dunia Nyata

#=======================================
#Langkah 1 - Tentukan Studi Kasus
#=======================================
#NIM J0403251018 maka studi kasusnya Peta Kota

#=======================================
#Langkah 2- Tentukan Node dan Edge
#=======================================
#Vertex
#Bogor, Jakarta, Depok, Tanggerang, Bekasi

#Edge
#Bogor <-> Jakarta
#Bogor <-> Depok
#Jakarta <-> Tanggerang
#Jakarta <-> Bekasi
#Depok <-> Bekasi

#=======================================
#Langkah 3 - Gambar Desain Graph
#=======================================

#=======================================
#Langkah 4 - Implementasi dalam Python
#=======================================

#Daftar kota (vertex)
perkotaan = ["Bogor", "Jakarta", "Depok", "Tanggerang", "Bekasi"] 

V = len(perkotaan) #Jumlah vertex

#Dictionary untuk idex kota agar nama kota bisa diakses menggunakan angka
indeks_kota = {
    "Bogor": 0,
    "Jakarta": 1,
    "Depok": 2,
    "Tanggerang": 3,
    "Bekasi": 4
}

#Daftar jalan antar kota (edge)
jalan = [
    ("Bogor", "Jakarta"),
    ("Bogor", "Depok"),
    ("Jakarta", "Tanggerang"),
    ("Jakarta", "Bekasi"),
    ("Depok", "Bekasi")
]

#----------------------------------
#Membuat Adjacency Matrix
#----------------------------------
matrix = [[0 for _ in range(V)] for _ in range(V)] #Membuat matrix kosong ukuran V x V

#Menambahkan edge ke matrix
for u, v in jalan:
    #Mengubah nama kota menjadi index angka
    i = indeks_kota[u]
    j = indeks_kota[v]

    #Hubungan dua arah (undirected)
    matrix[i][j] = 1
    matrix[j][i] = 1

#----------------------------------
#Membuat Adjacency List
#----------------------------------
adj = {} #Membuat dictionary kosong

#Membuat list kosong untuk setiap kota
for kota in perkotaan:
    adj[kota] = []

#Menambahkan hubungan antarkota
for u, v in jalan:
    adj[u].append(v) #Menambahkan kota tujuan ke kota asal
    adj[v].append(u) #Menambahkan kota asal ke kota tujuan karena undirected

#=======================================
#Langkah 5 - Tampilkan Output Program
#=======================================

#Menampilkan nama node
#----------------------------------
print("DAFTAR NAMA KOTA")
for kota in perkotaan:
    print("-", kota)
print()

#Menampilkan Hubungan antar node
#----------------------------------
print("HUBUNGAN ANTAR KOTA")
for u, v in jalan:
    print(f"{u} <--> {v}")
print()

#Menampilkan adjacency matrix
#----------------------------------
print("ADJACENCY MATRIX")
print("                 ", end="")
for kota in perkotaan:
    print(f"{kota:12}", end=" ")
print()

#Menampilkan list matrix
for i in range(V):
    print(f"{perkotaan[i]:12}", end="") #Menampilkan nama kota pada baris
    
    #Menampilkan isi matrix
    for j in range(V):
        print(f"{matrix[i][j]:12}", end="")
    print()
print()

#Menampilkan adjacency list
#----------------------------------
print("ADJACENCY LIST")
#Menampilkan adjacency list tiap kota
for kota in adj:
    print(f"{kota}:", end=" ")

    for j in adj[kota]:
        print(j, end=" ")
    print()

#=======================================
#Langkah 6 - Analisis Singkat
#=======================================
# Graph pada kasus peta jalan dengan kota sebagai verteks dan jalan sebagai edge
# Representasi dengan adjacency matrix digunakan untuk melihat hubungan antar kota dengan mengecek nilai 0 atau 1 pada matriks
# Representasi dengan adjacency list hanya menampilkan daftar kota yang benar-benar terhubung
# Maka, pada studi kasus ini yang paling efisien bagi user adalah adjacency list karena menampilkan jumlah jalan lebih sedikit sehingga mudah dipahami dibandingkan dengan menampilkan seluruh hubungan antar kota
