#---------------------------------------------------------------------------
#Nama   : Midori Harahap
#NIM    : J0403251018
#Kelas  : TPL A2/P2
#--------------------------------------------------------------------------- 

#--------------------------------------------------------------------------- 
#Latihan 2: Tracing Rekursi
#--------------------------------------------------------------------------- 

def countdown(n):
    if n == 0:
        print("Selesai")
        return

    print("Masuk: ", n)
    countdown(n-1)
    print("Keluar: ", n)

countdown(3)

"""
Alur keluar dalam rekursi terbalik karena rekursi bekerja dalam dua fase: winding(pemanggilan) dan unwinding(pengembalian)
countdown(3) berarti fungsi memanggil dirinya sendiri sampai mencapai kondisi dasar (n==0). setelah mencapai base case,
eksekusi kembali ke pemanggil sebelumnya
"""