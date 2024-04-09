import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

for island in range(1, N + 1):
    sorted(graph[island], key=lambda x: -x[0])

weights = [0] * (N + 1)
a, b = map(int, input().split())


def dijkstra(start, end):
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        weight, now = heapq.heappop(queue)
        weight = -weight

        if now == end:
            print(weight)
            break

        if weights[now] > weight:
            continue

        for island in graph[now]:
            if weight == 0:
                weights[island[1]] = island[0]
                heapq.heappush(queue, (-weights[island[1]], island[1]))

            elif weights[island[1]] < island[0] and weights[island[1]] < weight:
                weights[island[1]] = min(weight, island[0])
                heapq.heappush(queue, (-weights[island[1]], island[1]))


dijkstra(a, b)
