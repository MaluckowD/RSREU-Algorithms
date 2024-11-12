class Node:
    def __init__(self, key):
      self.data = key
      self.left = None
      self.right = None
      self.count = 1

class BinarySearchTree:

    def __init__(self):
        self.root = None

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
            curr_node.count += 1
            break

    def order_up(self, node):
      result = []
      stack = []
      current = self.root
      while stack or current:
        while current:
          stack.append(current)
          current = current.left
        current = stack.pop()
        item = [current.data] + [current.count]
        result.append(item)
        current = current.right
      return result
        
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

numbers = list(map(int, input().split()))
bst = BinarySearchTree()
for el in numbers:
  if el == 0:
    break
  else:
    bst.insert(el)

for el in bst.order_up(bst.root):
  print(*el)