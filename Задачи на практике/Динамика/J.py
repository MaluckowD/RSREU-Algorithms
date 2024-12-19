import math

n, m = map(int, input().split())

found = False
for i in range(1, 96):
    a = math.floor(((1 + math.sqrt(5)) / 2) * i + 1)
    b = math.floor(((3 + math.sqrt(5)) / 2) * i + 1)

    if (n == a and m == b) or (n == b and m == a):
        print(2)
        found = True
        break

if not found:
    print(1)