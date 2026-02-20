#---------------------------------------------------------------------------
#Nama   : Midori Harahap
#NIM    : J0403251018
#Kelas  : TPL A2/P2
#--------------------------------------------------------------------------- 

#--------------------------------------------------------------------------- 
#Implementasi Dasar : Stack
#--------------------------------------------------------------------------- 

class Node:
    #Konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__ (self, data):
        self.data = data #Menyimpan nilai atau data pada list
        self.next = None #Pointer ini menunjukk ke note berikutnya (awal=None)

#Stack ada operasi push(masukkin head baru) dan pop(menghapus head)
class Stack:
    def __init__ (self): #Memasukkan data baru pada stack
        self.top = None #Top menunjuk ke nide paling atas(awal=None)

    def is_empty(self):
        return self.top is None
    
    def push(self,data):
        #1) Membuat node baru
        nodeBaru = Node(data) #Instansiasi/memanggil konstruktor node pada class Node

        #2) Node baru harus menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top

        #3) Geser top pindah ke node baru
        self.top = nodeBaru

        #B -> A -> None

    def pop(self): #Mengambil dan menghapus node palinga atas(top/head)
        if self.is_empty():
            print("Stack kosong. Tidak bisa pop")
            return None

        data_terhapus = self.top.data # soroti bagian top dan simpan di variabel (peak)
        # B -> A -> None
        self.top = self.top.next
        return data_terhapus
        #A -> None

    def peek(self):
        #Melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data

    def tampilkan(self):
        current = self.top
        print("Top ",  end="-> ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#Instantiasi class Stack
s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
s.pop()
s.tampilkan()
s.pop()
s.tampilkan()
s.pop()
s.tampilkan()
print("Peek (Lihat Top): ", s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat Top): ", s.peek())
