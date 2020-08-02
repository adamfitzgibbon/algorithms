class LinkedList:
    def __init__(self, headValue):
        self._head = Node(headValue)

    def pop(self):
        prevItem, currentItem = self._findFoot()
        prevItem.next = None 
        return currentItem

    def append(self, value):
        _, currentItem = self._findFoot()
        currentItem.next = Node(value)

    def toString(self):
        currentItem = self._head
        s = f"[ {str(currentItem.value)}"
        while currentItem.next is not None:
            currentItem = currentItem.next
            s += f", {str(currentItem.value)}"
        s += " ]"
        return s

    def _findFoot(self):
        currentItem = self._head
        prevItem = None
        while currentItem.next is not None:
            prevItem = currentItem
            currentItem = currentItem.next
        return prevItem, currentItem

class Node:  
    def __init__(self, value):
        self.value = value
        self.next = None

ll = LinkedList("head")
for i in range(10):
    ll.append(i)
    if i == 5:
        print(ll.pop().value)

print(ll.toString())