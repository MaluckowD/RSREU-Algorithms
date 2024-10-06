from sys import stdin

class Stack:
  def __init__(self):
    self.items = []
    
  def is_empty(self):
    return self.items == []
  
  def push(self, item):
    self.items.append(item)
    
  def pop(self):
    if self.is_empty():
      return "error"
    return self.items.pop()
  
  def back(self):
    if self.is_empty():
      return "error"
    return self.items[-1]
  
  def size(self):
    return len(self.items)
  
  def clear(self):
    self.items = []
    
  def exit(self):
    return "bye"

class Queue:
  def __init__(self):
    self.l = Stack()
    self.r = Stack()
    
  def is_empty(self):
    return self.l.is_empty() and self.r.is_empty()
  
  def push(self, item):
    self.l.push(item)
    
  def pop(self):
    if self.is_empty():
      return "error"
    if self.r.is_empty():
      while not self.l.is_empty():
        self.r.push(self.l.pop())
    return self.r.pop()
  
  def size(self):
    return self.l.size() + self.r.size()
  
  def front(self):
    if self.is_empty():
      return "error"
    if self.r.is_empty():
      while not self.l.is_empty():
        self.r.push(self.l.pop())
    return self.r.back()
  
  def clear(self):
    self.l.clear()
    self.r.clear()
  def exit(self):
    return "bye"

parts = []
q = Queue()
for line in stdin:
    parts.append(line.strip())


for i in range(len(parts)):
  if parts[i] == 'size':
    print(q.size())
    
  if parts[i][ :4 ] == 'push':
    q.push(int(parts[i].split()[1]))
    print("ok")
  
  if parts[i] == 'pop':
    print(q.pop())
  
  if parts[i] == 'front':
    print(q.front())
    
  if parts[i] == 'clear':
    q.clear()
    print("ok")

  if parts[i] == 'exit':
    print(q.exit())
    break
