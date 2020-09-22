"""A Python implementation of a Queue"""

class Node:
    next = None

    def __init__(self, data):
        self.data = data

class Queue:
    _head = None
    _tail = None

    def __init__(self, *args):
        if len(args) > 0:
            self._head = Node(args[0]) 
            node = self._head
            for item in args[1:]:
                node.next = Node(item)
                node = node.next
            self._tail = node

    def add(self, item):
        if self.isEmpty():
            self._head = Node(item)
            self._tail = self._head
        else:
            self._tail.next = Node(item)
            self._tail = self._tail.next

    def remove(self):
        if self.isEmpty():
            return None
        node = self._head
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        return node.data

    def peek(self):
        return self._head.data

    def isEmpty(self):
        return self._head is None

    def toString(self):
        node = self._head
        while node is not None:
            print(node.data)
            node = node.next

q = Queue(1,2,3)

assert q.peek() == 1

q.add(4)
q.remove()

assert q.remove() == 2

q.remove()
q.remove()
q.add(5)
q.remove()

assert q.isEmpty()