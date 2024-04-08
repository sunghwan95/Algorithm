import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range(N):
    a = list(map(int, input().rstrip()))
    graph.append(a)

visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    queue.append((0, 0, 0))

    while queue:
        x, y, z = queue.popleft()

        if x == N - 1 and y == M - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append((nx, ny, z))
                elif graph[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))
    return -1


print(bfs())
