#---------------------------------------------------------------------------
#Nama   : Midori Harahap
#NIM    : J0403251018
#Kelas  : TPL A2/P2
#--------------------------------------------------------------------------- 

#--------------------------------------------------------------------------- 
#Latihan 4: Kombinasi Huruf
#--------------------------------------------------------------------------- 

def kombinasi(n, hasil=""):
    #Base case: ketika panjang string hasil == n maka mencetak string hasil
    if len(hasil) == n:
        print(hasil)
        return

    #Recursive case: jika panjang string hasil belum mencapai n, fungsi akan:
    #Menambahkan "A" ke string hasil dan memanggil kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "A")
    #Menambahkan "B" ke string hasil dan menambahkan kombinasi(n, hasil + "B")
    kombinasi(n, hasil + "B")

kombinasi(2)
