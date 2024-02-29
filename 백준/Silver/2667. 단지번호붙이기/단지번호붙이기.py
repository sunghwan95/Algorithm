import sys
input = sys.stdin.readline

N = int(input())

graph = []
visited = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    _list = list(map(int, input().rstrip()))
    graph.append(_list)


res = []
def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = []
    queue.append((x, y))
    houseCount = 1

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    houseCount += 1
    res.append(houseCount)


count = 0
for x in range(N):
    for y in range(N):
        if graph[x][y] == 1 and visited[x][y] == 0:
            visited[x][y] = 1
            bfs(x, y)
            count += 1

res.sort()
print(count)
print(*res, sep="\n")
