import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

visited = [0 for _ in range(N+1)]
edges = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

parent = [0 for _ in range(N+1)]
for i in range(N+1):
    parent[i] = i


def dfs(x):
    for i in edges[x]:
        if visited[i] == 0:
            visited[i] = 1
            parent[i] = x
            dfs(i)


dfs(1)
for i in parent[2:]:
    print(i)
