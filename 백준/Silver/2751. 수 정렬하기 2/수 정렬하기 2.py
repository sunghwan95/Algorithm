import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []
for _ in range(N):
    a = int(input())
    heapq.heappush(heap, a)

while heap:
    print(heapq.heappop(heap))
