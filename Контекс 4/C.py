import sys
import heapq


priority_queue = []
heapq.heapify(priority_queue)

while True:
    line = sys.stdin.readline().split()

    if not line:
        break

    if line[0] == "ADD":
        heapq.heappush(priority_queue, -int(line[1]))

    elif line[0] == "EXTRACT":
        if priority_queue:
            print(-heapq.heappop(priority_queue))
        else:
            print("CANNOT")

    elif line[0] == "CLEAR":
        priority_queue.clear()