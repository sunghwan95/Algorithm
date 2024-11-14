import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

heapq.heapify(nums)

for _ in range(m):
    v1 = heapq.heappop(nums)
    v2 = heapq.heappop(nums)
    new_val = v1 + v2

    heapq.heappush(nums, new_val)
    heapq.heappush(nums, new_val)

print(sum(nums))
