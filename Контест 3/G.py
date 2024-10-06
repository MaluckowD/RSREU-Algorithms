def good(x):
  cnt = 0
  for ln in a:
    cnt += ln // x
  return cnt >= k

n, k = map(int, input().split())
a = [int(input()) for i in range(n)]
l, r = 0, 10 ** 7 + 1
for i in range(100):
  m = (l + r) / 2
  if good(m):
    l = m
  else:
    r = m
print(l)