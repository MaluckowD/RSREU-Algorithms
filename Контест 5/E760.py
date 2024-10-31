class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

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
            break

    def order_up(self):
      result = []
      stack = []
      current = self.root
      while stack or current:
        while current:
          stack.append(current)
          current = current.left
        current = stack.pop()
        result.append(current.data)
        current = current.right
      return result
        
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

numbers = list(map(int, input().split()))
bst = BinarySearchTree()
for el in numbers:
  if el == 0:
    break
  else:
    bst.insert(el)

for el in bst.order_up():
  print(el)
  

