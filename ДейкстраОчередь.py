
import queue

def dijkstra(start):
  dist = [INF] * n
  dist[start] = 0
  
  q = queue.Queue()
  q.put(start)
  
  while not q.empty():
    u = q.get()
    for v in range(n):
      if a[u][v] > 0 and dist[v] > dist[u] + a[u][v]
        q.put(v)
        dist[v] = min(dist[v], dist[u] + a[u][v])
  return dist
