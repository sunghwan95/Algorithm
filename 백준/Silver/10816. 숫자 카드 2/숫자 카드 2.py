import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
ownedCards = list(map(int, input().split()))

M = int(input())
findCards = list(map(int, input().split()))

_ownedCards = Counter(ownedCards)
for findCard in findCards:
    ans = _ownedCards.get(findCard)
    if not ans:
        ans = 0
    print(ans, end=" ")
