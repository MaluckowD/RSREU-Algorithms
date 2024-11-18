

def solve():
  global count1, count2
  for i in range(n):
    count_zer = 0
    for j in range(n):
      if a[j][i] == 0:
        count_zer += 1
    if count_zer == n:
      b.append(i + 1)
      
  for i in range(n):
    count_zer = 0
    for j in range(n):
      if a[i][j] == 0:
        count_zer += 1
    if count_zer == n:
      c.append(i + 1)


b = []
c = []
count1 = count2 = 0
n = int(input())
a = [[int(i) for i in input().split()] for i in range(n)]
solve()
print(len(b))
print(*b, sep = '\n')
print(len(c))
print(*c, sep = '\n')

