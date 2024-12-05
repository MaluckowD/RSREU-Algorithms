from collections import defaultdict

def solve():
    n, m = map(int, input().split())

    if m < n - 1:
        print("NO")
        return

    graph = defaultdict(list)  
    in_degree = [0] * (n + 1)  

    for _ in range(m):
        u, v, winner = map(int, input().split())
        if winner == 1:  
            graph[v].append(u)  
            in_degree[u] += 1
        else: 
            graph[u].append(v)
            in_degree[v] += 1

    queue = [i for i in range(1, n + 1) if in_degree[i] == 0]  
    count = 0
    result = []

    while queue:
        if len(queue) > 1:  
            print("NO")
            return
        u = queue.pop(0)
        result.append(u)
        count += 1
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if count == n:  
        print("YES")
    else:  
        print("NO")


solve()
    
  