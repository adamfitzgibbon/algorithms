"""You have two numbers represented by a linked list, where each node contains a single digit. 
The digits are stored in reverse order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
(You are not allowed to "cheat" and just convert the linked list to an integer.)

Follow Up: Suppose the digts are stored in forward order. Repeat the above problem"""

class Node:
    next = None
    def __init__(self, data):
        self.data = data

def sum_lists(node1, node2):
    pass

head = Node(3)
node = head
for i in [5,8,5,10,2,1]:
    node.next = Node(i)
    node = node.next

# TODO: follow up