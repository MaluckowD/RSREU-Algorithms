from collections import deque

def solve_labyrinth(n, m, labyrinth):
    start, end, door, key = None, None, None, None
    for i in range(n):
        for j in range(m):
            if labyrinth[i][j] == 'S':
                start = (i, j)
            elif labyrinth[i][j] == 'F':
                end = (i, j)
            elif labyrinth[i][j] == 'D':
                door = (i, j)
            elif labyrinth[i][j] == 'K':
                key = (i, j)
    
    queue = deque([(start[0], start[1], False, "")])
    visited_with_key = set()
    visited_without_key = set()
    visited_without_key.add(start)
    
    moves = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]

    while queue:
        x, y, has_key, path = queue.popleft()
        
        if (x, y) == end:
            print(len(path))
            print(path)
            return
        
        for dx, dy, move in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and labyrinth[nx][ny] != '#':
                if labyrinth[nx][ny] == 'D':
                    if has_key and (nx, ny) not in visited_with_key:
                        queue.append((nx, ny, True, path + move))
                        visited_with_key.add((nx, ny))
                else: 
                    new_state_visited = visited_with_key if has_key else visited_without_key
                    if (nx, ny) not in new_state_visited:
                        queue.append((nx, ny, has_key, path + move))
                        new_state_visited.add((nx, ny))
        
        if not has_key and (x, y) == key:
            if (x, y) not in visited_with_key:
                queue.append((x, y, True, path + 'P'))
                visited_with_key.add((x, y))

    print(-1)


n, m = map(int, input().split())
labyrinth = []
for i in range(n):
  labyrinth.append(input())

solve_labyrinth(n, m, labyrinth)
