from collections import deque

T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())

    graph = [[0] * N for _ in range(N)]
    graph[0][0] = 1

    i = 0
    queue = deque([(0, 0)])

    cnt = 1
    while queue:
        if cnt == N * N:
            break

        q = queue.popleft()
        x, y = q[0], q[1]

        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= N or graph[nx][ny] != 0:
            i = (i + 1) % 4
            nx = x + dx[i]
            ny = y + dy[i]

        graph[nx][ny] = graph[x][y] + 1
        queue.append([nx, ny])
        cnt += 1

    print(f"#{tc}")
    for a in graph:
        print(*a)