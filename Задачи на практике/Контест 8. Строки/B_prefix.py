def prefix(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p


text = input()
pattern = input()

combined_string = pattern + "#" + text
prefix_values = prefix(combined_string)

pattern_length = len(pattern)
matches = []

for i, value in enumerate(prefix_values[pattern_length + 1:], start=pattern_length + 1):
    if value == pattern_length:
      matches.append(i - 2 * pattern_length)

print(*matches)


