# Nama  : Midori Harahap
# NIM   : J0403251018
# Kelas : TPL A/2
# Latihan 3 - Implementasi Algoritma Prim

# ========================================================== 
# Implementasi Algoritma Prim
# ==========================================================

import heapq

graph = { 
    'A': {'B': 4, 'C': 2, 'D': 5}, 
    'B': {'A': 4, 'D': 3}, 
    'C': {'A': 2, 'D': 1}, 
    'D': {'A': 5, 'B': 3, 'C': 1} 
} 

def prim(graph, start):
    visited = set([start])
    edges = []

    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)

            mst.append((u, v, weight))
            total_weight += weight

            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total)

# ========================================================== 
# Pertanyaan Analisis
# ==========================================================
# 1. Node awal apa yang digunakan? Node A
# 2. Edge mana yang dipilih pertama kali? A - C
# 3. Bagaimana Prim menentukan edge berikutnya? Dengan cara menghubungkan dengan edge yang memiliki bobot terkecil dan node yang belum terhubung juga menghindari cycle
# 4. Berapa total bobot MST yang dihasilkan? 6
# 5. Apa perbedaan pendekatan Prim dan Kruskal? Perbedaannya adalah Algoritma Kruskal bekerja dengan mengurutkan seluruh edge terlebih dahulu, proses sorting akan memerlukan waktu komputasi yang cukup besar jika jumlah edge sangat banyak
# Sedangkan Algoritma Prim adalah algoritma Minimum Spanning Tree (MST) yang bekerja dengan membangun spanning tree secara bertahap mulai dari satu node awal. Prim lebih berorientasi pada pengembangan tree dari node awal ke node-node di sekitarnya
# Algoritma kruskal cenderung kurang efisien dibandingkan algoritma prim karena harus memproses banyak edge secara global