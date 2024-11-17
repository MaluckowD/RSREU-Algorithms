

def solve():
  global count1, count2
  for i in range(1, n + 1):
    for j in range(1,n + 1):
      print(a[j][i])
      if a[j][i] != 0:
        break
      count1 += 1
      a.append(i)
      
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      if a[i][j] != 0:
        break
      count2 += 1
      c.append(i)


b = []
c = []
count1 = count2 = 0
n = int(input())
a = [[int(i) for i in input().split()] for i in range(n)]
solve()

print(count1, count2)
print(b)

print(c)

