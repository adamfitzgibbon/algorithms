"""Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node."""

class Node:
    next = None
    def __init__(self, data):
        self.data = data

def delete_middle_node(node):
    if node.next is not None and node.next.next is not None:
        node.next = node.next.next

head = Node(0)
node = head
for i in range(5):
    node.next = Node(i)
    node = node.next

delete_middle_node(head)

node = head
while node is not None:
    print(node.data)
    node = node.next

#TODO: rework this one. You are NOT given the head node