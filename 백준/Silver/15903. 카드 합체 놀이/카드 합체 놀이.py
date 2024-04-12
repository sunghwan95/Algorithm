import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

heapq.heapify(nums)

for _ in range(m):
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)

    c = a + b

    heapq.heappush(nums, c)
    heapq.heappush(nums, c)

print(sum(nums))
