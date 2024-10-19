def check_answer(length):
    return sum(num // length for num in lengths) >= k


n, k = map(int, input().split())
lengths = list(int(input()) for i in range(n))

left = 0
right = 10 ** 18
while left < right - 1:
    middle = (left + right) // 2
    if check_answer(middle):
        left = middle
    else:
        right = middle

print(left)