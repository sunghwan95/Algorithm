import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [0]
for _ in range(N):
    a, b = map(int, input().split())
    graph.append((a, b))

edges = []
for i in range(1, len(graph) - 1):
    for j in range(i + 1, len(graph)):
        distance = math.sqrt(
            (graph[i][0] - graph[j][0]) ** 2 + (graph[i][1] - graph[j][1]) ** 2
        )
        edges.append((i, j, distance))

edges.sort(key=lambda x: x[2])
parent = [i for i in range(N + 1)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(M):
    a, b = map(int, input().split())
    union_parent(a, b)

ans = 0
for i in edges:
    x, y, cost = i
    if find_parent(x) != find_parent(y):
        union_parent(x, y)
        ans += cost

print(f"{ans:.2f}")
