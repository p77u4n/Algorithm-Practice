class CircularQueue:
    class Node:
        def __init__(self, e, next):
            self._value = e
            self._next = next
    
    def __init__(self):
        self.len = 0
        self.tail = None
    
    def __len__(self):
        return self.len
    
    def isEmpty(self):
        return self.len == 0

    def first(self):
        if self.isEmpty():
            raise Empty('Queue is Empty')
        else:
            head = self.tail._next
            return head._value
    def enque(self, e):
        new = self.Node(e, None)
        if self.isEmpty():
            new._next = new
        else:
            new._next = self.tail._next
            self.tail._next = new
        self.tail = new
        self.len += 1
    
    def deque(self):
        if self.isEmpty():
            raise Empty('Queue is Empty')
        oldhead = self.tail._next
        if self.len == 1:
            self.tail = None
        else:
            self.tail._next = oldhead._next
        self.len -= 1
        return oldhead._value

    def rotate(self):
        if self.isEmpty():
            raise Empty('Queue is Empty')
        else:
            self.tail = self.tail._next
        
newQueue = CircularQueue()
newQueue.enque(30)
newQueue.enque(40)
newQueue.enque(50)
print(newQueue.deque())
print(newQueue.__len__())

print(newQueue.deque())
print(newQueue.__len__())

print(newQueue.deque())
print(newQueue.__len__())
