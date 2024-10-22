def check_answer(d):
    return max((w // (a + 2 * d)) * (h // (b + 2 * d)), (w // (b + 2 * d)) * (h // (a + 2 * d))) >=n


n, a, b, w, h = map(int, input().split())

left = 0
right = min(w, h)
ans = 0
while left + 1 < right:
    middle = (left + right) // 2
    if check_answer(middle):
        left = middle
    else:
        right = middle

print(left)