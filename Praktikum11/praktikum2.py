#----------------------------------
# Praktikum 1
# Nama  = Midori Harahap
# NIM   = J0403251018
# Kelas = TPL A2
#----------------------------------

def createGraph(edges):
    """
    Fungsi untuk membuat adjacency list
    """
    adj = {} #Dictionary kosong untuk menyimpan graph

    #Melakukan perulangan pada setiap edge
    for it in edges:
        u = it[0] #Mengambil node asal
        v = it[1] #Mengambil node tujuan

        if u not in adj: #Jika node u belum ada di dictionary maka buat list kosong dulu
            adj[u] = []

        if v not in adj: #Jika node v belum ada di dictionary maka buat list kosong dulu
            adj[v] = []

        adj[u].append(v) #Menambahkan v ke daftar tetangga u
        adj[v].append(u) #Menambahkan u ke daftar tetangga v
    return adj #Mengembalikan adjacency list

#Program utama
if __name__ == "__main__":
    V = 4

    #List edge antar node menggunakan huruf sebagai node
    edges = [
        ["A", "B"], 
        ["A", "C"], 
        ["B", "D"], 
        ["C", "D"]
        ]

    adj = createGraph(edges) #Membuat graph

    print("Adjacency List Representation:") #Menampilkan adjacency list
    #Perulangan untuk setiap node pada dictionary
    for i in adj:
        print(f"{i}:", end=" ") #Menampilkan nama node
        for j in adj[i]: #Menampilkan semua tetangga node
            print(j, end=" ")
        print()