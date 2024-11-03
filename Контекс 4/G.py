import heapq

n = int(input())

heap = []
for i in range(n):
    f = int(input())
    heapq.heappush(heap, (max(1000 - f, 1), i, f + 1))


time = 0
pos = 0
while True:
    next_time, ind, f = heapq.heappop(heap)
    if time + abs(ind - pos) > next_time:
        break
    time = next_time
    pos = ind

    heapq.heappush(heap, (time + max(1000 - f, 1), ind, f + 1))

print(next_time)