def merge_and_count(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1 
    k = left    
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

def min_transpositions_to_sort(n, p):
    min_transpositions = float('inf')

    for x in range(1, n + 1):
        left_part = p[(p.index(x)):] + p[:(p.index(x))]  
        temp_arr = [0] * n
        transpositions = merge_sort_and_count(left_part.copy(), temp_arr, 0, n - 1)
        min_transpositions = min(min_transpositions, transpositions)

    return min_transpositions

n = int(input())
p = list(map(int, input().split()))

print(min_transpositions_to_sort(n, p))