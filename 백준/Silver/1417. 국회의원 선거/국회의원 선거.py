import sys
import heapq

input = sys.stdin.readline

N = int(input())
dasom = int(input())
candidates = []
for _ in range(N - 1):
    a = int(input())
    candidates.append((-a, a))
heapq.heapify(candidates)

ans = 0
while candidates:
    candidate = heapq.heappop(candidates)[1]
    if candidate >= dasom:
        candidate -= 1
        dasom += 1
        heapq.heappush(candidates, (-candidate, candidate))
        ans += 1

print(ans)
