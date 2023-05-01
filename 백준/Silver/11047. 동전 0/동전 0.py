import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse=True)

count = 0
for coin in coins:
    if K < coin:
        continue
    count += K//coin
    K -= (K//coin)*coin
    if K == 0:
        print(count)
        break

