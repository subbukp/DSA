class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

def insert(head, key):
    if head is None:
        head = Node(key)
        return head
    if key < head.key:
        head.left = insert(head.left, key)
    else:
        head.right = insert(head.right, key)
    return head

def inOrder(head):
    if head:
        inOrder(head.left)
        print(f"{head.key} ->", end = "")
        inOrder(head.right)

def preOrder(head):
    if head:
        print(f"{head.key} ->", end = "")
        preOrder(head.left)
        preOrder(head.right)

# Example
root = Node(50)
insert(root, 30)
insert(root, 70)
insert(root, 20)
insert(root, 40)
insert(root, 60)
insert(root, 80)
insert(root, 8)
inOrder(root)
print()
preOrder(root)
