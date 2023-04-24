import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1]*(N+1)
distance[X] = 0


def bfs(start):
    arr = [start]
    while arr:
        now = arr.pop(0)

        for _next in graph[now]:
            if distance[_next] == -1:
                distance[_next] = distance[now]+1
                arr.append(_next)


bfs(X)


if K not in distance:
    print(-1)
else:
    for i in range(1, len(distance)):
        if K == distance[i]:
            print(i)
