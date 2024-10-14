def bynary_searchl(arr, x):
    l, r = 0, len(arr) - 1
    ans = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] < x:
          l = m + 1
        elif arr[m] > x:
          r = m - 1
        else:
          ans = m
          r = m - 1
          
    return ans

def bynary_searchr(arr, x):
    l, r = 0, len(arr) - 1
    ans = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] < x:
          l = m + 1
        elif arr[m] > x:
          r = m - 1
        else:
          ans = m
          l = m + 1
          
    return ans

N = int(input())
lst = list(map(int,input().split()))
q = int(input())
ls = list(map(int,input().split()))
for i in range(q):
  if (bynary_searchr(lst, ls[i]) == -1 and bynary_searchl(lst, ls[i]) == -1):
    print(0, end = ' ')
  else:
    print(bynary_searchr(lst, ls[i]) - bynary_searchl(lst, ls[i]) + 1, end = ' ')