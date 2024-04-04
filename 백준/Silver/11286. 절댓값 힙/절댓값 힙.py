import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    num = int(input())

    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(num), num))
