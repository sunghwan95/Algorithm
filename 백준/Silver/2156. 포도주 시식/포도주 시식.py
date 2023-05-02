import sys
input = sys.stdin.readline

N = int(input())

wine = []
for _ in range(N):
    a = int(input())
    wine.append(a)

dp = [0 for _ in range(N)]


for i in range(N):
    if N == 1:
        print(wine[0])
        exit(0)
    elif N == 2:
        print(max(wine[0] + wine[1], wine[1]))
        exit(0)
    elif N == 3:
        print(max(wine[1]+wine[2], wine[0] + wine[2], wine[0]+wine[1]))
        exit(0)
    else:
        dp[0] = wine[0]
        dp[1] = max(wine[0] + wine[1], wine[1])
        dp[2] = max(wine[1]+wine[2], wine[0] + wine[2], wine[0]+wine[1])
        dp[i] = max(dp[i-3] + wine[i-1] + wine[i], dp[i-2]+wine[i], dp[i-1])

print(dp[-1])
