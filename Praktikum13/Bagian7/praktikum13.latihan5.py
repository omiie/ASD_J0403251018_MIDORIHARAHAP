# Nama  : Midori Harahap
# NIM   : J0403251018
# Kelas : TPL A/2
# Latihan 4 - Tugas Mandiri: Buat Program MST dengan Kasus Baru

# ========================================================== 
# Tugas Mandiri: Buat Program MST dengan Kasus Baru
# ==========================================================

# Kasus 2. Jaringan Komputer
# Representasi weighted graph
import heapq

graph = { 
    'RouterA': {'RouterB': 3, 'RouterC': 2}, 
    'RouterB': {'RouterA': 3, 'RouterC': 4, 'RouterD': 5}, 
    'RouterC': {'RouterA': 2, 'RouterB': 4, 'RouterD': 1}, 
    'RouterD': {'RouterB': 5, 'RouterC': 1} 
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
mst, total = prim(graph, 'RouterA')

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

# Output total biaya minimum
print("Total bobot =", total)

# ========================================================== 
# Pertanyaan Analisis
# ==========================================================
# 1. Kasus apa yang dipilih? Kasus Jaringan Komputer
# 2. Algoritma apa yang digunakan? Algoritma Prim
# 3. Edge mana saja yang dipilih dalam MST? RouterA - RouterC, RouterC - RouterD, dan RouterA - RouterB
# 4. Berapa total bobot MST? 6
# 5. Mengapa edge tertentu tidak dipilih? Karena edge tertentu sudah terhubung dengan edge yang dipilih sebelumnya. Jika tetap dipilih maka akan ada cycle yang mengakibatkan tidak efektifnya edge dan biaya tidak minimum