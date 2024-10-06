from collections import deque

N = int(input())

class Queue:
  def __init__(self):
    self.queue = deque([])

  def push(self, item):
    self.queue.append(item)
  
  def push_center(self,item):
    if len(self.queue) % 2 == 0:
      self.queue.insert(len(self.queue)//2, item)
    else:
      self.queue.insert(len(self.queue)//2 + 1, item)

  def pop(self):
    item = self.queue.popleft()
 
  def back(self):
    return self.queue[0]

q = Queue()    
lst = []
for i in range(N):
  lst.append(input().split())


for i in range(N):
  if lst[i][0] == "+":
    q.push(lst[i][-1])
  
  if lst[i][0] == "*":
    q.push_center(lst[i][-1])
    
  if lst[i][0] == "-":
    print(q.back())
    q.pop()
    