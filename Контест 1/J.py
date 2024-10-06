from sys import stdin
numbers = []

for line in stdin:
    numbers.append(line.strip())


def bubble_sort(arr):
  n = len(arr)
  for iter in range(n-1):
    swapper = False
    for i in range(n - iter - 1):
      if int(arr[i] + arr[i+1]) < int(arr[i + 1] + arr[i]):
        arr[i], arr[i+1] = arr[i+1], arr[i]
        swapper = True
    if not swapper:
      break
  return arr

print(''.join(bubble_sort(numbers)))
