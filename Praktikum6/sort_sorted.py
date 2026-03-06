#---------------------------------------------------------------------------
#Nama   : Midori Harahap
#NIM    : J0403251018
#Kelas  : TPL A2/P2
#--------------------------------------------------------------------------- 

#--------------------------------------------------------------------------- 
#Fungsi sorted()
#--------------------------------------------------------------------------- 
a = [1,3,5,7,9,0,2,4,6,8]
print(sorted(a))
print(a) #sorted tidak mengubah data asli
#mengembalikan list baru yang sudah diurutkan
#bisa digunakan pada list, tuple, set, dan string

#--------------------------------------------------------------------------- 
#Fungsi sort()
#--------------------------------------------------------------------------- 
b = [1,3,5,7,9,0,2,4,6,8]
print(b)
b.sort()
print(b) #mengurutkan langsung pada data aslinya (in-place)
#tidak mengembalikan nilai baru (return None)
#hanya bisa digunakan pada list