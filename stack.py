from linked_list import LinkedList
from functools import reduce


class Stack(LinkedList):
    def push(self, val):
        ''' O(1) '''
        return self.prepend(Stack(val))

    def pop(self):
        ''' O(1) '''
        return self.tail



s = Stack(0).push(1).push(2)
assert s == Stack(2, Stack(1, Stack(0)))
assert s.head == 2
assert s.pop().head == 1
assert s.pop().pop().head == 0
