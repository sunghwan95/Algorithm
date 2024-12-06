import sys

input = sys.stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = []
    queue.append((x, y))

    while queue:
        _x, _y = queue.pop(0)

        for i in range(4):
            nx = _x + dx[i]
            ny = _y + dy[i]

            if (
                0 <= nx < N
                and 0 <= ny < M
                and graph[nx][ny] == 1
                and visited[nx][ny] == 0
            ):
                visited[nx][ny] = 1
                queue.append((nx, ny))


for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    visited = [[0] * M for _ in range(N)]

    cnt = 0

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and graph[i][j] == 1:
                visited[i][j] = 1
                bfs(i, j)
                cnt += 1

    print(cnt)
