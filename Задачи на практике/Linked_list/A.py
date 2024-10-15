class Node:
    def __init__(self, element, next_node=None):
        self.element = element
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

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
      
lst = LinkedList()
a = []
q = int(input())
for _ in range(q):
    quary = list(map(int,input().split()))
    if quary[0] == 1:
        lst.insert(quary[2], quary[1])
    elif quary[0] == 2:
        a.append(lst.get(quary[1] - 1))
    else:
        lst.pop(quary[1] - 1)
print(*a, sep = '\n')