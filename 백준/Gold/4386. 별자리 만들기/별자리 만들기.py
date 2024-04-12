import sys
import math

input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    a, b = map(float, input().split())
    graph.append((a, b))

dist = []
for i in range(n - 1):
    for j in range(i + 1, n):
        dist.append(
            (
                (
                    math.sqrt(
                        (
                            (graph[i][0] - graph[j][0]) ** 2
                            + (graph[i][1] - graph[j][1]) ** 2
                        )
                    )
                ),
                i,
                j,
            )
        )

dist.sort()

parent = [0] * (n + 1)
for i in range(1, n + 1):
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
for i in dist:
    cost, a, b = i

    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        ans += cost

print(f"{ans:.2f}")
