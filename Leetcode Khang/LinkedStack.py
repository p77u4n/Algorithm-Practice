class LinkedStack:
    class Node:
        def __init__(self, val, next):
            self._val = val
            self._next = next
    def __init__(self):
        self._head = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def push(self,a):
        self._head = self.Node(a, self._head)
        self._size += 1
    
    def top(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self._head._val
    def pop(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        answer = self._head._val
        self._head = self._head._next
        self._size -= 1
        return answer
if __name__ == '__main__':
    newL = LinkedStack()
    print(newL._size)
    newL.push(3)
    print(newL._size)
    print(newL._head._val)
    print(newL.pop())
    print(newL._head)
    
