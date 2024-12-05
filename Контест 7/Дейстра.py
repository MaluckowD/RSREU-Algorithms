
def dijkstra(graph, start, end):
  n = len(graph)
  visited = [False] * n
  dist = [float('inf')] * n
  dist[start] = 0
  
  for _ in range(n):
    min_dist = float('inf')
    min_index = -1
    for i in range(n):
      if not visited[i] and dist[i] < min_dist:
        min_dist = dist[i]
        min_index = i
    
    if min_index == -1:
      break
    
    visited[min_index] = True
    for i in range(n):
      if graph[min_index][i] >= 0:
        new_dist = dist[min_index] + graph[min_index][i]
        if new_dist < dist[i]:
          dist[i] = new_dist
  