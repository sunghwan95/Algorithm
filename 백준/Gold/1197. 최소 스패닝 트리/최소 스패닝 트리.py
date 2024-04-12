import sys

input = sys.stdin.readline

V, E = map(int, input().split())

graph = []
for _ in range(E):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))
graph = sorted(graph, key=lambda x: x[2])

parent = [0] * (V + 1)
for i in range(1, V + 1):
    parent[i] = i


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
for i in range(E):
    a, b, cost = graph[i]

    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ans += cost

print(ans)
