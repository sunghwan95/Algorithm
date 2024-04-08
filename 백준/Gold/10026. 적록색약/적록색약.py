import sys

input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    _list = list(map(str, input().rstrip()))
    graph.append(_list)

visited = [[0 for _ in range(N)] for _ in range(N)]
color_weakness_visited = [[0 for _ in range(N)] for _ in range(N)]


def bfs(a, b, is_color_weakness, visited_arr):
    queue = []
    queue.append((a, b))
    color = graph[a][b]

    if is_color_weakness and color == "R":
        color = "G"

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                next_color = graph[nx][ny]
                if is_color_weakness and next_color == "R":
                    next_color = "G"

                if visited_arr[nx][ny] == 0 and next_color == color:
                    visited_arr[nx][ny] = 1
                    queue.append((nx, ny))


count = 0
for x in range(N):
    for y in range(N):
        if visited[x][y] == 0:
            visited[x][y] = 1
            bfs(x, y, False, visited)
            count += 1

_count = 0
for x in range(N):
    for y in range(N):
        if color_weakness_visited[x][y] == 0:
            color_weakness_visited[x][y] = 1
            bfs(x, y, True, color_weakness_visited)
            _count += 1

print(count, _count)
