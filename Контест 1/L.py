
km = list(map(int,input().split()))
count = list(map(int,input().split()))
km.sort(reverse = True)
count.sort()
ans = 0
for i in range(len(km)):
  ans += km[i] * count[i]

print(ans)