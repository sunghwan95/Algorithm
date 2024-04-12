import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, D = map(int, input().split())

# i번째에서 i+1번째로 가는 비용을 1로 초기화
graph = [[] for _ in range(D + 1)]
for i in range(D):
    graph[i].append((i + 1, 1))

for _ in range(N):
    start, end, length = map(int, input().split())
    if end > D:
        continue
    graph[start].append((end, length))

distance = [INF] * (D + 1)


def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 0))
    distance[0] = 0

    while heap:
        now, cost = heapq.heappop(heap)

        if cost > distance[now]:
            continue

        for i in graph[now]:
            _next = i[0]
            short_cut_cost = i[1]
            total_cost = cost + short_cut_cost

            if total_cost < distance[_next]:
                distance[_next] = total_cost
                heapq.heappush(heap, (_next, total_cost))


dijkstra()

print(distance[D])
