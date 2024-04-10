import sys
from collections import deque

input = sys.stdin.readline

graph = [list(input().rstrip()) for _ in range(12)]


def bfs(x, y, color):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    # 터질 예정인 뿌요를 빈 공간으로 만들어주기 위한 배열
    puyo_about_to_explode = [(x, y)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 12 and 0 <= ny < 6:
                if visited[nx][ny] == 0 and graph[nx][ny] == color:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    puyo_about_to_explode.append((nx, ny))

    return puyo_about_to_explode


ans = 0
while True:
    visited = [[0] * 6 for _ in range(12)]
    is_popped = False
    for x in range(12):
        for y in range(6):
            if visited[x][y] == 0 and graph[x][y] != ".":
                # bfs탐색을 통해 해당 좌표와 같은 색의 뿌요가 연결되어 있는지 확인
                puyo_about_to_explode = bfs(x, y, graph[x][y])
                if len(puyo_about_to_explode) >= 4:
                    is_popped = True
                    # 터진 뿌요의 자리를 빈 공간으로 갱신
                    for nx, ny in puyo_about_to_explode:
                        graph[nx][ny] = "."

    if is_popped:
        # 뿌요가 터졌으면 위의 뿌요들을 아래로 떨궈줘야함
        # 열을 차례대로 탐색(0~5까지)
        # 각 열의 가장 바닥 행부터 탐색하여 뿌요가 나오는 위치 확인(11~)
        for y in range(6):
            for x in range(10, -1, -1):
                # 빈 공간탐색은 처음으로 뿌요가 발견되는 지점까지만 확인하면됨
                for k in range(11, x, -1):
                    if graph[k][y] == "." and graph[x][y] != ".":
                        graph[k][y] = graph[x][y]
                        graph[x][y] = "."
                        break
        ans += 1
    else:
        break

print(ans)
