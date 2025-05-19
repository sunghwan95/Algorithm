import sys

input = sys.stdin.readline

N, M = map(int, input().split())

apps = list(map(int, input().split()))
costs = list(map(int, input().split()))

zipped = list(zip(apps, costs))

sum_cost = sum(costs)
dp = [[0] * (sum_cost + 1) for _ in range(N + 1)]


for i, (memory, cost) in enumerate(zipped):
    for j in range(sum_cost + 1):
        dp[i + 1][j] = dp[i][j]

        if j >= cost:
            dp[i + 1][j] = max(dp[i + 1][j], memory + dp[i][j - cost])

for j in range(sum_cost + 1):
    if dp[N][j] >= M:
        print(j)
        break
