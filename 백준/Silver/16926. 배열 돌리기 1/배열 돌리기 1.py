import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = []
for i in range(N):
    a = list(map(int, input().split()))
    graph.append(a)


def rotate_layer(graph, start_x, end_x, start_y, end_y):
    temp = graph[start_x][start_y]

    # 위쪽 가로줄 반시계 방향 이동
    for i in range(start_y, end_y):
        graph[start_x][i] = graph[start_x][i + 1]

    # 오른쪽 세로줄 반시계 방향 이동
    for i in range(start_x, end_x):
        graph[i][end_y] = graph[i + 1][end_y]

    # 아래쪽 가로줄 반시계 방향 이동
    for i in range(end_y, start_y, -1):
        graph[end_x][i] = graph[end_x][i - 1]

    # 왼쪽 세로줄 반시계 방향 이동
    for i in range(end_x, start_x, -1):
        graph[i][start_y] = graph[i - 1][start_y]

    graph[start_x + 1][start_y] = temp


def rotate_graph(graph, row, col, R):
    for _ in range(R):
        start_x, start_y = 0, 0
        end_x, end_y = row - 1, col - 1
        while start_x < end_x and start_y < end_y:
            rotate_layer(graph, start_x, end_x, start_y, end_y)
            start_x += 1
            start_y += 1
            end_x -= 1
            end_y -= 1


rotate_graph(graph, N, M, R)
for ans in graph:
    print(*ans)
