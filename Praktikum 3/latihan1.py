# ==========================================================
# TUGAS LINKED LIST DALAM PYTHON
# Latihan : 1, 2, 4
#
# Nama  : Midori Harahap
# NIM   : J0403251018
# Kelas : TPL A2/P2
# ==========================================================

# Latihan 1: Implementasikan fungsi untuk menghapus node dengan nilai tertentu.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head

        # Menghapus node head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Elemen tidak ditemukan")
            return
        
        prev.next = temp.next
        temp = None
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# Implementasi
sll = SingleLinkedList()
for i in [10, 20, 30, 40]:
    sll.insert(i)

print("Sebelum dihapus:")
sll.display()

sll.delete_node(30)

print("Setelah dihapus:")
sll.display()