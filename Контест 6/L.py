from collections import defaultdict
import sys

sys.setrecursionlimit(1000000000)


def dfs(start, parent):
    global find
    color[start] = "Grey"
    for v in graph[start]:
        if v == parent:
            continue

        if color[v] == "White":
            dfs(v, start)

        elif color[v] == "Grey":
            if not find:
                to_remove[start].add(v)

            find = True

    color[start] = "Black"


n, m = map(int, input().split())

graph = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

while True:
    find = False
    to_remove = defaultdict(set)
    for i in range(1, n + 1):
        color = ["White"] * (n + 1)
        dfs(i, -1)

    if to_remove:
        for key, data in to_remove.items():
            for v in data:
                graph[key].remove(v)
                graph[v].remove(key)

    else:
        break

visited = set()
for key, data in graph.items():
    for v in data:
        if (min(key, v), max(key, v)) not in visited:
            print(key, v)
            visited.add((min(key, v), max(key, v)))