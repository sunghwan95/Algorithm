import sys
input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    a = list(map(int, input().rstrip()))
    graph.append(a)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    queue = []
    queue.append((a, b))

    visited = [[0]*N for _ in range(N)]
    visited[a][b] = 1

    count = 1

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


result = []
for a in range(N):
    for b in range(N):
        if graph[a][b] == 1:
            graph[a][b] = 0
            result.append(bfs(a, b))

result.sort()
print(len(result))

for i in result:
    print(i)
