import sys
input = sys.stdin.readline

N = int(input())

stairs = []
for _ in range(N):
    a = int(input().strip())
    stairs.append(a)

dp = [0 for _ in range(N)]


for i in range(N):
    if N == 1:
        print(stairs[0])
        exit(0)
    elif N == 2:
        print(max(stairs[0] + stairs[1], stairs[1]))
        exit(0)
    elif N == 3:
        print(max(stairs[1]+stairs[2], stairs[0] + stairs[2]))
        exit(0)
    else:
        dp[0] = stairs[0]
        dp[1] = max(stairs[0] + stairs[1], stairs[1])
        dp[2] = max(stairs[1]+stairs[2], stairs[0] + stairs[2])
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2]+stairs[i])

print(dp[-1])
