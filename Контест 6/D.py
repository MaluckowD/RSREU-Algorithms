from collections import defaultdict

def dfs(start):
  visited[start] = True
  for v in graph[start]:
    if not visited[v]:
      dfs(v)

n, s = map(int, input().split())
lst = []
visited = [False] * (n + 1)
for i in range(n):
  lst.append(list(map(int, input().split())))

graph = defaultdict(set)
for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            graph[i].add(j)

dfs(s - 1)
print(visited.count(True))
