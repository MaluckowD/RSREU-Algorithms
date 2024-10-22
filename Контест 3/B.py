def binary_search(lst, n, target):
    left = 0
    right = n - 1

    answer = [10 ** 10, 10 ** 10]
    while left <= right:
        middle = (left + right) // 2

        d = abs(lst[middle] - target)
        if d <= answer[0]:
            if d < answer[0]:
                answer[1] = lst[middle]
            else:
                answer[1] = min(answer[1], lst[middle])
            answer[0] = d

        if lst[middle] == target:
            return lst[middle]

        if lst[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return answer[1]


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for item in b:
    print(binary_search(a, n, item))