import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())

box = []
for _ in range(H):
    graph = []
    for _ in range(N):
        a = list(map(int, input().split()))
        graph.append(a)
    box.append(graph)

visited = [[[0]*M for _ in range(N)] for _ in range(H)]

queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1 and visited[i][j][k] == 0:
                visited[i][j][k] = 1
                queue.append((i, j, k))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]

            if nx < 0 or nx >= H or ny < 0 or ny >= N or nz < 0 or nz >= M:
                continue

            if box[nx][ny][nz] == 0 and visited[nx][ny][nz] == 0:
                visited[nx][ny][nz] = 1
                box[nx][ny][nz] = box[x][y][z]+1
                queue.append((nx, ny, nz))


bfs()

answer = 0
for level in box:
    for line in level:
        for tomato in line:
            if tomato == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(line))

print(answer-1)
