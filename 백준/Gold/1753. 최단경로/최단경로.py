import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = int(1e9)
res = [INF] * (V+1)
heap = []


def dijkstra(start):
    heapq.heappush(heap, (0, start))
    res[start] = 0
    while heap:
        value, now = heapq.heappop(heap)
        if res[now] < value:
            continue
        for i in graph[now]:
            weight = value + i[1]
            if weight < res[i[0]]:
                res[i[0]] = weight
                heapq.heappush(heap, (weight, i[0]))


dijkstra(K)

for i in range(1, V+1):
    if res[i] == INF:
        print("INF")
    else:
        print(res[i])
