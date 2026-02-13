# ==========================================================
# TUGAS LINKED LIST DALAM PYTHON
# Latihan : 1, 2, 4
#
# Nama  : Midori Harahap
# NIM   : J0403251018
# Kelas : TPL A2/P2
# ==========================================================

# Latihan 4: Buat metode untuk menggabungkan dua single linked list menjadi satu
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class MergeLinkedList:
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
    def display(self):
        if self.head is None:
            print("Kosong")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def merge(self, list1, list2):
        merged_list = MergeLinkedList()

        temp = list1.head
        while temp:
            merged_list.insert(temp.data)
            temp = temp.next

        temp = list2.head
        while temp:
            merged_list.insert(temp.data)
            temp = temp.next
        
        return merged_list

# Tampilan 1
list1 = MergeLinkedList()
list2 = MergeLinkedList()

for i in [1,3,5,7]:
    list1.insert(i)

for i in [2,4,6,8]:
    list2.insert(i)

print("Linked List 1: ")
list1.display()

print("Linked List 2: ")
list2.display()

merged = MergeLinkedList().merge(list1, list2)
print("Linked List setelah digabungkan: ")
merged.display()
print(" ")

# Tampilan 2
list3 = MergeLinkedList()
list4 = MergeLinkedList()

for i in [5,15,25]:
    list3.insert(i)

print("Linked List 1: ")
list3.display()

print("Linked List 2: ")
list4.display()

merged2 = MergeLinkedList().merge(list3, list4)
print("Linked List setelah digabungkan: ")
merged2.display()
print(" ")
