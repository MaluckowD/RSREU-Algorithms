class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
      
    def set_next(self, new_next):
        self.next = new_next

class Stack:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def push(self, data):
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp

    def pop(self):
        if not self.is_empty():
            current = self.head
            self.head = current.get_next()
    
    def top(self):
        if not self.is_empty():
            return self.head.get_data()
        return -1

n = int(input())
mystack = Stack()
for _ in range(n):
    quary = list(map(int,input().split()))
    if quary[0] == 1:
        mystack.push(quary[1])
    else:
        mystack.pop()
    print(mystack.top())