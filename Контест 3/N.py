def check_answer(days):
    return days * a - a * (days // k) + days * b - b * (days // m) >= x


a, k, b, m, x = map(int, input().split())

left = 0
right = 10 ** 18
while left <= right:
    middle = (left + right) // 2
    if check_answer(middle):
        right = middle - 1
    else:
        left = middle + 1

print(left)