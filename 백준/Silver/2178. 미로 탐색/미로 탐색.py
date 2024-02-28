import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
visited = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    _list = list(map(int, input().rstrip()))
    graph.append(_list)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while queue:
        (x, y) = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    graph[nx][ny] += graph[x][y]


queue = []
for x in range(N):
    for y in range(M):
        if graph[x][y] == 1 and visited[x][y] == 0:
            visited[x][y] = 1
            queue.append((x, y))
            bfs()

print(graph[-1][-1])