import sys

input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    a = list(map(int, input().rstrip()))
    graph.append(a)

visited = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = []
    queue.append((x, y))

    cnt = 1
    while queue:
        _x, _y = queue.pop(0)

        for i in range(4):
            nx = _x + dx[i]
            ny = _y + dy[i]

            if (
                0 <= nx < N
                and 0 <= ny < N
                and graph[nx][ny] == 1
                and visited[nx][ny] == 0
            ):
                visited[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1

    return cnt


_cnt = 0
nums = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            a = bfs(i, j)
            nums.append(a)
            _cnt += 1

nums.sort()
print(_cnt, *nums, sep="\n")
