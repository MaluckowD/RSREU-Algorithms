from collections import deque

def solve():
    n, m = map(int, input().split())
    maze = [list(input()) for _ in range(n)]
    k = int(input())
    key_door_pairs = {}
    for _ in range(k):
        door, key = input().split()
        key_door_pairs[key] = door

    start_row, start_col = -1, -1
    end_row, end_col = -1, -1

    for r in range(n):
        for c in range(m):
            if maze[r][c] == 'S':
                start_row, start_col = r, c
            elif maze[r][c] == 'F':
                end_row, end_col = r, c

    queue = deque([((start_row, start_col), 0, "")])  # (position, keys_collected_mask, path)
    visited = {((start_row, start_col), 0)}

    while queue:
        (row, col), keys_collected, path = queue.popleft()
        if row == end_row and col == end_col:
            print(len(path))
            print(path)
            return

        for dr, dc, move in [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < m:
                cell = maze[new_row][new_col]

                new_keys = keys_collected

                if 'a' <= cell <= 'k':  # Pick up key
                    new_keys |= (1 << (ord(cell) - ord('a')))
                    if ((new_row, new_col), new_keys) not in visited:
                        visited.add(((new_row, new_col), new_keys))
                        queue.append(((new_row, new_col), new_keys, path + 'P'))

                elif 'A' <= cell <= 'K':  # Door
                    required_key = key_door_pairs.get(cell.lower())
                    if required_key and (keys_collected & (1 << (ord(required_key) - ord('a')))):
                        if ((new_row, new_col), keys_collected) not in visited:
                            visited.add(((new_row, new_col), keys_collected))
                            queue.append(((new_row, new_col), keys_collected, path + move))

                elif cell in ('.', 'F', 'S') and ((new_row, new_col), new_keys) not in visited:  #Passable Cell
                    visited.add(((new_row, new_col), new_keys))
                    queue.append(((new_row, new_col), new_keys, path + move))


    print("-1")

solve()