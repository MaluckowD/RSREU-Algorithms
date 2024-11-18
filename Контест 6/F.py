
from sys import setrecursionlimit
setrecursionlimit(100000)

def dfs(v):
  global cycle
  color[v] = 'gray'
  for w in graph[v]:
    if color[w] == 'white':
      dfs(w)
    if color[w] == 'gray':
      cycle = True
  
  color[v] = 'black'

n = int(input())
w = [] * n
for i in range(n):
  w.append(input().split(' '))

graph = {i + 1: set() for i in range(n)}

for i in range(n):
  for j in range(len(w)):
    if w[i][j] == '1':
      graph[i+1].add(j + 1)

color = ['white'] * (n + 1)
cycle = False
for v in range(1, n + 1):
  if color[v] == 'white':
    dfs(v)
    if cycle:
      print(1)
      break
else:
  print(0)