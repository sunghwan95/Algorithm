import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

M, N = map(int, input().split())

graph = []
for _ in range(M):
    a = list(map(int, input().split()))
    graph.append(a)

visited = [[-1] * N for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        else:
            if graph[x][y] > graph[nx][ny]:
                visited[x][y] += dfs(nx, ny)

    return visited[x][y]


print(dfs(0, 0))
