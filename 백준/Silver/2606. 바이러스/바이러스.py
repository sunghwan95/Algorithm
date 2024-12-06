import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N + 1)

cnt = 0


def dfs(start):
    global cnt

    visited[start] = 1

    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1


dfs(1)
print(cnt)
