def solve():
    n = int(input())
    cost = list(map(int, input().split()))

    if n <= 0:
        print(0)
        return

    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

    print(dp[n - 1])


solve()