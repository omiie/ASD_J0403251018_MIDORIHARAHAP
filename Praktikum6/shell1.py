#---------------------------------------------------------------------------
#Nama   : Midori Harahap
#NIM    : J0403251018
#Kelas  : TPL A2/P2
#--------------------------------------------------------------------------- 

#--------------------------------------------------------------------------- 
#Implementasi Shell Sort (Ascending)
#--------------------------------------------------------------------------- 

#cara kerja: membagi list menjadi beberapa sublist yang lebih kecil kemudian diurutkan secara terpisah menggunakan algoritma pengurutan insertion sort
#kemudian sublist tersebut digabungkan kembali
#shell: pengembangan dari insertion sort

def shellSort(data):
    sublistcount = len(data)//2

    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(data, startposition, sublistcount)
        
        print("After increments of size", sublistcount, "The list is", data)
        sublistcount = sublistcount // 2

def gapInsertionSort(data, start, gap):
    for i in range(start+gap, len(data), gap):
        currentvalue = data[i]
        position = i

        while position >= gap and data[position-gap] > currentvalue:
            data[position] = data[position-gap]
            position = position-gap

        data[position] = currentvalue

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(data)
print(data)