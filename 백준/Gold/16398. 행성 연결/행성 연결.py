import sys

input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    a = list(map(int, input().split()))
    graph.append(a)

edges = []
for i in range(len(graph)):
    for j in range(i + 1, len(graph[i])):
        cost = graph[i][j]
        edges.append((cost, i, j))
edges.sort(key=lambda x: x[0])

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


ans = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ans += cost

print(ans)
