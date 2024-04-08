import sys
from collections import deque

input = sys.stdin.readline


def bfs(a, b):
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()

        if x == goal[0] and y == goal[1]:
            return 0

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l:
                if nx == goal[0] and ny == goal[1]:
                    return graph[x][y] + 1
                else:
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
                        graph[nx][ny] = graph[x][y] + 1


T = int(input())

dx = [-2, -1, 1, 2, 1, 2, -1, -2]
dy = [1, 2, 2, 1, -2, -1, -2, -1]
for _ in range(T):
    l = int(input())
    graph = [[0] * l for _ in range(l)]
    visited = [[0] * l for _ in range(l)]
    for i in range(2):
        a, b = map(int, input().split())
        if i == 0:
            start = (a, b)
        else:
            goal = (a, b)

    ans = bfs(start[0], start[1])
    print(ans)
