import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    sticker1 = list(map(int, input().split()))
    sticker2 = list(map(int, input().split()))

    if n == 1:
        print(max(sticker1[0], sticker2[0]))
        continue

    dp = [[0] * 3 for _ in range(n)]

    dp[0][0] = sticker1[0]
    dp[0][1] = sticker2[0]
    dp[0][2] = 0

    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + sticker1[i]
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + sticker2[i]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])

    ans = max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])
    print(ans)
