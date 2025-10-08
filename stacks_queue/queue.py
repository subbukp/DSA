from collections import deque

class queue:
    def __init__(self, size):
        self.queue_collection = deque()
        self.size = size
    
    @property
    def isFull(self) -> bool:
        if len(self.queue_collection) < self.size:
            return False
        return True
    
    @property
    def isEmpty(self) -> bool:
        if len(self.queue_collection) <= 0:
            return True
        return False

    def push(self, key: int):
        if not self.isFull:
            self.queue_collection.append(key)
            return
        print("Its full")
        
    @property
    def pop(self):
        if not self.isEmpty:
            print(f"Poped item:{self.queue_collection[0]}")
            self.queue_collection.popleft()
            return
        print("No item to pop")

    @property
    def print_queue(self):
        print(f'queue: {self.queue_collection}')

q =queue(2)
q.pop
q.push(1)
q.push(2)
q.push(3)
q.pop
q.print_queue