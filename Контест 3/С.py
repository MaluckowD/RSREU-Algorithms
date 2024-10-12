C = float(input())

def f(x):
  return x ** 2 + x ** 0.5 

l, r = 0, C ** 0.5
while l < r:
    m = (l + r) / 2
    if abs(f(m) - C) < 10e-7:
      print(m)
      break
    if f(m) < C:
        l = m
    else:
        r = m


