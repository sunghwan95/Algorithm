import sys
import heapq

N = int(sys.stdin.readline())

heap = []
for _ in range(N):
    a = int(sys.stdin.readline())
    heapq.heappush(heap, a)

result = 0
while True:
    if N == 1:
        print(0)
        break

    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a+b)
    result += a+b

    if len(heap) == 2:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        print(result+a+b)
        break
