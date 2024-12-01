
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


N = int(input())

graph = []
for i in range(N):
  graph.append(list(map(int, input().split())))

result = floyd_warshall(graph, N)
count = 0
for i in range(N):
  for j in range(N):
    if result[i][j] < 0:
      break
    count += 1
if count != N * N:
  print(-1)
else:
  for i in range(N):
    for j in range(N):
      if result[i][j] == 0:
        result[i][j] = 10 ** 6
  ans = 10 ** 4
  for i in range(N):
    for j in range(N):
      ans = min(result[i][j], ans)
print(ans)
  
