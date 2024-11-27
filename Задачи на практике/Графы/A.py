from collections import deque

def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, winner = map(int, input().split())
        if winner == u:
            edges.append((u, v))  # u beats v
        else:
            edges.append((v, u))

    graph = {i: [] for i in range(1, n + 1)}
    in_degree = {i: 0 for i in range(1, n + 1)}

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([node for node, degree in in_degree.items() if degree == 0])
    sorted_players = []
    count = 0

    while queue:
        if len(queue) > 1:  # Ambiguous if multiple starting nodes
            print("NO")
            return

        u = queue.popleft()
        sorted_players.append(u)
        count += 1

        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if count != n:  # Cycle detected
        print("NO")
    elif m == 0: # No matches
        print("NO")
    else:
        print("YES")


solve()
    
  