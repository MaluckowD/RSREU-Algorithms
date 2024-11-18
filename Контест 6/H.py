from collections import deque


def bfs(start, target):
  q = deque([(start, [start])])
  visited = set()

  while q:
    node, path = q.popleft()

    if node == target:
      return path

    visited.add(node)

    for neighbor in graph[node]:
      if neighbor not in visited:
        q.append((neighbor, path + [neighbor]))

  return []


n = int(input())
data = list(list(map(int, input().split())) for _ in range(n))

graph = {i: set() for i in range(1, n + 1)}
for i in range(1, n + 1):
  for j in range(1, n + 1):
    if data[i - 1][j - 1] == 1:
      graph[i].add(j)


a, b = map(int, input().split())
path = bfs(a, b)

print(len(path) - 1)
if len(path) > 1:
  print(*path)
  



      
    