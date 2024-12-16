PRIME = 31
MOD = 1000000007
ARR_SIZE = 1000000

def hash_func(s):
    h = 0
    for c in s:
        h = (h * PRIME + (ord(c) - ord('a') + 1)) % MOD
    return h % ARR_SIZE


arr = [[] for _ in range(ARR_SIZE)]


while True:
    inp = input()
    if inp == "#":
        break

    op = inp[0]
    word = inp[2:]
    h = hash_func(word)

    if op == '+':
        arr[h].append(word)
    elif op == '-':
        try:
            arr[h].remove(word)
        except ValueError:
            pass
    else:
        print("YES" if word in arr[h] else "NO")