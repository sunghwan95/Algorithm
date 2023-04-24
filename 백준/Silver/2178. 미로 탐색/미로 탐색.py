from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))
visited = [[0]*(M) for _ in range(N)]
# print(f'graph : {graph}')
# print(f'visited : {visited}')


def bfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    coordinate = deque()
    coordinate.append((x, y))
    visited[x][y] = 1
    while coordinate:
        x, y = coordinate.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 0:
                continue

            if visited[nx][ny] == 0:
                graph[nx][ny] += graph[x][y]
                visited[nx][ny] = 1
                coordinate.append((nx, ny))
    print(graph[-1][-1])


bfs(0, 0)
