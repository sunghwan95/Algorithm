import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

V, E = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(E)]
graph.sort(key=lambda x: x[2])

parent = [0] * (V + 1)
for i in range(1, V + 1):
    parent[i] = i


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


ans = 0
for i in range(E):
    node, edge, cost = graph[i]

    if find(node) != find(edge):
        union(node, edge)
        ans += cost

print(ans)
