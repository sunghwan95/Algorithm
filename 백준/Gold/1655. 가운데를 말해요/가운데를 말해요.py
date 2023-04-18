import sys
import heapq

N = int(sys.stdin.readline())

# 중간 값보다 작은 heap배열
low_heap = []
# 중간 값보다 큰 heap배열
high_heap = []
answer = []

for _ in range(N):
    num = int(sys.stdin.readline())

    if len(low_heap) == len(high_heap):
        # 중간 값보다 작은 값들은 최대힙 정렬
        heapq.heappush(low_heap, (-num, num))
    else:
        # 중간 값보다 높은 값들은 최소힙 정렬
        heapq.heappush(high_heap, num)

    if high_heap and high_heap[0] < low_heap[0][1]:
        high_num = heapq.heappop(low_heap)[1]
        low_num = heapq.heappop(high_heap)
        heapq.heappush(low_heap, (-low_num, low_num))
        heapq.heappush(high_heap, high_num)
    
    answer.append(low_heap[0][1])

for i in answer:
    print(i)