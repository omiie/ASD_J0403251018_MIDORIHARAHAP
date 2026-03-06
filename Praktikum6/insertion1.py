#---------------------------------------------------------------------------
#Nama   : Midori Harahap
#NIM    : J0403251018
#Kelas  : TPL A2/P2
#--------------------------------------------------------------------------- 

#--------------------------------------------------------------------------- 
#Implementasi Insertion Sort (Ascending)
#--------------------------------------------------------------------------- 

#cara kerja: membandingkan dan mengurutkan dua data pertama pada list, kemudian membandingkan data pada list berikutnya apakah sudah berada di tempat semestinya
#insertion karena setiap langkah memasukkan elemen pada posisi yang sesuai
#menyisipkan elemen ke posisi yang benar

def insertionSort(data):
    for index in range(1, len(data)):

        currentvalue = data[index]
        position = index

        while position>0 and data[position-1] > currentvalue:
            data[position] = data[position-1]
            position = position-1
        data[position] = currentvalue

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(data)
print(data)