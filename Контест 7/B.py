
import heapq

def dijkstra(graph, start):
  dist = {node: 2009000999 for node in graph}
  dist[start] = 0
  
  pq = [ (0, start)]
  heapq.heapify(pq)
  
  while pq:
    cur_dist, cur_vertex = heapq.heappop(pq)
    
    if dist[cur_vertex] < cur_dist:
      continue
    
    for neighbor, weight in graph[cur_vertex].items():
      d = cur_dist + weight
      if d < dist[neighbor]:
        dist[neighbor] = d
        heapq.heappush(pq, (d, neighbor))
  
  return dist


NUM = int(input())
for i in range(NUM):
  N, M = map(int, input().split())
  graph = {i: {} for i in range(N)}

  for i in range(M):
    s, f, w = list(map(int, input().split()))
    graph[s][f] = w
    graph[f][s] = w

  S = int(input())
    
  print(*dijkstra(graph, S).values())