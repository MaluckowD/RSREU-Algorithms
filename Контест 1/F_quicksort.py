
def quick_sort(arr):
  if len(arr) <= 1:
    return arr

  val = arr[len(arr)//2]
  left = list(filter(lambda x: x < val,arr))
  center = [elem for elem in arr if elem == val]
  right = list(filter(lambda x: x > val, arr))
  return quick_sort(left) + center + quick_sort(right)
    

N = int(input())
arr = list(map(int,input().split()))
print(*quick_sort(arr))