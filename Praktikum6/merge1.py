#---------------------------------------------------------------------------
#Nama   : Midori Harahap
#NIM    : J0403251018
#Kelas  : TPL A2/P2
#--------------------------------------------------------------------------- 

#--------------------------------------------------------------------------- 
#Implementasi Shell Sort (Ascending)
#--------------------------------------------------------------------------- 

#cara kerja: membagi daftar data(list) menjadi dua bagian yang lebih kecil, mengurutkan setiap bagian secara terpisah
#kemudian menggabungkan dua bagian yang telah diurutkan menjadi satu daftar data yang terurut

#dua tahap utama: 
#pembagian(divide): daftar data dibagi menjadi dua bagian yang sama besar
#penggabungan(conquer): dua bagian yang telah diurutkan digabungkan menjadi satu daftar yang terurut

def mergeSort(data):
    print("Splitting", data)
    if len(data) > 1:
        mid = len(data)//2
        lefthalf = data[:mid]
        righthalf = data[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0 
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                data[k]=lefthalf[i]
                i=i+1
            else:
                data[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            data[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            data[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging", data)

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(data)
print(data)
