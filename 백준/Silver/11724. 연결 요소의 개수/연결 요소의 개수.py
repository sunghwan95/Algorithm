import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x):
    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)


count = 0
for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        count += 1

print(count)
