# Nama  : Midori Harahap
# NIM   : J0403251018
# Kelas : TPL A/2
# Latihan 1 - Memahami Konsep Spanning Tree

# ========================================================== 
# Memahami Konsep Spanning Tree
# ========================================================== 

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D'),
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")

for edge in edges:
    print(edge)

print("\nSpanning Tree:")

for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph = ", len(edges))
print("Jumlah edge spanning tree = ", len(spanning_tree))

# ========================================================== 
# Pertanyaan Analisis
# ========================================================== 
# 1. Apa perbedaan graph awal dan spanning tree? Graph awal terdiri dari semua edge yang terhubung sedangkan spanning tree adalah subgraph dari sebuah graph yang menghubungka seluruh node, tidak memiliki cycle, dan memiliki jumlah edge sebanyak jumlah node -1
# 2. Mengapa spanning tree tidak boleh memiliki cycle? Cycle dihindari dalam spanning tree karena menyebabkan penggunaan edge berlebih, meningkatkan biaya total, dan membuat koneksi tidak efisien
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit? Karena spanning tree menghubungkan seluruh node dengan menghindari cycle sehingga jumlah edge menjadi sebanyak jumlah node -1. Spanning Tree memperoleh koneksi paling efisien dengan biaya terkecil