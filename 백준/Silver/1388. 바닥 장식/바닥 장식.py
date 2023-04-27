import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    a = list(map(str, input().rstrip()))
    graph.append(a)

visited = [[0]*M for _ in range(N)]


def dfs(x, y):
    visited[x][y] = 1
    if graph[x][y] == '|':
        if x+1 < N and graph[x+1][y] == '|' and visited[x+1][y] == 0:
            dfs(x+1, y)
        else:
            return

    if graph[x][y] == '-':
        if y+1 < M and graph[x][y+1] == '-' and visited[x][y+1] == 0:
            dfs(x, y+1)
        else:
            return


count = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            dfs(i, j)
            count += 1
print(count)
