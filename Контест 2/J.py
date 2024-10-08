def solution(lst):
    if not lst:
        return 1

    lst = lst[:]  
    index_of_minimal = lst.index(min(lst))

    
    if lst[:index_of_minimal] != sorted(lst[:index_of_minimal], reverse=True):
        return 0

    del lst[index_of_minimal]

    return 1

n = int(input())
for _ in range(n):
    a = list(map(float, input().split()[1:]))
    print(solution(a))