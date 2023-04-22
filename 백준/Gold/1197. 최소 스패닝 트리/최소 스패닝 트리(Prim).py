import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
visited = [0]*(V+1)
edges = [[] for _ in range(V+1)]
for _ in range(E):
    current, _next, weight = map(int, input().split())
    edges[current].append((weight, _next))
    edges[_next].append((weight, current))

heap = [(0, 1)]
answer = 0
count = 0
while heap:
    if count == V:
        break
    weight, _next = heapq.heappop(heap)
    if visited[_next] == 0:
        visited[_next] = 1
        answer += weight
        count += 1
        for i in edges[_next]:
            heapq.heappush(heap, i)

print(answer)
