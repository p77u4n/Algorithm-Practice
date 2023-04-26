class LinkedQueue:
    class Node:
        def __init__(self, val, next):
            self._val = val
            self._next = next
    def __init__(self):
        self._tail = None
        self._head = None
        self._size = 0
    
    def __len__(self):
        return self._size
    def isEmpty(self):
        return self._size == 0
    def first(self):
        if self.isEmpty():
            raise Empty('The queue is empty')
        return self._head._val
    def enQueue(self,a):
        newest = self.Node(a, None)     
        if self.isEmpty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
    def deQueue(self):
        if self.isEmpty():
            raise Empty('The queue is empty')
        else:
            answer = self._head._val
            self._head = self._head._next
            self._size -= 1
        if self.isEmpty():
            self._tail = None
        return answer
if __name__ == '__main__':
    queue = LinkedQueue()
    queue.enQueue(3)
    queue.enQueue(4)
    queue.deQueue()
    #print(queue._head._val)
    print(queue._tail._val)
    print(queue._size)
