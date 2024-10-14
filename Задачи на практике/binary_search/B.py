def bynary_search(arr, x):
    l, r = -1, len(arr)
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] < x:
            l = m
        else:
            r = m
    if r == len(arr) or arr[r] != x:
        return -1
    return r

N = int(input())
lst = list(map(int,input().split()))
q = int(input())
ls = list(map(int,input().split()))
for i in range(q):
  print(bynary_search(lst, ls[i]))