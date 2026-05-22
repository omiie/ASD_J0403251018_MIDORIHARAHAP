# Nama  : Midori Harahap
# NIM   : J0403251018
# Kelas : TPL A2
# Praktikum 12 - Graph II : Shortest Path 
# Latihan 3 : Implementasi Bellman-Ford

# ========================================================== 
# Latihan 3: Implementasi Bellman-Ford 
# ========================================================== 
# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start ke seluruh node
    lain menggunakan algoritma Bellman-Ford
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika jarak ke node saat ini sudah diketahui dan ditemukan jarak yang lebih kecil ke neighbor
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    return distances
                
hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A: ")
for node, distances in hasil.items():
    print(node, "=", distances)

# Jawaban Analisis
# 1. Berapa bobot langsung dari A ke B? 5
# 2. Berapa total bobot jalur A -> C -> B? 2
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B? Jalur A -> C -> B karena total bobotnya 2, lebih kecil dari 5
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif? Karena Bellman-Ford teta dapat menghitung jarak terpendek meski terdapat edge dengan bobot negatif
# 5. Apa yang dimaksid dengan proses relaksasi edge? Relaksasi edge adalah proses memperbarui jarak node jika ditemukan dengan jalur yang lebih pendek
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra? Bellman-Ford dapat menangani bobot negatif, sedangkan Dijkstra tidak. Selain itu Bellman-Ford lebih lambat dibanding Dijkstra karena harus menyusuri dan membandingkan jarak/bobot node