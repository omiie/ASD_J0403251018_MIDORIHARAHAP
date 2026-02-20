# ==========================================================
# TUGAS LINKED LIST DALAM PYTHON
# Latihan : 1, 2, 4
#
# Nama  : Midori Harahap
# NIM   : J0403251018
# Kelas : TPL A2/P2
# ==========================================================

# Latihan 2: Buat kode Implementasikan Pencarian pada node tertentu Single
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def search(self, key):
        if self.head is None:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari")
            return

        temp = self.head

        while True:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List")
                return
            temp = temp.next
            if temp == self.head:
                break

        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List")

# Tampilan 1
cll = CircularLinkedList()
for i in [3,7,12,19,25]:
    cll.insert(i)

cll.search(12)

# Tampilan 2
cll2 = CircularLinkedList()
for i in [5,10,15,20,30]:
    cll2.insert(i)

cll2.search(25)

# Tampilan 3
cll3 = CircularLinkedList()

cll3.search(10)