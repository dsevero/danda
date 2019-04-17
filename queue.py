from linked_list import LinkedList

class Queue(LinkedList):
    def enqueue(self, val):
        ''' O(n) '''
        return self.append(Queue(val))

    def dequeue(self):
        ''' O(1) '''
        return self.tail

    # SUGAR #

    @property
    def d(self):
        return self.dequeue()

    def e(self, val):
        return self.enqueue(val)

q = Queue(0).e(1).e(2)
assert q.head == 0
assert q.d.head == 1
assert q.d.d.head == 2
