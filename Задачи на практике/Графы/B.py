from collections import deque

def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, winner = map(int, input().split())
        if winner == u:
            edges.append((u, v))
        else:
            edges.append((v, u))

    graph = {i: [] for i in range(1, n + 1)}
    in_degree = {i: 0 for i in range(1, n + 1)}

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([node for node, degree in in_degree.items() if degree == 0])
    sorted_players = []
    
    while queue:
        if len(queue) > 1:
            print("NO")
            return
        u = queue.popleft()
        sorted_players.append(u)

        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(sorted_players) == n:
        print("YES")
    else:
        print("NO")  # Cycle detected

solve()
      