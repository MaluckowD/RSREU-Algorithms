from collections import deque
from sys import stdin
dq = deque()

parts = []
for line in stdin:
    parts.append(line.strip())

for i in range(len(parts)):
  if parts[i] == 'size':
    print(len(dq))
    
  if parts[i][ :10 ] == 'push_front':
    dq.appendleft(int(parts[i].split()[1]))
    print("ok")
    
  if parts[i][ :9 ] == 'push_back':
    dq.append(int(parts[i].split()[1]))
    print("ok")
  
  if parts[i] == 'pop_front':
    if len(dq) == 0:
       print("error")
    else:
       print(dq.popleft())
  
  if parts[i] == 'pop_back':
    if len(dq) == 0:
       print("error")
    else:
       print(dq.pop())
  
  if parts[i] == 'front':
    if len(dq) == 0:
       print("error")
    else:
       print(dq[0])
  
  if parts[i] == 'back':
    if len(dq) == 0:
       print("error")
    else:
       print(dq[-1])
    
  if parts[i] == 'clear':
    dq.clear()
    print("ok")

  if parts[i] == 'exit':
    print("bye")
    break