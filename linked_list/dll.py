class Node:
    def __init__(self, key):
        self.value = key
        self.prev = None
        self.next = None

class dll:
    def __init__(self):
        self.head = None

    def insert_in_beg(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        new_node.next.prev = new_node
        self.head = new_node
    
    def insert_in_end(self,key):
        if self.head is None:
            self.insert_in_beg(key)
            return
        new_node = Node(key)
        itr = self.head
        while itr.next is not None:
            itr = itr.next
        itr.next = new_node
        new_node.prev = itr
    
    def traverse(self):
        itr = self.head
        while itr:
            print(f"{itr.value} -> ",end="")
            itr = itr.next
        print("None")

d = dll()
d.insert_in_beg(10)
d.insert_in_beg(20)
d.insert_in_end(30)
d.insert_in_beg(15)
d.insert_in_end(50)
d.traverse()