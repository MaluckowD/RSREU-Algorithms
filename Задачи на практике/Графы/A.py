
from collections import deque

def can_determine(n, m, matches):
  graph = defaultdict(list)
  
  for u, v, winner in matches:
    if winner == u:
      graph(u).append(v)
    else:
      graph(v).append(u)
  
  visited = [0] * (n + 1)
  has_cycle = false
  
  win_rate = [0] * (n + 1)
  
  def dfs(node):
    nonlocal has_cycle
    if  has_cycle:
      return

    visited[node] = 1
    
  