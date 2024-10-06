from math import factorial


def polish_calculator(expression):
  stack = []
  ls = expression.split()
  for token in ls:
    print(stack)
    if token.isdigit():
      stack.append(int(token))
    elif token == "+":
      a = stack.pop()
      b = stack.pop()
      stack.append(a + b)
    elif token == "-":
      a = stack.pop()
      b = stack.pop()
      stack.append(b - a)
    elif token == "*":
      a = stack.pop()
      b = stack.pop()
      stack.append(a * b)
    elif token == "/":
      a = stack.pop()
      b = stack.pop()
      stack.append(a / b)
    elif token == "~":
      stack.append(-stack.pop())
    elif token == "!":
      n = stack.pop()
      stack.append(factorial(n))
    elif token == "#":
      value = stack.pop()
      stack.append(value)
      stack.append(value)
    elif token == "@":
      nm3 = stack.pop()
      nm2 = stack.pop()
      nm1 = stack.pop()
      stack.append(nm2)
      stack.append(nm3)
      stack.append(nm1)
  return stack.pop()


st = input()

print(polish_calculator(st))