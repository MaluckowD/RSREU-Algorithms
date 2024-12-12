def prefix(s):
    pref = [0] * len(s)
    for i in range(1, len(s)):
      k = pref[i - 1]
      while k > 0 and s[k] != s[i]:
        k = pref[k - 1]
      if s[k] == s[i]:
        k += 1
      pref[i] = k
    return pref


s = input()
pref = prefix(s)
print(*pref)