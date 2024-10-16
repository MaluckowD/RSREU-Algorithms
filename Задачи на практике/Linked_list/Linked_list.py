class Node:
    def __init__(self, element, next_node=None):
        self.element = element
        self.next_node = next_node

    def __str__(self):
        return f'[{self.element} -> {self.next_node}]' 


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return "[]"
        current = self.head
        result = "["
        while current:
            result += str(current.element) + ", "
            current = current.next_node
        result = result[:-2]  
        result += "]"
        return result
    
    def is_empty(self):
        return self.head is None

    def push_front(self, element):
        new_node = Node(element, self.head)
        self.head = new_node

    def push_back(self, element):
        new_node = Node(element)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def size(self):
      count = 0
      current = self.head
      while current:
        count += 1
        current = current.next_node
      return count

    def find(self, x):
        current = self.head
        while current:
            if current.element == x:
                return True
            current = current.next_node
        return False

    def pop_front(self):
        if not self.is_empty():
            self.head = self.head.next_node

    def pop_back(self):
        if not self.is_empty():
            current = self.head
            previous = None
            while current.next_node:
                previous = current
                current = current.next_node
            if previous:
                previous.next_node = None
            else:
                self.head = None  

    def remove(self, key):
        if self.find(key):
            current = self.head
            previous = None
            while current:
                if current.element == key:
                    if previous:
                        previous.next_node = current.next_node
                    else:
                        self.head = current.next_node
                    return True
                previous = current
                current = current.next_node
        return False
      

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
        if index < 0 or index >= self.size():
            raise IndexError("Индекс вне диапазона.")

        count = 0
        current = self.head
        while count < index:
            current = current.next_node
            count += 1
        return current.element

    def pop(self, index):
        if index < 0 or index >= self.size():
            raise IndexError("Индекс вне диапазона.")

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
    
    def reverse(self):
        previous = None
        current = self.head
        next_node = None
        while current:
            next_node = current.next_node  
            current.next_node = previous  
            previous = current  
            current = next_node  
        self.head = previous  
    
    def insert_after(self, key, new_element):
        current = self.head
        previous = None
        while current:
            if current.element == key:
                new_node = Node(new_element, current.next_node)
                current.next_node = new_node
                return True
            previous = current
            current = current.next_node
        return False  

    def insert_before(self, key, new_element):
        current = self.head
        previous = None
        while current:
            if current.element == key:
                new_node = Node(new_element, current)
                if previous:  
                    previous.next_node = new_node
                else:  
                    self.head = new_node
                return True
            previous = current
            current = current.next_node
        return False 
      
    def remove_after(self, key):
        current = self.head
        previous = None
        while current:
            if current.element == key:
                if current.next_node:
                    current.next_node = current.next_node.next_node
                    return True
                else:
                    return False 
            previous = current
            current = current.next_node
        return False  

    def remove_before(self, key):
        current = self.head
        previous = None
        while current:
            if current.next_node and current.next_node.element == key:
                if previous:
                    previous.next_node = current.next_node
                    return True
                else:
                    self.head = current.next_node
                    return True
            previous = current
            current = current.next_node
        return False 
    
    def clear(self):
        self.head = None
    
    def count_element(self, key):
      count = 0
      current = self.head
      while current:
          if current.element == key:
              count += 1
          current = current.next_node
      return count
    
    def find_index(self, key):
        index = 0
        current = self.head
        while current:
            if current.element == key:
                return index
            current = current.next_node
            index += 1
        return -1
    
    def sort(self):
        if self.head is None or self.head.next_node is None:
            return 

        current = self.head
        while current:
            next_node = current.next_node
            while next_node:
                if current.element > next_node.element:
                    current.element, next_node.element = next_node.element, current.element
                next_node = next_node.next_node
            current = current.next_node

    def copy(self):
        new_list = LinkedList()
        current = self.head
        while current:
            new_list.push_back(current.element)
            current = current.next_node
        return new_list
        
mylist = LinkedList()
mylist.push_front(5)
mylist.push_front(1)
mylist.push_back(3)
mylist.push_back(9)
print(mylist)
mylist.pop_back()
print(mylist)
mylist.pop_front()
print(mylist)
mylist.insert(8,1)
print(mylist)

print(mylist.get(2))
print(mylist)


mylist.pop(0)

print(mylist)

mylist.reverse()
print(mylist)

mylist.insert_after(10, 8)
print(mylist)

mylist.insert_before(8, 10)
print(mylist)


mylist.remove_after(100)
print(mylist)

print(mylist.count_element(11))
print(mylist.find_index(10))
mylist.sort()
print(mylist)
a = mylist.copy()
print(a)

mylist.clear()
print(mylist)
