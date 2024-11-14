from collections import deque

def bfs(x, y):
  queue = deque([[x, 0]])
  visited = set([x])
  maximum = max(x, y)
  while queue:
    node, length = queue.popleft()
    if node == y:
      return length
    
    if node in visited:
      continue
    if abs(node - y) > 100:
      continue
      #return length + (y - node) // 9 + 1
    
    visited.add(node)
    for c in range(10):
      options = [ node + C,  node - C, node * C]
      for var in options:
        if 0 <= var <= maximum + 100 and var not in visited:
          visited.add(var)
          queue.append([var, length + 1])
    
    return -1

x, y = map(int, input().split())
      