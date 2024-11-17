


def solve():
  for i in range(n):
    for j in range(n):
      if a[i][j] != a[j][i] or a[i][i] != 0:
        print("NO")
        return
  print("YES")


n = int(input())
a = [[int(i) for i in input().split()] for i in range(n)]
solve()    


      