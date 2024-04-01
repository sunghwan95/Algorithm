import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
operations = list(map(int, input().split()))


def flip_up_down(graph):
    return graph[::-1]


def flip_left_right(graph):
    return [row[::-1] for row in graph]


def rotate_clockwise(graph, op):
    rotated_graph = [[0] * N for _ in range(M)]

    if op == 3:
        for i in range(N):
            for j in range(M):
                rotated_graph[j][N - i - 1] = graph[i][j]
    else:
        for i in range(N):
            for j in range(M):
                rotated_graph[M - j - 1][i] = graph[i][j]

    return rotated_graph


def move_groups(graph, op, N, M):
    # 1번그룹, 2번그룹, 3번그룹, 4번그룹 순
    if op == 5:
        idx_groups = [(0, 0), (0, M // 2), (N // 2, M // 2), (N // 2, 0)]
    # 1번그럽, 4번그룹, 3번그룹, 2번그룹 순
    else:
        idx_groups = [(0, 0), (N // 2, 0), (N // 2, M // 2), (0, M // 2)]

    new_graph = [[0] * M for _ in range(N)]
    for i in range(4):
        x, y = idx_groups[(i + 1) % 4]
        dx, dy = idx_groups[i]
        for r in range(N // 2):
            for c in range(M // 2):
                new_graph[x + r][y + c] = graph[dx + r][dy + c]

    return new_graph


for op in operations:
    if op == 1:
        graph = flip_up_down(graph)
    elif op == 2:
        graph = flip_left_right(graph)
    elif op == 3 or op == 4:
        graph = rotate_clockwise(graph, op)
        N, M = M, N
    elif op == 5 or op == 6:
        graph = move_groups(graph, op, N, M)

for ans in graph:
    print(*ans)
