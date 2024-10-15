class Node:
    def __init__(self, element, next_node=None):
        self.element = element
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def insert(self, element, index):
        if index == 0:
            self.head = Node(element, self.head)
            return

        count = 0
        current = self.head
        previous = None
        while count < index:
            previous = current
            current = current.next_node
            count += 1

        new_node = Node(element, current)
        previous.next_node = new_node

    def get(self, index):
        count = 0
        current = self.head
        while count < index:
            current = current.next_node
            count += 1
        return current.element

    def pop(self, index):
        if index == 0:
            element = self.head.element
            self.head = self.head.next_node
            return element
        count = 0
        current = self.head
        previous = None
        while count < index:
            previous = current
            current = current.next_node
            count += 1

        element = current.element
        previous.next_node = current.next_node
        return element

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_node
        return count


class Queue:
    def __init__(self):
        self.l = LinkedList()
        self.r = LinkedList()

    def is_empty(self):
        return self.l.is_empty() and self.r.is_empty()

    def push(self, item):
        self.l.insert(item, 0)

    def pop(self):
        if self.is_empty():
            return -1
        if self.r.is_empty():
            while not self.l.is_empty():
                self.r.insert(self.l.pop(0), 0)
        return self.r.pop(0)

    def front(self):
        if self.is_empty():
            return -1
        if self.r.is_empty():
            while not self.l.is_empty():
                self.r.insert(self.l.pop(0), 0)
        return self.r.get(0)

    def size(self):
        return self.l.size() + self.r.size()
  
lst = Queue()
a = []
q = int(input())
for _ in range(q):
    quary = list(map(int,input().split()))
    if quary[0] == 1:
        lst.push(quary[1])
        a.append(lst.front())
    else:
      lst.pop()
      a.append(lst.front())
print(*a, sep = '\n')