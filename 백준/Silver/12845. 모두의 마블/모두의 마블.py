import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cards.sort(reverse=True)
a = cards[0]

ans = 0
for i, card in enumerate(cards):
    if i == 0:
        continue
    ans += (a+card)

print(ans)
