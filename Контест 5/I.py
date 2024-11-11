class Node:
  def __init__(self, data):
    self.data = data
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
            
  def height(self):
    def height_recursion(node):
      if node is None:
          return 0
      return 1 + max(height_recursion(node.left), height_recursion(node.right))
    
    return height_recursion(self.root)

  def is_balanced(self):
    def is_balanced_recursion(node):
      if node is None:
        return True, 0
      
      left_balanced, left_height = is_balanced_recursion(node.left)
      right_balanced, right_height = is_balanced_recursion(node.right)
      
      height_diff = abs(left_height - right_height)
      
      return left_balanced and right_balanced and height_diff <= 1, max(left_height, right_height) + 1
    
    balanced, heights = is_balanced_recursion(self.root)
    return balanced


bst = BinarySearchTree()
numbers = input().split()
for number in numbers:
  if number != "0":
    bst.insert(int(number))
  else:
    break

if bst.is_balanced():
  print("YES")
else:
  print("NO")
