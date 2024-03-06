import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = list((map(int, input().split())))
visited = [0 for _ in range(N)]
graph.sort()


def dfs(a):
    if len(res) == M:
        print(*res)
        return

    for i in range(a, N):
        if visited[i] == 0:
            visited[i] = 1
            res.append(graph[i])
            dfs(i)
            res.pop()
            visited[i] = 0


res = []
for i in range(N):
    if visited[i] == 0:
        visited[i] = 1
        res.append(graph[i])
        dfs(i)
        res.pop()
