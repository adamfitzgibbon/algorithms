"""Write code to remove duplicates from an unsorted linked list.
How would you solve this if a temporary buffer is not allowed?"""

class Node:
    next = None
    def __init__(self, data):
        self.data = data

def remove_dups(head):
    vals = set()
    prev = None
    current = head
    while current.next is not None:
        if current.data in vals:
            prev.next = current.next
        else:
            vals.add(current.data)
        prev = current
        current = current.next
    if current.data in vals:
        prev.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(2)

remove_dups(head)

current = head
while current.next is not None:
    print(current.data)
    current = current.next
print(current.data)

# for no buffer just loop through rest of list and check for duplicates (but this ends up being O(n^2) time)