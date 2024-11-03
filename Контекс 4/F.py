import heapq


n = int(input())
a = list(tuple(map(int, input().split())) for _ in range(n))
a.sort()

heap = []
heapq.heapify(heap)

mx = 0
for i in range(n):
    
    while heap and heap[0] <= a[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, a[i][0] + a[i][1])

    mx = max(mx, len(heap))

print(mx)
