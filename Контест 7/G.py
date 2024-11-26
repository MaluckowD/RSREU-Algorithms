N, M = map(int, input().split())
INF = float('inf')

pred = [ [-1] * N for i in range(N)]
dist = [ [INF] * N for i in range(N)]

for i in range(N):
  dist[i][j] = 0

for j in range(M):
  a, b, weight = map(int, input().split())
  if dist[a][b] > weight:
    diat[a][b] = weight
    pred[a][b] = a

for k in range(N):
    for i in range(N):
      for j in range(N):
        if dist[i][k] != INF and dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]
          pred[i][j] = pred[k][j]

N = int(input())
graph = list(list(map(int, input().split())) for _ in range(n))

        