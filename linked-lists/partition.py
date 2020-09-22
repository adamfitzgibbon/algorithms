"""Write code to poartition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.
IMPORTANT: The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
The additional spacing the example below indicates the partition.)"""

class Node:
    next = None
    def __init__(self, data):
        self.data = data

def partition(head, part):
    prev = None
    current = head
    while current is not None:
        if current.data < part and prev is not None:
            prev.next = current.next
            current.next = head
            head = current
            current = prev.next
        else:
            prev = current
            current = current.next
    return head

head = Node(3)
node = head
for i in [5,8,5,10,2,1]:
    node.next = Node(i)
    node = node.next

head = partition(head, 5)

while head is not None:
    print(head.data)
    head = head.next