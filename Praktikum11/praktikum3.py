#----------------------------------
# Praktikum 3
# Nama  = Midori Harahap
# NIM   = J0403251018
# Kelas = TPL A2
#----------------------------------

#Konversi Matrix ke List
def matrixToList(matrix):
    """
    Fungsi mengubah adjacency matrix ke adjacency list
    """

    adj = {}  #Membuat dictionary kosong untuk menyimpan adjacency list
    V = len(matrix) #Mengambil jumlah vertex

    #Perulangan untuk setiap baris matrix
    for i in range(V):
        adj[i] = [] #Membuat list kosong untuk tetangga node i

        #Perulangan untuk setiap kolom
        for j in range(V):
            if matrix[i][j] == 1: #Jika bernilai 1 berarti ada edges
                adj[i].append(j) #Tambahkan node j ke adjacency list node i
    return adj #Mengembalikan adjacency list

#Program utama
if __name__ == "__main__":

    #Adjacency matrix yang mau diubah
    matrix = [
        [0,1,1,0],
        [1,0,1,0],
        [1,1,0,1],
        [0,0,1,0]
    ]

    adj = matrixToList(matrix) #Mengubah matrix menjadi list

    print("Adjacency List Representation:") #Menampilkan hasil adjacency list
    for i in adj: #Perulangan setiap node
        print(f"{i}: ", end=" ") #Menampilkan node

        for j in adj[i]: #Menampilkan tetangga node
            print(j, end=" ")
        print()

