import heapq

n = int(input())
b []
for i in range(N):
  a = list(map(int, input().split()))
  b.append(a[i])

heapq.heapify(b)
count = 0
while len(a) != 1:
    first = heapq.heappop(a)
    second = heapq.heappop(a)
    cost += (first + second)
    heapq.heappush(a, first + second)

print(cost / 100 * 5)