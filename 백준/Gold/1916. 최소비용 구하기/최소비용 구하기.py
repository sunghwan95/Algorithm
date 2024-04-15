import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

graph = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    start, end, val = map(int, input().split())
    graph[start].append((val, end))

start, destination = map(int, input().split())

costs = [INF] * (N + 1)
costs[start] = 0


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        now_cost, start = heapq.heappop(heap)

        if now_cost > costs[start]:
            continue

        for i in graph[start]:
            next_cost, end = i
            new_cost = next_cost + now_cost
            if costs[end] > new_cost:
                costs[end] = new_cost
                heapq.heappush(heap, (new_cost, end))
            else:
                continue


dijkstra(start)
print(costs[destination])
