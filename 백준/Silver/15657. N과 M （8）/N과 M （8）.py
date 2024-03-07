import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = list(map(int, input().split()))
graph.sort()


def dfs(a):
    if len(res) == M:
        print(*res)
        return

    for i in range(a, N):
        res.append(graph[i])
        dfs(i)
        res.pop()


res = []
for i in range(N):
    res.append(graph[i])
    dfs(i)
    res.pop()
