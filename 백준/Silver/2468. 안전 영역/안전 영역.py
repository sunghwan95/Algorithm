import sys

input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    _list = list(map(int, input().split()))
    graph.append(_list)

max_precipitations = []
min_precipitations = []
for _graph in graph:
    max_precipitations.append(max(_graph))
    min_precipitations.append(min(_graph))


def bfs(a, b, c):
    queue = []
    queue.append((a, b))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > c and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


count = 1
for i in range(min(min_precipitations), max(max_precipitations) + 1):
    _count = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if graph[x][y] > i and visited[x][y] == 0:
                visited[x][y] = 1
                bfs(x, y, i)
                _count += 1
    count = max(count, _count)

print(count)
