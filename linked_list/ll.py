class Node:
    def __init__(self, value:int) -> None:
        self.value = value
        self.next = None
    
class linked_list:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        next_node = Node(value)
        if self.head is None:
            self.head = next_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = next_node

    def traverse(self):
        last = self.head
        while last:
            print(f"{last.value}->",end="")
            last=last.next
        print("Null")

    def delete(self, value):
        temp = self.head
        if temp and temp.value == value:
            self.head = temp.next
            return
        prev = None
        while temp and temp.value != value:
            prev = temp
            temp = temp.next
        if temp == None:
            print('key not found')
            return
        prev.next = temp.next
        temp = None

l = linked_list()
l.append(10)
l.append(20)
l.append(30)
l.traverse()
l.delete(30)
l.traverse()