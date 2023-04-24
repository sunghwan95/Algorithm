import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [0]*(N+1)
distance = [0]*(N+1)


def bfs(start):
    arr = deque([start])
    while arr:
        now = arr.popleft()
        visited[now] = 1

        for _next in graph[now]:
            if visited[_next] == 0:
                visited[_next] = 1
                distance[_next] = distance[now]+1
                arr.append(_next)


bfs(X)


if K not in distance:
    print(-1)
else:
    for i in range(1, len(distance)):
        if K == distance[i]:
            print(i)
