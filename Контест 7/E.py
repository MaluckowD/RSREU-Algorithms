import heapq


def dijkstra(graph, start, end):
    INF = float('inf')
    pq = []

    dist = {node: INF for node in graph}
    dist[start] = 0

    heapq.heappush(pq, (0, start))

    while pq:
        cur_time, cur_vertex = heapq.heappop(pq)

        if cur_time > dist[cur_vertex]:
            continue

        for dep_time, arr_time, neighbor in graph[cur_vertex]:
            if dep_time >= cur_time:
                if arr_time < dist[neighbor]:
                    dist[neighbor] = arr_time
                    heapq.heappush(pq, (arr_time, neighbor))

    return dist[end] if dist[end] != INF else -1


n = int(input())
d, v = map(int, input().split())
r = int(input())

graph = {i: [] for i in range(1, n + 1)}
for i in range(r):
    start, time_start, end, time_end = map(int, input().split())
    graph[start].append((time_start, time_end, end))

result = dijkstra(graph, d, v)
print(result)