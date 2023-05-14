import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    while queue:
        (x, y) = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                else:
                    continue
    return


T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque()
    count = 0

    for _ in range(K):
        Y, X = map(int, input().split())
        graph[X][Y] = 1

    for x in range(N):
        for y in range(M):
            if graph[x][y] == 1 and visited[x][y] == 0:
                visited[x][y] = 1
                queue.append((x, y))
                bfs(x, y)
                count += 1
    print(count)
