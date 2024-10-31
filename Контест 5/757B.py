
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, key):
    self.root = self._insert(self.root, key)

  def _insert(self, node, key):
    if node is None:
        return Node(key)
    if key < node.data:
        node.left = self._insert(node.left, key)
    elif key > node.data:
        node.right = self._insert(node.right, key)
    return node

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


  def size(self):
      return self._size(self.root)

  def _size(self, node):
      if node is None:
          return 0
      return 1 + self._size(node.left) + self._size(node.right)

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
        return self._height(self.root)

  def _height(self, node):
      if node is None:
          return 0
      return 1 + max(self._height(node.left), self._height(node.right))


bst = BinarySearchTree()
numbers = [int(x) for x in input().split()][:-1]
for number in numbers:
  bst.insert(number)
print(bst.height())  
    



      
