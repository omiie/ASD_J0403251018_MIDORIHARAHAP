#---------------------------------------------------------------------------
#Nama   : Midori Harahap
#NIM    : J0403251018
#Kelas  : TPL A2/P2
#--------------------------------------------------------------------------- 

#--------------------------------------------------------------------------- 
#Implementasi Selection Sort (Ascending)
#--------------------------------------------------------------------------- 

#cara kerja: memilih elemen terkecil atau terbesar dari data yang belum terurut lalu menukarnya dengan posisi yang seharusnya
#selection karena setiap langkah menyeleksi elemen paling kecil atau besar
#memilih nilai terkecil dari sisa data

def selectionSort(data):
    for fillslot in range(len(data)-1,0,-1):
        positionofmax=0
        for location in range(1, fillslot+1):
            if data[location] > data[positionofmax]:
                positionofmax = location
            
            #swap
            temp = data[fillslot]
            data[fillslot] = data[positionofmax]
            data[positionofmax] = temp

data = [54,26,93,17,77,31,44,55,20]
selectionSort(data)
print(data)