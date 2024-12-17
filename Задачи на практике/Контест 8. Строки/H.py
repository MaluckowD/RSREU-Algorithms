def manacher(text):
    modified_text = "#" + "#".join(text) + "#"
    n = len(modified_text)
    p = [0] * n
    center = 0
    right = 0

    for i in range(n):
        mirror = 2 * center - i

        if i < right:
            p[i] = min(right - i, p[mirror])

        while (i + p[i] + 1 < n and i - p[i] - 1 >= 0 and
               modified_text[i + p[i] + 1] == modified_text[i - p[i] - 1]):
            p[i] += 1

        if i + p[i] > right:
            center = i
            right = i + p[i]

    result = []
    for i in range(1, n, 2):
        result.append(p[i])

    return result


text = input()
result = manacher(text)
print(*result)