import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for i in range(1, N + 1):
    graph.append(i)
visited = [0 for _ in range(N)]


def dfs(a):
    res.append(graph[a])

    if len(res) == M:
        print(*res)
        return

    for j in range(len(graph)):
        if visited[j] == 0:
            visited[j] = 1
            dfs(j)
            visited[j] = 0
            res.pop()


for i in range(N):
    res = []
    if visited[i] == 0:
        visited[i] = 1
        dfs(i)
        visited[i] = 0
