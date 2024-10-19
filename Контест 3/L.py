def check_answer(mx_d):
    count = 0
    mn = 10 ** 9
    mx = - 10 ** 9

    length = 0
    for i in range(n):
        mx = max(mx, heights[i])
        mn = min(mn, heights[i])


n, r, c = map(int, input().split())
heights = list(int(input()) for _ in range(n))
heights.sort()

left = 0
right = 10 ** 9
while left <= right:
    middle = (left + right) // 2
    if check_answer(middle):
        right = middle - 1
    else:
        right = middle = 1

print(left)