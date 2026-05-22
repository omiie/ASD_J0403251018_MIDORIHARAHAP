# Nama  : Midori Harahap
# NIM   : J0403251018
# Kelas : TPL A2
# Praktikum 12 - Graph II : Shortest Path 
# Latihan 5: Studi Kasus dengan Program Shortest Path

# Mencari jarak terpendek dari Bogor ke semua kota dengan algoritma Dijkstra
# Bogor ➔ Jakarta = 5 
# Bogor ➔ Depok = 2 
# Depok ➔ Jakarta = 2 
# Depok ➔ Bandung = 6
# Jakarta ➔ Bandung = 7 

# Representasi graph berbobot menggunakan dictionary
import heapq
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# Fungsi Dijktra
def dijkstra(graph, start):
    # Menyimpan jarak minimum
    distances = {node: float('inf') for node in graph}

    # Jarak node awal = 0
    distances[start] = 0

    # Priority queue
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

# Input node awal atau minimal penentuan node awal dalam program
# Output jarak terpendek dari node awal ke semua node
hasil = dijkstra(graph, 'Bogor')

print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print('Bogor ->', kota, "=", jarak)

# Jawaban Analisis
# 1. Node awal yang digunakan apa? Bogor
# 2. Node mana yang memiliki jarak paling kecil dari node awal? Depok dengan jarak 2
# 3. Node mana yang memiliki jarak paling besar dari node awal? Bandung dengan jarak 8
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat. 
# Algoritma Dijkstra bekerja dengan mencari jalur dengan total bobot paling kecil dari node awal ke node lainnya, Algoritma memeriksa setiap tetangga node
# memperbarui jarak bila ditemukan jalur lebih pendek lalu memproses node dengan jarak terkecil terlebih dahulu hingga semua node mendapat jarak minimum