#---------------------------------------------------------------------------
#Nama   : Midori Harahap
#NIM    : J0403251018
#Kelas  : TPL A2/P2
#--------------------------------------------------------------------------- 

#--------------------------------------------------------------------------- 
#Latihan 3: Mencari Nilai Maksimum
#--------------------------------------------------------------------------- 

def cari_maks(data, index=0): #Mencari nilai maksimum dari elemen daftar data, dimulai dari index = 0 (index pertama)
    #Base case: ketika fungsi mencapai elemen terakhir dari daftar data, fungsi mengembalikkan elemen terakhir sebagai nilai max
    if index == len(data) - 1:
        return data[index]

    #Recursive case: memecah masalah menjadi masalah yang lebih kecul kemudian membandingkan elemen saat ini dengan hasil rekursi dan mengembalikkan nilai yang lebih besar
    maks_sisa = cari_maks(data, index + 1)

    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))