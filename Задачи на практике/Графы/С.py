from collections import deque

def solve():
    n, m = map(int, input().split())
    maze = [list(input()) for _ in range(n)]

    start_row, start_col = -1, -1
    end_row, end_col = -1, -1

    for r in range(n):
        for c in range(m):
            if maze[r][c] == 'S':
                start_row, start_col = r, c
            elif maze[r][c] == 'F':
                end_row, end_col = r, c

    queue = deque([(start_row, start_col, "")]) 
    visited = set([(start_row, start_col)])

    while queue:
        row, col, path = queue.popleft()
        if row == end_row and col == end_col:
            print(len(path))
            print(path)
            return

        for dr, dc, move in [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < m and maze[new_row][new_col] != '#' and (new_row, new_col) not in visited:
                queue.append((new_row, new_col, path + move))
                visited.add((new_row, new_col))

    print("-1")


solve()