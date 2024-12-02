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
  
  for i in range(N):
    for j in range(N):
        dist[i][j] = 1 if dist[i][j] != float("inf") else 0
  
  return dist


N = int(input())


graph = []
for i in range(N):
  graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = -1

result = floyd_warshall(graph, N)
for i in range(len(result)):
  print(*result[i])
  
