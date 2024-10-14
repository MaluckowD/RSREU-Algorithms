def check(length, points, k):
  count = 1
  start = points[0]  
  for i in range(1, len(points)):
    if points[i] - start > length:  
      count += 1  
      start = points[i]  
  return count <= k #Проверяет, можно ли покрыть все точки k отрезками длины length

def min_length(n, k, points):
  points.sort() 
  left = 0 
  right = points[-1] - points[0]
  while left < right:
    mid = (left + right) // 2 
    if check(mid, points, k):
      right = mid  
    else:
      left = mid + 1  
  return left  

n, k = map(int, input().split())
points = list(map(int, input().split()))
print(min_length(n, k, points))