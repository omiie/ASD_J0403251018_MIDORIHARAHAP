#---------------------------------------------------------------------------
#Nama   : Midori Harahap
#NIM    : J0403251018
#Kelas  : TPL A2/P2
#--------------------------------------------------------------------------- 

#--------------------------------------------------------------------------- 
#Implementasi Dasar : Node pada Linked List
#--------------------------------------------------------------------------- 

class Node:
    #Konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__ (self, data):
        self.data = data #Menyimpan nilai atau data pada list
        self.next = None #Pointer ini menunjukk ke note berikutnya (awal=None)

#1) Membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) Menghubungkan node: A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3) Traversal : Menelusuri node dari head sampai ke None
current = head
while current is not None:
    print(current.data) #Menampilkan data pada node saat ini
    current = current.next #Pindah ke node berikutnya

#--------------------------------------------------------------------------- 
#Implementasi Dasar : Stack
#--------------------------------------------------------------------------- 