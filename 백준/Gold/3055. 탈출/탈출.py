import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
for _ in range(R):
    a = list(map(str, input().rstrip()))
    graph.append(a)

visited = [[-1]*C for _ in range(R)]

queue = deque()
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == "*":
            queue.appendleft((i, j))
        elif graph[i][j] == "S":
            queue.append((i, j))
            visited[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if visited[nx][ny] != -1:
                continue
            if graph[nx][ny] == "*" or graph[nx][ny] == "X":
                continue
            if graph[nx][ny] == "D" and graph[x][y] == "*":
                continue
            if graph[nx][ny] == "D" and graph[x][y] == "S":
                return visited[x][y] + 1

            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y]+1
            graph[nx][ny] = graph[x][y]
    return "KAKTUS"


print(bfs())
