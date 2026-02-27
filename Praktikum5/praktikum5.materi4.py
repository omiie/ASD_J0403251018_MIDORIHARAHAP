#---------------------------------------------------------------------------
#Nama   : Midori Harahap
#NIM    : J0403251018
#Kelas  : TPL A2/P2
#--------------------------------------------------------------------------- 

#--------------------------------------------------------------------------- 
#Contoh Bactracking 1: Kombinasi Biner(n)
#--------------------------------------------------------------------------- 

def biner(n, hasil=""):
    #Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return

    #Choose + explore: tambah '0'
    biner(n, hasil + "0")

    #Choose + explore: tambah '1'
    biner(n, hasil + "1")

biner(3)