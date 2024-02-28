import sys

input = sys.stdin.readline

T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs():
    while queue:
        (x, y) = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0 for _ in range(N)] for _ in range(M)]
    visited = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1

    queue = []
    count = 0

    for x in range(M):
        for y in range(N):
            if graph[x][y] == 1 and visited[x][y] == 0:
                queue.append((x, y))
                bfs()
                count += 1

    print(count)
