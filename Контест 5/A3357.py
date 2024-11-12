import sys

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    

class BinarySearchTree:
  def __init__(self):
    self.root = None
    
  def search(self, key):
    return self._search(self.root, key)

  def _search(self, node, key):
    if node is None:
        return False
    if key == node.data:
        return True
    if key < node.data:
        return self._search(node.left, key)
    return self._search(node.right, key)

  def insert(self, key):
    if self.root is None:
      self.root = Node(key)
    else:
      curr_node = self.root
      while True:
        if key < curr_node.data:
          if curr_node.left is None:
            curr_node.left = Node(key)
            break
          curr_node = curr_node.left
        elif key > curr_node.data:
          if curr_node.right is None:
            curr_node.right = Node(key)
            break
          curr_node = curr_node.right
        else:
          break
  def delete(self, key):
    self.root = self._delete(self.root, key)
  
  def _max_node(self, node):
    current = node
    while current.right is not None:
        current = current.right
    return current

  def _delete(self, node, key):
    if node is None:
        return node
    if key < node.data:
        node.left = self._delete(node.left, key)
    elif key > node.data:
        node.right = self._delete(node.right, key)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        max_node = self._max_node(node.left)
        node.data = max_node.data
        node.left = self._delete(node.left, max_node.data)
    return node
            
  def print_tree(self, node, level = 0):
    if node is None:
        return
    level += 1
    self.print_tree(node.left, level)
    for i in range(1, level):
      print(".", end = "")
    
    print(node.data)
    self.print_tree(node.right, level)
    
    
bst = BinarySearchTree()
numbers = sys.stdin.readline().split()

while numbers:
    #print(numbers)
    if numbers[0] == "ADD":
      if bst.search(int(numbers[1])): 
        print("ALREADY")
      else:
        bst.insert(int(numbers[1]))  
        print("DONE")
    elif numbers[0] == "DELETE":
      if bst.search(int(numbers[1])):  
        bst.delete(int(numbers[1]))  
        print("DONE")
      else:
        print("CANNOT")
    elif numbers[0] == "SEARCH":
      if bst.search(int(numbers[1])):  
        print("YES")
      else:
        print("NO")
    elif numbers[0] == "PRINTTREE":
      bst.print_tree(bst.root, 0)

    numbers = sys.stdin.readline().split()  
  
