#---------------------------------------------------------------------------
#Nama   : Midori Harahap
#NIM    : J0403251018
#Kelas  : TPL A2/P2
#--------------------------------------------------------------------------- 

#--------------------------------------------------------------------------- 
# Contoh 2: Tracing Masuk/Keluar
#--------------------------------------------------------------------------- 

def hitung(n):
    #Base case
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk: ", n)     #Fase stacking
    print(n-1)              #Pemanggilang rekursif
    print("Keluar: ", n)    #Fase unwinding

hitung(3)