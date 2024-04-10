import sys
import heapq

input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    a = int(input())

    if a == 0:
        if not nums:
            print(0)
            continue
        else:
            print(heapq.heappop(nums))
            continue
    else:
        heapq.heappush(nums, a)
