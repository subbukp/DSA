from collections import deque

class stack:
    def __init__(self, size):
        self.stack_collection = deque()
        self.size = size

    def isFull(self):
        if len(self.stack_collection) < self.size:
            print(len(self.stack_collection))
            return True
        return False
    def push(self, value):
        a = self.isFull()
        if a:
            self.stack_collection.append(value)
            return
        print("stack is full!!!")

    def pop(self):
        if len(self.stack_collection) == 0:
            print("empty stack")
            return
        print(f"Popped value: {self.stack_collection[-1]}")
        self.stack_collection.pop()

    def print_val(self):
        print(f"Top element: {self.stack_collection[-1]}")

a = stack(5)
a.pop()
a.push(10)
a.push(20)
a.push(30)
a.push(40)
a.push(50)
a.push(60)
a.print_val()
#a.print_val()
#a.pop()
#a.print_val()
#a.pop()
#a.print_val()