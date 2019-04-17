from dataclasses import dataclass
from typing import Any, Optional


@dataclass(eq=True)
class L:
    ''' Implementation of an Imutable Linked List'''
    head: Any
    tail: Optional['L'] = None

    def prepend(self, l) -> 'L':
        ''' O(1) '''
        return type(self)(l.head, self)

    def next(self) -> 'L':
        ''' O(1) '''
        return self.tail

    def traverse(self, max_i=float('inf')):
        ''' O(n) '''
        curr = self
        i = 0
        while curr and i <= max_i:
            yield curr
            curr = curr.next()
            i += 1

    def __getitem__(self, i) -> 'L':
        ''' O(n) '''
        if isinstance(i, slice):
            return self.__getitem__slice(i)
        elif isinstance(i, int):
            return self.__getitem__index(i)
        else:
            raise TypeError()

    def __getitem__index(self, i):
        ''' O(n) '''
        if i < -1:
            raise NotImplementedError()

        for j, l in enumerate(self.traverse()):
            if i == j:
                return L(l.head, l.tail)

            if (l.tail is None) and i == -1:
                return l

    def __getitem__slice(self, i):
        ''' O(n) '''
        def loop(curr, depth=0):
            if curr.tail and depth < i.stop - i.start - 1:
                return loop(curr.tail, depth + 1).prepend(type(self)(curr.head))
            else:
                return type(self)(curr.head)
        return loop(self[i.start])

    def append(self, l):
        ''' O(n) '''
        def loop(curr):
            if curr.tail:
                return loop(curr.tail).prepend(type(self)(curr.head))
            else:
                return l.prepend(type(self)(curr.head))
        return loop(self)

    def remove(self, i):
        ''' O(n) '''
        def loop(curr, depth=0):
            if curr.tail and depth != i:
                return loop(curr.tail, depth + 1).prepend(type(self)(curr.head))
            elif curr.tail and depth == i:
                return type(self)(curr.tail.head, curr.tail.tail)
            else:
                return type(self)(None)
        return loop(self)

    def search(self, val):
        ''' O(n) '''
        for l in self.traverse():
            if val == l.head:
                return True

    #######################################################
    ######## ####### ####### SUGAR ######## ####### ####### 
    #######################################################

    def __add__(self, l):
        return self.append(l)

    @property
    def first(self):
        return self[0]

    @property
    def last(self):
        return self[-1]

    def __iter__(self):
        return self.traverse()

LinkedList = L

#######################################################
######## ####### ####### TESTS ######## ####### ####### 
#######################################################

# prepend
assert L(0).prepend(L(1)) == L(1, L(0))

# next
assert L(0, L(1)).next() == L(1)

# traverse
assert all(i == l.head 
           for i, l in enumerate(L(0, L(1, L(2))).traverse()))
assert all(i == l.head 
           for i, l in enumerate(L(0, L(1, L(2)))))

# __getitem__
assert L(0)[0] == L(0)
assert L(0, L(1))[1] == L(1)
assert L(0, L(1))[99] is None
assert L(0, L(1, L(2))).last == L(2)
assert L(0, L(1, L(2, L(3))))[0:2] == L(0, L(1))

# append
assert L(0, L(1)).append(L(2)) == L(0, L(1, L(2)))
assert L(0) + L(1) + L(2) == L(0, L(1, L(2)))

# remove
assert L(0, L(1, L(2, L(3)))).remove(2) == L(0, L(1, L(3)))

# search
assert L(0, L(1, L(2))).search(1)
assert not L(0, L(1, L(2))).search(-1)
