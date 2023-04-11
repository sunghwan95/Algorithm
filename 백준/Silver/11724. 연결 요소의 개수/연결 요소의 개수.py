import sys
N, M = map(int, sys.stdin.readline().split())

visited = [0]*(N+1)

link = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    link[a].append(b)
    link[b].append(a)


def dfs(x):
    for i in link[x]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)


count = 0
for i in range(1, N+1):
    if visited[i] == 0:
        count += 1
        dfs(i)

print(count)
