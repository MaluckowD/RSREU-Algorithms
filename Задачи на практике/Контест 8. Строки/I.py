def prefix_function(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p


def min_moves_unlock(current, target):
    s = current + "#" + target
    pi = prefix_function(s)
    return len(current) - pi[-1]



current = input()
target = input()

result = min_moves_unlock(current, target)
print(result)
