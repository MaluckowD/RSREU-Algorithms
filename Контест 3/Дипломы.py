w, h, n = map(int, input().split())

def good(x, w, h, n):
  return (x // w) * (x // h) >= n
  
l, r = 0, n * max(w, h)
while r - l > 1:
  m = (l + r)// 2
  if good(m, w, h, n):
    r = m
  else:
    l = m
    
print(r)