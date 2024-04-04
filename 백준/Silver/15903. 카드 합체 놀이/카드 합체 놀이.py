import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

heapq.heapify(nums)

for _ in range(m):
    x = heapq.heappop(nums)
    y = heapq.heappop(nums)
    add_num = x + y
    heapq.heappush(nums, add_num)
    heapq.heappush(nums, add_num)

print(sum(nums))
