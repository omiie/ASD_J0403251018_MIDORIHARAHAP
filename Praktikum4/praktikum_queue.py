#---------------------------------------------------------------------------
#Nama   : Midori Harahap
#NIM    : J0403251018
#Kelas  : TPL A2/P2
#--------------------------------------------------------------------------- 

#--------------------------------------------------------------------------- 
#Implementasi Dasar : Queue
#--------------------------------------------------------------------------- 

class Node:
    #Konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__ (self, data):
        self.data = data #Menyimpan nilai atau data pada list
        self.next = None #Pointer ini menunjukk ke note berikutnya (awal=None)

class queue:
    #Buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__ (self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def is_empty(self):
        return self.front is None

    #Membuat fungsi untuk menambahkan data baru
    def enqueue(self, data):
        nodeBaru = Node(data)
        
        #Jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        #Jika queue tidak kosong, maka rear akan menunjuk ke node baru
        self.rear.next = nodeBaru #Letakkan data baru setelahnya rear
        self.rear = nodeBaru #Jadikan data baru sebagai rear

    def dequeue(self):
        #Menghapus data dari depan/front
        data_terhapus = self.front.data #Lihat data paling depan
        #Geser front ke node berikutnya
        self.front = self.front.next

        #Jika setelah geser front menjadi none, maka queue juga kosong
        #Rear juga harus kosong
        if self.front is None:
            self.rear = None


    def tampilkan(self):
        current =  self.front
        print("Front ",  end="-> ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print(" Rear")

q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()