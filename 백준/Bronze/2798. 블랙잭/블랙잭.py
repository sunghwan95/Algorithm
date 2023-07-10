import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            threeSum = cards[i]+cards[j]+cards[k]
            if threeSum <= M:
                ans = max(ans, threeSum)

print(ans)
