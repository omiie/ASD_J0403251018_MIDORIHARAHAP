#---------------------------------------------------------------------------
#Nama   : Midori Harahap
#NIM    : J0403251018
#Kelas  : TPL A2/P2
#--------------------------------------------------------------------------- 

#--------------------------------------------------------------------------- 
#Latihan Soal Pengurutan
#--------------------------------------------------------------------------- 

"""
Pak Budi adalah seorang manager sumber daya manusia di suatu perusahaan. Ia
saat ini harus menseleksi pelamar kerja berdasarkan skor tes potensi akademik
mereka. Skor tersebut disajikan dalam bentuk list dengan rentang nilai 0 - 100.
Berikut adalah data hasil tes potensi akademik yang tersedia:

[43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

Soal:
1. Jika Pak Budi akan meloloskan lima kandidat dengan nilai tertinggi, tuliskanlah
skor lima kandidat tersebut dari yang paling tinggi hingga terendah.
2. Kandidat berapa saja yang lolos?
"""

# Data skor tes
scores = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

# Membuat pasangan (nomor kandidat, skor)
data = [(i+1, scores[i]) for i in range(len(scores))]

def mergeSort(data):
    if len(data) > 1:
        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i][1] > right[j][1]:  # bandingkan skor (descending)
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1


mergeSort(data)

print("Data setelah diurutkan:", data)

# Ambil 5 kandidat terbaik
top5 = data[:5]

print("\n5 skor tertinggi:")
for kandidat, skor in top5:
    print("Kandidat", kandidat, "dengan skor", skor)
