
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def find_max(self):
    if self.root is None:
      return str(None)
    return self._max_node(self.root).data
  
  def _max_node(self, node):
    current = node
    while current.right is not None:
        current = current.right
    return current
  
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
 
  


bst = BinarySearchTree()
numbers = input().split()
for number in numbers:
  if number != "0":
    bst.insert(int(number))
  else:
    break

a = bst.find_max()
bst.delete(a)

print(bst.find_max())