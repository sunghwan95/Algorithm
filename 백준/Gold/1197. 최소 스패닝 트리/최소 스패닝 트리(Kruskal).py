# kruskal

import sys
input = sys.stdin.readline

V, E = map(int, input().split())
edges = []
for _ in range(E):
    edges.append(list(map(int, input().split())))
edges.sort(key=lambda x: x[2])

parent = [0]*(V+1)
for i in range(V+1):
    parent[i] = i


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = find(a)
    else:
        parent[a] = find(b)


answer = 0
for current, _next, weight in edges:
    if find(current) != find(_next):
        union(current, _next)
        answer += weight

print(answer)
