
from collections import deque

def shortest_path(matrix):
  rows, cols = len(matrix), len(matrix[0])
  start, end = (0, 0), (rows - 1, cols - 1)

  if matrix[start[0]][start[1]] == -1 or matrix[end[0]][end[1]] == -1:
    return -1

  queue = deque([(start, 0)])
  visited = set()
  visited.add(start)
  
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

  while queue:
    (row, col), distance = queue.popleft()
    
    if (row, col) == end:
      return distance

    for dr, dc in directions:
      next_row, next_col = row + dr, col + dc
      if 0 <= next_row < rows and 0 <= next_col < cols and \
        matrix[next_row][next_col] == 0 and (next_row, next_col) not in visited:
        queue.append(((next_row, next_col), distance + 1))
        visited.add((next_row, next_col))

  return -1


n, m = map(int, input().split())
matrix = []
for i in range(n):
  row = list(map(int, input().split()))
  matrix.append(row)

result = shortest_path(matrix)
print(result)