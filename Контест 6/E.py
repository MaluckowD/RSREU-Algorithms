from collections import defaultdict

import sys

sys.setrecursionlimit(100000000)

def dfs(v, component):
  visited[v] = True
  component.append(v)
  for neighbor in graph[v]:
    if not visited[neighbor]:
      dfs(neighbor, component)

n, m = map(int, input().split())

graph = defaultdict(set)
for i in range(m):
  a, b = map(int, input().split())
  graph[a].add(b)
  graph[b].add(a)

visited = [False] * (n + 1)
components = []

for v in range(1, n + 1):
  if not visited[v]:
    component = []
    dfs(v, component)
    components.append(component)

print(len(components))
for component in components:
  print(len(component))
  print(*component)