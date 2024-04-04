import sys
import heapq

input = sys.stdin.readline

N = int(input())
graph = []

init_nums = list(map(int, input().split()))
for init_num in init_nums:
    heapq.heappush(graph, init_num)

for _ in range(N - 1):
    nums = list(map(int, input().split()))
    for num in nums:
        if num > graph[0]:
            heapq.heappush(graph, num)
            heapq.heappop(graph)

print(graph[0])
