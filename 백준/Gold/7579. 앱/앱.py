import sys

input = sys.stdin.readline

N, M = map(int, input().split())

memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
total_cost = sum(costs)

app_by_cost = list(zip(memories, costs))

dp = [[0] * (total_cost + 1) for _ in range(N + 1)]
# dp[i][j] = i번째 앱까지 고려했을 때, 총 비용 j에서의 최대 메모리

for i, (memory, cost) in enumerate(app_by_cost):
    for j in range(total_cost + 1):
        dp[i + 1][j] = dp[i][j]

        if j >= cost:
            dp[i + 1][j] = max(dp[i][j], memory + dp[i][j - cost])

for j in range(total_cost + 1):
    if dp[N][j] >= M:
        print(j)
        break
