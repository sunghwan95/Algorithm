import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
visited = [0]*(N+1)

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0


def dfs(x):
    global count
    visited[x] = 1
    for i in graph[x]:
        if visited[i] == 0:
            dfs(i)
            count += 1


dfs(1)
print(count)
