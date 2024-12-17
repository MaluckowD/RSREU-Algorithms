PRIME = 31
MOD = 1000000007
ARR_SIZE = 1000000

def hash_func(s):
    hash_val = 0
    for c in s:
        hash_val = (hash_val * PRIME + (ord(c) - ord('a') + 1)) % MOD
    return hash_val % ARR_SIZE

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
        if word in arr[h]:
            arr[h].remove(word)
    else:
        if word in arr[h]:
            print("YES")
        else:
            print("NO")