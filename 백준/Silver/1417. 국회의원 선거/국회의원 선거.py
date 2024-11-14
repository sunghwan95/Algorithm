import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []
for i in range(N):
    num = int(input())

    if i == 0:
        dasom = -num
    else:
        heapq.heappush(heap, -num)

if N == 1:
    print(0)
    exit(0)

cnt = 0
while True:
    now = heapq.heappop(heap)

    if dasom >= now:
        dasom -= 1
        heapq.heappush(heap, now + 1)
        cnt += 1
    else:
        print(cnt)
        break
