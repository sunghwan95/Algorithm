import sys

input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    a = list(input().rstrip())
    graph.append(a)


def count_ans(graph):
    ans = 0
    for row in graph:
        count = 0
        for cell in row:
            if cell == ".":
                count += 1
            else:
                if count >= 2:
                    ans += 1
                count = 0
        if count >= 2:
            ans += 1

    return ans


def transpose(graph):
    transposed_graph = []
    for i in range(N):
        transposed_row = []
        for j in range(N):
            transposed_row.append(graph[j][i])
        transposed_graph.append(transposed_row)

    return transposed_graph


ans_row = count_ans(graph)

transposed_graph = transpose(graph)
ans_col = count_ans(transposed_graph)

print(ans_row, ans_col, end=" ")
