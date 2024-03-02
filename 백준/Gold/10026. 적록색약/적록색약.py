import sys

input = sys.stdin.readline

N = int(input())
graph = []
visited = [[0 for _ in range(N)] for _ in range(N)]
abnormal_visited = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    _list = list(map(str, input().rstrip()))
    graph.append(_list)


def bfs(a, b):
    global color
    queue = []
    queue.append((a, b))
    color = graph[a][b]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and graph[nx][ny] == color:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


def abnormal_bfs(a, b):
    global abnormal_color
    queue = []
    queue.append((a, b))
    abnormal_color = graph[a][b]
    if abnormal_color == "R":
        abnormal_color = "G"

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == "R":
                    graph[nx][ny] = "G"

                if abnormal_visited[nx][ny] == 0 and graph[nx][ny] == abnormal_color:
                    abnormal_visited[nx][ny] = 1
                    queue.append((nx, ny))


count = 0
for x in range(N):
    for y in range(N):
        if visited[x][y] == 0:
            visited[x][y] = 1
            bfs(x, y)
            count += 1

_count = 0
for x in range(N):
    for y in range(N):
        if abnormal_visited[x][y] == 0:
            abnormal_visited[x][y] = 1
            abnormal_bfs(x, y)
            _count += 1

print(count, end=" ")
print(_count)
