
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


N = int(input())
d, v = map(int, input().split())
R = int(input())

graph = {i: {} for i in range(1, N + 1)}

for i in range(R):
  start_village, t_start, end_village, t_end = map(int, input().split())
  graph[start_village][end_village] = (t_end - t_start)

print(sum(dijkstra(graph, d)) - 1)