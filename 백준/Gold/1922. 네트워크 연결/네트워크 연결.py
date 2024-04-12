import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = []
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))
graph = sorted(graph, key=lambda x: x[2])

parent = [0] * (N + 1)
for i in range(1, N + 1):
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
for i in graph:
    a, b, cost = i
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ans += cost

print(ans)
