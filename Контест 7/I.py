def floyd_warshall(graph, n):
  dist = [[float("inf") for i in range(N)] for i in range(N)]

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


N, M = map(int, input().split())

graph = list(list(-1 if i != j else 0 for i in range(N)) for j in range(N))
for i in range(M):
  start, end, length = map(int, input().split())
  graph[start - 1][end - 1] = length
  graph[end - 1][start - 1] = length

result = floyd_warshall(graph, N)

ans = 0
cur_mx = float("inf")
for i in range(N):
  mx = max(result[i])
  if mx < cur_mx:
    ans = i
    cur_mx = mx

print(ans + 1)