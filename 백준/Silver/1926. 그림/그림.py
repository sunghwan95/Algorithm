import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    area = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    area += 1
                    queue.append((nx, ny))

    return area


ans = 0
cnt = 0
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1 and visited[x][y] == 0:
            ans = max(bfs(x, y), ans)
            cnt += 1

print(cnt, ans, sep="\n")
