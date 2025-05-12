import heapq

T = int(input())

for i in range(1, T + 1):
    heap = []

    nums = list(map(int, input().split()))
    for num in nums:
        heapq.heappush(heap, (-num, num))

    print(f"#{i} {heap[0][-1]}")
