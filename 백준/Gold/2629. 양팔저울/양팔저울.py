import sys

input = sys.stdin.readline

N = int(input())
weights = list(map(int, input().split()))
total_weight = sum(weights)

M = int(input())
beads = list(map(int, input().split()))

dp = [[False] * (total_weight + 1) for _ in range(N + 1)]
dp[0][0] = True

for i, weight in enumerate(weights):
    for j in range(total_weight + 1):
        if dp[i][j]:
            dp[i + 1][j] = dp[i][j]
            dp[i + 1][abs(j - weight)] = True
            if j + weight <= total_weight:
                dp[i + 1][j + weight] = True

for bead in beads:
    if bead > total_weight:
        print("N", end=" ")
    else:
        if dp[N][bead]:
            print("Y", end=" ")
        else:
            print("N", end=" ")
