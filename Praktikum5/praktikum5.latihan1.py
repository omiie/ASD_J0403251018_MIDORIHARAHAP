#---------------------------------------------------------------------------
#Nama   : Midori Harahap
#NIM    : J0403251018
#Kelas  : TPL A2/P2
#--------------------------------------------------------------------------- 

#--------------------------------------------------------------------------- 
#Latihan 1: Rekursi Pangkat
#--------------------------------------------------------------------------- 

def pangkat(a, n):
    #Base case: ketika n == 0 kembalikan 1
    if n == 0:
        return 1

    #Recursive case: memanggil dirinya sendiri dengan nilai n sampai akhirnya mencapai base case di n == 0.
    return a * pangkat(a, n-1)

print(pangkat(2, 4)) #Output: 16

"""
Fungsi pangkat(a, n) menggunakan rekursi untuk menghitung pangkat dari suatu angka a dengan eksponen n, yaitu a^n.
Fungsi bekerja dengan cara memanggil dirinya sendiri hingga mencapai base case kemudian mengembalikkan hasil
"""