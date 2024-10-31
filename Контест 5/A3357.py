
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
            
  def height(self):
    def height_recursion(node):
      if node is None:
          return 0
      return 1 + max(height_recursion(node.left), height_recursion(node.right))
    
    return height_recursion(self.root)


bst = BinarySearchTree()
numbers = input().split()
for number in numbers:
  if number[:3] != "0":
    bst.insert(int(number))
  else:
    break
print(bst.height()) 