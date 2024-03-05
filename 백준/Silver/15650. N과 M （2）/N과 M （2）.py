import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for i in range(1, N + 1):
    graph.append(i)
visited = [0 for _ in range(N)]
res = []


def dfs(a):
    visited[a] = 1

    if len(res) == M:
        print(*res)
        return

    for i in range(a, N):
        if visited[i] == 0:
            res.append(graph[i])
            dfs(i)
            res.pop()
            visited[i] = 0


for i in range(N):
    res.append(graph[i])
    dfs(i)
    res.pop()
