import sys

input = sys.stdin.readline


def bfs(a, b):
    queue = []
    queue.append((a, b))

    dx = [-1, -1, 1, 1, -1, 1, 0, 0]
    dy = [-1, 1, -1, 1, 0, 0, -1, 1]

    while queue:
        x, y = queue.pop(0)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


res = []
while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        _list = list(map(int, input().split()))
        graph.append(_list)
    visited = [[0 for _ in range(w)] for _ in range(h)]

    count = 0
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1 and visited[x][y] == 0:
                visited[x][y] = 1
                bfs(x, y)
                count += 1

    res.append(count)

print(*res, sep="\n")
