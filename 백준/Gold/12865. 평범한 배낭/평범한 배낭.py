import sys

input = sys.stdin.readline

N, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1)

for weight, value in arr:
    for w in range(K, weight - 1, -1):
        dp[w] = max(dp[w], value + dp[w - weight])

print(max(dp))
