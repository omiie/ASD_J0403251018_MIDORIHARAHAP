#---------------------------------------------------------------------------
#Nama   : Midori Harahap
#NIM    : J0403251018
#Kelas  : TPL A2/P2
#--------------------------------------------------------------------------- 

#--------------------------------------------------------------------------- 
#Studi Kasus: Generator PIN
#--------------------------------------------------------------------------- 

def buat_pin(panjang, hasil=""):
    #Base case: jika panjang string hasil sama dengan panjang (len(hasil == panjang)), maka PIN
    #yang terbentuk dicetak menggunakan print("PIN:", hasil) dan rekursi berhenti dengan return
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    #Recursive case: fungsi buat_pin akan memanggil dirinya sendiri dengan panjang dan hasil yang bertambah
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)

print("BUAT PIN")
buat_pin(3)

"""
Untuk mencegah angka yang sama berulang dalam PIN, tambahkan pengecekan angka sebelumnya di dalam recursive call.
pastikan bahwa angka tersebut tidak sama dengan angka terakhir yang ada dalam string hasil.
"""

#Perbaikan code angka tidak berulang dalam PIN
def buat_pin_unik(panjang, hasil=""):
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return

    for angka in ["0", "1", "2"]:
        #Cek apakah angka yang ditambahkan sama dengan angka terakhir
        if len(hasil) == 0 or angka != hasil[-1]:
            buat_pin_unik(panjang, hasil + angka)

print("BUAT PIN UNIK")
buat_pin_unik(3)