from collections import deque


def isValid(num):
    return 1 <= num <= n


def bfs():
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == INF:
                q.append(neighbor)
                dist[neighbor] = min(dist[neighbor], dist[node] + 1)
                path[neighbor] = path[node] + [neighbor]


n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

graph = {(i, j): set() for i in range(1, n + 1) for j in range(1, n + 1)}
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if isValid(j + 2):
            if isValid(i + 1):
                graph[(i, j)].add((i + 1, j + 2))
                graph[(i + 1, j + 2)].add((i, j))
            if isValid(i - 1):
                graph[(i, j)].add((i - 1, j + 2))
                graph[(i - 1, j + 2)].add((i, j))

        if isValid(j - 2):
            if isValid(i + 1):
                graph[(i, j)].add((i + 1, j - 2))
                graph[(i + 1, j - 2)].add((i, j))
            if isValid(i - 1):
                graph[(i, j)].add((i - 1, j - 2))
                graph[(i - 1, j - 2)].add((i, j))

        if isValid(j + 1):
            if isValid(i + 2):
                graph[(i, j)].add((i + 2, j + 1))
                graph[(i + 2, j + 1)].add((i, j))
            if isValid(i - 2):
                graph[(i, j)].add((i - 2, j + 1))
                graph[(i - 2, j + 1)].add((i, j))

        if isValid(j - 1):
            if isValid(i + 2):
                graph[(i, j)].add((i + 2, j - 1))
                graph[(i + 2, j - 1)].add((i, j))
            if isValid(i - 2):
                graph[(i, j)].add((i - 2, j - 1))
                graph[(i - 2, j - 1)].add((i, j))

visited = list(list(False for _ in range(n)) for _ in range(n))
root = (x1, y1)
INF = 10 ** 9
dist = {(i, j): INF for i in range(1, n + 1) for j in range(1, n + 1)}
path = {(i, j): [] for i in range(1, n + 1) for j in range(1, n + 1)}

dist[root] = 0
path[root] = [root]
q = deque([root])

bfs()

print(dist[(x2, y2)])
for elem in path[(x2, y2)]:
    print(*elem)
