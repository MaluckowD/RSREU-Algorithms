
def prime_power(n):
    p = [1] * (n + 1)
    for i in range(1, n + 1):
        p[i] = (p[i - 1] * PRIME) % MOD
    return p


def hash_func(s):
    hashes = [0] * (len(s) + 1)
    for i in range(len(s)):
        hashes[i + 1] = (hashes[i] * PRIME + (ord(s[i]) - ord("a") + 1)) % MOD
    return hashes


def get_hash(p, hashes, l, r):
    return (hashes[r] - hashes[l - 1] * p[r - l + 1]) % MOD


text = input()
pattern = input()

PRIME = 31
MOD = 10**9 + 7

text_hashes = hash_func(text)
pattern_hash = hash_func(pattern)[-1]

max_length = len(text_hashes) -1
prime_powers = prime_power(max_length)


pattern_length = len(pattern)
matches = []


for i in range(1, len(text) - pattern_length + 2):
    if get_hash(prime_powers, text_hashes, i, i + pattern_length - 1) == pattern_hash:
        matches.append(i - 1)


print(*matches)