import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = [0] * (N + 1)
for i in range(1, N + 1):
    ans[i] = i


def dfs(start):
    for i in graph[start]:
        if visited[i] == 0:
            visited[i] = 1
            ans[i] = start
            dfs(i)


dfs(1)

print(*ans[2:], sep="\n")
