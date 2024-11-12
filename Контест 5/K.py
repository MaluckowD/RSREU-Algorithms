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
            return

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

    def next(self, key):
        curr_node = self.root
        min_greater = -1
        while curr_node:
            if key <= curr_node.data:
                min_greater = curr_node.data
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return min_greater

n = int(input())
bst = BinarySearchTree()
last_y = None

for _ in range(n):
    command, num = input().split()
    num = int(num)

    if command == "+":
        if last_y is not None:
            bst.insert((num + last_y) % (10**9))
            last_y = None
        else:
            bst.insert(num)

    elif command == "?":
        result = bst.next(num)
        print(result)
        last_y = result

