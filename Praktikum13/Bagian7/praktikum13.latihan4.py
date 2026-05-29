# Nama  : Midori Harahap
# NIM   : J0403251018
# Kelas : TPL A/2
# Latihan 4 - Studi Kasus: Jaringan Kabel Antar Gedung

# ========================================================== 
# Studi Kasus: Jaringan Kabel Antar Gedung
# ==========================================================

# Representasi weighted graph
import heapq

graph = { 
    'A': {'B': 4, 'C': 2, 'D': 5}, 
    'B': {'A': 4, 'D': 3}, 
    'C': {'A': 2, 'D': 1}, 
    'D': {'A': 5, 'B': 3, 'C': 1} 
} 

# Implementasi Algoritma Prim
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

# Output edge yang dipilih
mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

# Output total biaya minimum
print("Total bobot =", total)

# ========================================================== 
# Pertanyaan Analisis
# ==========================================================
# 1. Algoritma apa yang digunakan? Algoritma Prim
# 2. Edge mana saja yang dipilih? Edge A - C, C - D, dan D - B
# 3. Berapa total biaya minimum? 6
# 4. Mengapa MST cocok digunakan pada kasus ini? Karena MST menghubungkan seluruh node tanpa membentuk cycle dan memiliki total bobot minimum dibandingkan kemungkinan spanning tree lainnya. Memperoleh koneksi paling efisien dengan biaya terkecil