
s1 = list(input().lower())
s2 = list(input().lower())

if len(s1) != len(s2):
  print("NO")
  exit(0)

a = [0] * len(s1)
b = [0] * len(s1)
count = 0
for i in range(len(s1)):
  a[i] += s1.count(s1[i])

for i in range(len(s2)):
  b[i] += s2.count(s1[i])

if a==b:
  print("YES")
else:
  print("NO")
