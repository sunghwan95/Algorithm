import sys

input = sys.stdin.readline

N, T = map(int, input().split())

arr = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * (T + 1) for _ in range(N + 1)]
# dp[i][j] = i번쨰 단원까지 공부했을 때, j시간에서 얻을 수 있는 최대 점수

for i, (time, score) in enumerate(arr):
    for j in range(T + 1):
        dp[i + 1][j] = dp[i][j]

        if j >= time:
            dp[i + 1][j] = max(dp[i][j], score + dp[i][j - time])

print(max(dp[N]))
