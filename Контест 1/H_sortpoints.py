from functools import cmp_to_key

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
      return (self.x**2 + self.y**2) ** 0.5

def compare(x,y):
  return x.distance() - y.distance()

points = []
n = int(input())

for i in range(n):
  x, y = map(int, input().split())
  points.append(Point(x, y))

points.sort(key = cmp_to_key(compare))

for point in points:
    print(point.x,point.y)

