import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for arr in graph:
    arr.sort()

visited = [0] * (N + 1)

ans = [0] * N

count = 1


def dfs(R):
    global count
    visited[R] = 1
    ans[R - 1] = count
    for i in graph[R]:
        if visited[i] == 0:
            visited[i] = 1
            count += 1
            dfs(i)


dfs(R)
print(*ans, sep="\n")
