#---------------------------------------------------------------------------
#Nama   : Midori Harahap
#NIM    : J0403251018
#Kelas  : TPL A2/P2
#--------------------------------------------------------------------------- 

#--------------------------------------------------------------------------- 
# Contoh 1: Faktorial
#--------------------------------------------------------------------------- 

def faktorial(n):
    #Base case: berhenti ketika n = 0
    if n == 0:
        return 1
    
    #Recursive case: masalah diperkecil menjadi faktorial(n-1)
    return n * faktorial(n-1)

print("Faktorial(5) =",faktorial(5)) # Output: 120