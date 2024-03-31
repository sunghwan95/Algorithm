import sys

input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    a = list(map(str, input().rstrip()))
    graph.append(a)

ans_width = 0
for i in range(N):
    width = 1
    for j in range(N):
        if graph[i][j] == "." and (j + 1 < N) and graph[i][j + 1] == ".":
            width += 1
        elif (j + 1 < N) and graph[i][j + 1] == "X":
            if width >= 2:
                ans_width += 1
                width = 1
                continue
            else:
                width = 1
                continue
    if width >= 2:
        ans_width += 1

ans_length = 0
for j in range(N):
    length = 1
    for i in range(N):
        if graph[i][j] == "." and (i + 1 < N) and graph[i + 1][j] == ".":
            length += 1
        elif (i + 1 < N) and graph[i + 1][j] == "X":
            if length >= 2:
                ans_length += 1
                length = 1
                continue
            else:
                length = 1
                continue
    if length >= 2:
        ans_length += 1

print(ans_width, ans_length, end=" ")
