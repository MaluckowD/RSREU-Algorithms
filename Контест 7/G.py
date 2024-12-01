
def floyd_warshall(graph, N):
  dist = [[float('inf')] * N for _ in range(N)]

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
      if dist[i][i] < 0:
          return -1  

  min_path = float('inf')
  for i in range(N):
      for j in range(N):
          if i != j:  
              min_path = min(min_path, dist[i][j])

  return min_path


N = int(input())
graph = []
for i in range(N):
  graph.append(list(map(int, input().split())))

result = floyd_warshall(graph, N)
print(result)

        