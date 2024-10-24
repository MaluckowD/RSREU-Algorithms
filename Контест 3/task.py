


def binary_search(x, arr):
  l = -1
  r = len(lst)
  
  while r - l > 1:
    m = (l + r) // 2
    if arr[m] <= x:
      l = m
    else:
      r = m
  if m - 1 == -1:
    return "No"
      
  return m - 1

lst = list(map(int,input().split()))

N = int(input())
print(binary_search(3,lst))


  