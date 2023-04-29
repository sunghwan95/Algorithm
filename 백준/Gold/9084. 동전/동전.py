import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    total = int(input())
    dp = [0 for _ in range(total+1)]
    dp[0] = 1
    for coin in coins:
        for cost in range(1, total+1):
            if cost >= coin:
                dp[cost] = dp[cost]+dp[cost-coin]

    print(dp[total])
