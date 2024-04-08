import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
w_queue = deque()
for i in range(R):
    row = list(input().rstrip())
    graph.append(row)
    for j, cell in enumerate(row):
        if cell == "S":
            hedgehog = (i, j)
        elif cell == "*":
            w_queue.append((i, j))

visited = [[0] * C for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    h_queue = deque([hedgehog])

    while h_queue:
        for _ in range(len(w_queue)):
            wx, wy = w_queue.popleft()

            for i in range(4):
                nwx = wx + dx[i]
                nwy = wy + dy[i]

                if 0 <= nwx < R and 0 <= nwy < C:
                    if graph[nwx][nwy] == ".":
                        graph[nwx][nwy] = "*"
                        w_queue.append((nwx, nwy))

        # 물이 먼저 차오른 다음에 고슴도치 이동
        for _ in range(len(h_queue)):
            hx, hy = h_queue.popleft()

            if graph[hx][hy] == "D":
                return visited[hx][hy]

            for j in range(4):
                nhx = hx + dx[j]
                nhy = hy + dy[j]
                if 0 <= nhx < R and 0 <= nhy < C:
                    if graph[nhx][nhy] == "." and visited[nhx][nhy] == 0:
                        visited[nhx][nhy] = visited[hx][hy] + 1
                        h_queue.append((nhx, nhy))
                    elif graph[nhx][nhy] == "D":
                        return visited[hx][hy] + 1

    return "KAKTUS"


print(bfs())
