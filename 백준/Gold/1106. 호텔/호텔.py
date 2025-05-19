import sys

input = sys.stdin.readline

C, N = map(int, input().split())

arr = [tuple(map(int, input().split())) for _ in range(N)]

INF = float("inf")

dp = [[INF] * (C + 1) for _ in range(N + 1)]
dp[0][0] = 0
# dp[i][j] = i번째까지 고려했을 때, 적어도 j명까지 늘리기 위해 투자해야 하는 최소금액

for i, (cost, customer) in enumerate(arr):
    for j in range(C + 1):
        dp[i + 1][j] = dp[i][j]

        if j >= customer:
            dp[i + 1][j] = min(dp[i + 1][j], cost + dp[i + 1][j - customer])
        else:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][0] + cost)

print(min(dp[N][C:]))
