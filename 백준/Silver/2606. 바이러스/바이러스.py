N = int(input())
M = int(input())

visited = [0]*(N+1)

coms = [[] for _ in range(N+1)]
count = 0


for i in range(M):
    a, b = map(int, input().split())
    coms[a].append(b)
    coms[b].append(a)


def dfs(x):
    global count
    visited[x] = 1
    for i in coms[x]:
        if visited[i] == 0:
            count += 1
            dfs(i)


dfs(1)
print(count)
