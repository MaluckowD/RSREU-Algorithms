def z_func(s):
    n = len(s)
    z = [0] * n
    left, right = 0, 0
    for i in range(1, n):
        k = max(0, min(z[i - left], right - i))
        while i + k < n and s[k] == s[i + k]:
            k += 1
        z[i] = k
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


text = input()
pattern = input()

combined_string = pattern + "#" + text
z_values = z_func(combined_string)
pattern_length = len(pattern)

matches = []

for i, value in enumerate(z_values[pattern_length + 1:], start=pattern_length + 1):
    if value == pattern_length:
      matches.append(i - pattern_length - 1)

print(*matches)