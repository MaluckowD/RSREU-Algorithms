
import sys

sys.setrecursionlimit(1000000)

def dfs(v, p):
  visited[v] = True
  for u in graph[v]:
    if u != p:
      if visited[u]:
        return True  
      if dfs(u, v):
        return True 
  return False


n, m = map(int, input().split())

graph = {i: set() for i in range(1, n + 1)}
for i in range(m):
  a, b = map(int, input().split())
  graph[a].add(b)
  graph[b].add(a)


visited = [False] * (n + 1)
cycle = False

if m != n - 1 or dfs(1, -1):
  print("NO")
else:
  print("YES")