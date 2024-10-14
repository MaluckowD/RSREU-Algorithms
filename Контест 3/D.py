def f(x):
    return a * x ** 3 + b * x * x + c * x + d


def find_section():
    r = 1
    while f(r) * f(-r) >= 0:
        r *= 2

    return r


def search_answer():
    init = find_section()

    left = -init
    right = init
    while left <= right:
        middle = (left + right) / 2
        cur = f(middle)
        if abs(cur) <= EPS:
            return middle

        if cur * f(right) > 0:
            right = middle
        else:
            left = middle


EPS = 1e-5

a, b, c, d = map(int, input().split())

print(search_answer())