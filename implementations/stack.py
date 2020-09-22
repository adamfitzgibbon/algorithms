"""A Python implementation of a Stack"""

class Stack:

    def __init__(self, *args):
        self._stack = [x for x in args]
        self._pointer = len(self._stack) - 1
    
    def pop(self):
        if self.isEmpty(): 
            return None
        item = self._stack[self._pointer]
        self._pointer -= 1
        return item

    def push(self, item):
        self._pointer += 1
        self._stack[self._pointer] = item

    def peek(self):
        return self._stack[self._pointer]

    def isEmpty(self):
        return self._pointer == -1

stack = Stack(1,2,3)
assert stack.pop() == 3

stack.push(4)
assert stack.peek() == 4

stack.pop()
stack.pop()
stack.push(1)
stack.pop()
stack.pop()

assert stack.pop() is None
assert stack.isEmpty()