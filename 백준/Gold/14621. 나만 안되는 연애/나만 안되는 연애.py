import sys

input = sys.stdin.readline

N, M = map(int, input().split())

univs = [0] + list(map(str, input().split()))

edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
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
linked = 0
for edge in edges:
    cost, a, b = edge
    if univs[a] != univs[b]:
        if find_parent(a) != find_parent(b):
            union_parent(a, b)
            ans += cost
            linked += 1

if linked == N - 1:
    print(ans)
else:
    print(-1)
