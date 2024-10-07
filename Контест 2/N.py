from collections import deque


def game():
    a = deque(map(int, input().split()))
    b = deque(map(int, input().split()))

    k = 1
    while k <= 10 ** 6:
        x = a.popleft()
        y = b.popleft()

        if x > y and not (x == 9 and y == 0) or (x == 0 and y == 9):
            a.append(x)
            a.append(y)
        else:
            b.append(x)
            b.append(y)

        if len(a) == 0:
            return f"second {k}"
        if len(b) == 0:
            return f"first {k}"

        k += 1

    return "botva"


print(game())