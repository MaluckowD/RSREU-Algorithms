

def floyd_warshall(graph, N):
  
  dist = [ [ float("inf") ] * N for _ in range(N)]
  
  for i in range(N):
    for j in range(N):
      if graph[i][j] != -1:
        dist[i][j] = graph[i][j]
      if i == j:
        dist[i][j] = 0
  
  for k in range(N):
    for i in range(N):
      for j in range(N):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
  
  return dist
