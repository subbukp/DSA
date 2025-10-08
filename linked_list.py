from typing import List
class Node:
    def __init__(self, data:int =  None,next=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head=None