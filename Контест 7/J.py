import heapq

def dijkstra(graph, n, start, end):
    dist = [float('inf')] * (n + 1) 
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)

        if u == end:
            return dist[end]

        if d > dist[u]:
            continue

        for v, weight in graph.get(u, []):
            new_dist = d + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v)) 

    return -1


n, k = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)} 

for _ in range(k):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

start_node, end_node = map(int, input().split())
result = dijkstra(graph, n, start_node, end_node)
print(result)