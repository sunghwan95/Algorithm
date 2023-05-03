import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])
arr = sorted(arr, key=lambda x: x[0])

heap = []
heapq.heappush(heap, arr[0][1])
for i in range(1, N):
    if heap[0] > arr[i][0]:
        heapq.heappush(heap, arr[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, arr[i][1])

print(len(heap))
