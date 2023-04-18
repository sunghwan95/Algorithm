import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())

heap = []

for i in range(N):
    a = int(sys.stdin.readline())
    if not heap and a == 0:
        print(0)

    else:
        heappush(heap, (-a, a))

    if heap and a == 0:
        print(heappop(heap)[1])
