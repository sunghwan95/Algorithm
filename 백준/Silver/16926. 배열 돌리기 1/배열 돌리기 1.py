import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = []
for i in range(N):
    a = list(map(int, input().split()))
    graph.append(a)


def rotate_layer(graph, start_row, end_row, start_col, end_col):
    temp = graph[start_row][start_col]

    # 왼쪽 세로 줄 이동
    for i in range(start_col, end_col):
        graph[start_row][i] = graph[start_row][i + 1]
    #  아래쪽 가로 줄 이동
    for i in range(start_row, end_row):
        graph[i][end_col] = graph[i + 1][end_col]
    # 오른쪽 세로 줄 이동
    for i in range(end_col, start_col, -1):
        graph[end_row][i] = graph[end_row][i - 1]
    # 위쪽 가로 줄 이동
    for i in range(end_row, start_row, -1):
        graph[i][start_col] = graph[i - 1][start_col]

    graph[start_row + 1][start_col] = temp


def rotate_graph(graph, row, col, R):
    for _ in range(R):
        start_row, start_col = 0, 0
        end_row, end_col = row - 1, col - 1
        while start_row < end_row and start_col < end_col:
            rotate_layer(graph, start_row, end_row, start_col, end_col)
            start_row += 1
            start_col += 1
            end_row -= 1
            end_col -= 1


rotate_graph(graph, N, M, R)
for ans in graph:
    print(*ans)
