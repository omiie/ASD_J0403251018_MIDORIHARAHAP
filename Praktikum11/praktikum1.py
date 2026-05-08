#----------------------------------
# Praktikum 1
# Nama  = Midori Harahap
# NIM   = J0403251018
# Kelas = TPL A2
#----------------------------------

def createGraph(V, edges):
    """
    Fungsi untuk membuat adjacency matrix
    """
    #Membuat matrix berukuran V x V dan semua isi awalnya 0 (belum ada hubungan antar node)
    mat = [[0 for _ in range(V)] for _ in range(V)]

    #Perulangan untuk setiap edge pada list edges
    for it in edges:
        u = it[0] #Mengambil node awal
        v = it[1] #Mengambil node tujuan
        mat[u][v] = 1 #Menandai bahwa node u terhubung ke node v
        mat[v][u] = 1 #Karena graph bersifat undirected (dua arah) maka v juga terhubung ke u
    return mat #Mengembalikan adjacency matrix yang sudah dibuat

#Program utama
if __name__ == "__main__":
    V = 4 #Jumlah vertex dalam graph

    #Daftar edge antar vertex
    edges = [[0,1], [0,2], [1,2], [3,2]]

    #Membuat graph dalam bentuk adjacency matrix
    mat = createGraph(V, edges)

    #Menampilkan output
    print("Adjacency Matrix Representation:")
    for i in range(V): #Perulangan untuk menampilkan matrix
        for j in range(V): #Perulangan kolom pada setiap baris
            print(mat[i][j], end=" ") #Menampilkan nilai matrix
        print() #Pindah baris setelah semua kolom ditampilkan