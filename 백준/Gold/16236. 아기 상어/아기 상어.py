import sys
import heapq
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    a = list(map(int, input().split()))
    graph.append(a)


is_found_shark = False
for i in range(N):
    if is_found_shark == True:
        break

    for j in range(N):
        if graph[i][j] == 9:
            start_x, start_y = i, j
            graph[i][j] = 0
            is_found_shark = True
            break


def bfs(start_x, start_y, fish_cnt, shark):
    queue = deque([(start_x, start_y)])

    times = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    visited[start_x][start_y] = 1
    fishes = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if graph[nx][ny] <= shark:
                    visited[nx][ny] = 1
                    times[nx][ny] = times[x][y] + 1
                    queue.append((nx, ny))

                    if 0 < graph[nx][ny] < shark:
                        heapq.heappush(fishes, (times[nx][ny], nx, ny))

    if fishes:
        time, nx, ny = heapq.heappop(fishes)
        return (time, nx, ny, fish_cnt + 1)

    return False


shark = 2
fish_cnt = 0
ans = 0
while True:
    res = bfs(start_x, start_y, fish_cnt, shark)
    if not res:
        break

    time, x, y, fish_cnt = res
    if fish_cnt == shark:
        shark += 1
        fish_cnt = 0

    graph[x][y] = 0
    start_x, start_y = x, y

    ans += time

print(ans)
