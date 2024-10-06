from collections import deque


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        return self.stack.pop()

    def len(self):
        return len(self.stack)

    def get_elem(self, index):
        return self.stack[index]


def solution():
    stack = Stack()
    dq = deque()
    num = 1
    for val in tr:
        if stack.len() > 0 and val > stack.get_elem(stack.len() - 1):
            return "NO"

        dq.append(1)
        stack.push(val)
        while stack.len() > 0 and stack.get_elem(stack.len() - 1) == num:
            dq.append(2)
            stack.pop()
            num += 1

    return "YES"


n = int(input())
tr = list(map(int, input().split()))
print(solution())