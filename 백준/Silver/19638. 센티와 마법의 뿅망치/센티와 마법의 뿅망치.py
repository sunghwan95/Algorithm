import sys
import heapq

input = sys.stdin.readline

N, H, T = map(int, input().split())

heap = []
for _ in range(N):
    giant_height = int(input())
    heap.append((-giant_height, giant_height))
heapq.heapify(heap)

count = 0
success = False
while T > 0:
    largest_height = heap[0][1]
    if largest_height < H or largest_height == 1:
        break

    target_height = heapq.heappop(heap)[1] // 2
    heapq.heappush(heap, (-target_height, target_height))
    T -= 1
    count += 1

    if heap[0][1] < H:
        success = True
        break

max_target_height = heap[0][1]
if success or max_target_height < H:
    print("YES")
    print(count)
else:
    print("NO")
    print(max_target_height)
