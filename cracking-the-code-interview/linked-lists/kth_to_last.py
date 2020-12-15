"""Implement an algorithm to find the kth to last element of a singly linked list"""

class Node:
    next = None
    def __init__(self, data):
        self.data = data

def kth_to_last(node, k):
    l = []
    if k <= 0:
        return None
    while node is not None:
        l.append(node)
        node = node.next
    return l[len(l)-k]

head = Node(0)
node = head
for i in range(5):
    node.next = Node(i)
    node = node.next

assert kth_to_last(head, 0) is None
assert kth_to_last(head, 4).data == 1