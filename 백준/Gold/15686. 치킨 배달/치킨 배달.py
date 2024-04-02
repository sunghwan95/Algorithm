import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[0] * N for _ in range(N)]
min_chicken_distance = sys.maxsize

houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append((i, j))
        elif graph[i][j] == 2:
            chickens.append((i, j))


distances = [[0] * len(chickens) for _ in range(len(houses))]
for i, house in enumerate(houses):
    for j, chicken in enumerate(chickens):
        distances[i][j] = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])


def dfs(idx, selected_chickens):
    global min_chicken_distance

    if len(selected_chickens) == M:
        total_distance = 0
        for i in range(len(houses)):
            min_distance = sys.maxsize
            for chicken_idx in selected_chickens:
                min_distance = min(min_distance, distances[i][chicken_idx])
            total_distance += min_distance
        min_chicken_distance = min(min_chicken_distance, total_distance)
        return

    if idx == len(chickens):
        return

    dfs(idx + 1, selected_chickens + [idx])
    dfs(idx + 1, selected_chickens)


dfs(0, [])
print(min_chicken_distance)
