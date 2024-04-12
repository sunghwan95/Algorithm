import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for arr in graph:
    if arr:
        arr.sort(reverse=True)

visited = [0] * (N + 1)
ans = [0] * (N + 1)


cnt = 1


def dfs(start):
    global cnt
    visited[start] = 1
    ans[start] = cnt

    for i in graph[start]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)


dfs(R)
print(*ans[1:], sep="\n")
