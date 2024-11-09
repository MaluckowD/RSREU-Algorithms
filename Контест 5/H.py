class Node:
    def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

class BinaryTree:
    def __init__(self):
      self.root = None

    def insert(self, node: Node, x):
      if node is None:
        return Node(x)

      if x < node.data:
        node.left = self.insert(node.left, x)
      else:
        node.right = self.insert(node.right, x)

      return node

    def print_leaves(self, node: Node):
        if node is None:
            return

        self.print_leaves(node.left)
        a = node.left is not None and node.right is None
        b = node.left is None and node.right is not None
        if a or b:
          print(node.data)

        self.print_leaves(node.right)


a = list(map(int, input().split()))
a.pop()

visited = set()
tree = BinaryTree()
for item in a:
  if item not in visited:
    tree.root = tree.insert(tree.root, item)
    visited.add(item)
    
tree.print_leaves(tree.root)