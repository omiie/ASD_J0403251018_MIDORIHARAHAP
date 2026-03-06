#---------------------------------------------------------------------------
#Nama   : Midori Harahap
#NIM    : J0403251018
#Kelas  : TPL A2/P2
#--------------------------------------------------------------------------- 

#--------------------------------------------------------------------------- 
#Implementasi Bubble Sort (Descending)
#--------------------------------------------------------------------------- 

#cara kerja: membandingkan dua elemen yang berdekatan lalu menukarnya jika urutannya salah, proses dilakukan berulang ulang sampai data terurut
#bubble (gelembung): karena nilai yang lebih besar akan menggelembung naik ke posisi akhir pada setiap iterasi
#menukar elemen bersebelahan

def bubbleSort(data):
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i] < data[i+1]:
                #tukar dua data bersebelahan yang ututannya salah
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp

data = [54,26,93,17,77,31,44,55,20]
bubbleSort(data)
print(data)

#tambahkan flag exchanges pada program
#flag bernilai True apabila pada iterasi sebelumnya terdapat setidaknya sekali penukaran
#flag bernilai False apabila pada iterasi sebelumnya sama sekali tidak terdapat pertukaran, program pim akan berhenti dengan sendirinya

def shortBubblesort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] < alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum-1

alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
shortBubblesort(alist)
print(alist)