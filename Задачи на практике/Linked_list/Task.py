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

  def push_back(self, element):
    new_node = Node(element)
    if self.is_empty():
      self.head = new_node
    else:
      current = self.head
      while current.next_node:
        current = current.next_node
      current.next_node = new_node
      
  def swap_first_last(self):
    
    if not self.head or not self.head.next_node:
      return "error"

    first = self.head  
    last = self.head
    while last.next_node:
      last = last.next_node  

    first.element, last.element = last.element, first.element

  def push_front(self, element):
    new_node = Node(element, self.head)
    self.head = new_node
      
  def sort_positive_negative_zero(self):
    if not self.head:
      return "error"

    positive_list = LinkedList()
    negative_list = LinkedList()
    zero_list = LinkedList()

    current = self.head
    while current:
      if current.element > 0:
        positive_list.push_back(current.element)
      elif current.element < 0:
        negative_list.push_back(current.element)
      else:
        zero_list.push_back(current.element)
          
      current = current.next_node

    self.head = None 
    current = positive_list.head
    while current:
      self.push_back(current.element)
      current = current.next_node

    current = negative_list.head
    while current:
      self.push_back(current.element)
      current = current.next_node

    current = zero_list.head
    while current:
      self.push_back(current.element)
      current = current.next_node

  def swap_pairs(self):
    
    if not self.head or not self.head.next_node:
      return "error"

    current = self.head
    while current and current.next_node:
      current.element, current.next_node.element = current.next_node.element, current.element
      current = current.next_node.next_node   
                  
mylist = LinkedList()
mylist.push_back(5)
mylist.push_back(1)
mylist.push_back(-1)
mylist.push_back(0)
mylist.push_back(1)
mylist.push_back(8)
mylist.push_back(-5)
mylist.push_back(0)

print("Исходный список: ")
print(mylist)
print()

print("1) Список состоящий сначала из положительных элементов, потом из отрицательных, после из нулей: ")
mylist.sort_positive_negative_zero()
print(mylist)
print()

print("2) Список, в котором поменяли местами первое и последнее число: ")
mylist.swap_first_last()
print(mylist)

print()
print("3) Список, в котором поменяли первое и второе число, третье и четвертое и тд: ")
mylist.swap_pairs()
print(mylist)

#  для списка, состоящего из одного элемента будет выводиться его единственный элемент