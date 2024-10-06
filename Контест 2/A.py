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

parts = []
s = Stack()
for line in stdin:
    parts.append(line.strip())



for i in range(len(parts)):
  if parts[i] == 'size':
    print(s.size())
    
  if parts[i][ :4 ] == 'push':
    s.push(int(parts[i].split()[1]))
    print("ok")
  
  if parts[i] == 'pop':
    print(s.pop())
  
  if parts[i] == 'back':
    print(s.back())
    
  if parts[i] == 'clear':
    s.clear()
    print("ok")

  if parts[i] == 'exit':
    print(s.exit())
    break

