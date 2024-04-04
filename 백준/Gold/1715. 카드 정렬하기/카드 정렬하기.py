import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []
for _ in range(N):
    a = int(input())
    heapq.heappush(heap, a)

result = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a + b)
    result += a + b

print(result)
