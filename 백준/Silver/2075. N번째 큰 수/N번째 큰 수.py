import sys
import heapq

input = sys.stdin.readline

N = int(input())

init = list(map(int, input().split()))
heapq.heapify(init)

for _ in range(N - 1):
    nums = list(map(int, input().split()))

    for num in nums:
        if num > init[0]:
            heapq.heappush(init, num)
            heapq.heappop(init)

print(init[0])
