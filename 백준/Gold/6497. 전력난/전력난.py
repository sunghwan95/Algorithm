import sys

input = sys.stdin.readline


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


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    graph = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        graph.append((x, y, z))
    graph.sort(key=lambda x: x[2])

    parent = [i for i in range(m)]

    ans = 0
    for i in graph:
        a, b, cost = i
        if find_parent(a) != find_parent(b):
            union_parent(a, b)
        else:  # 연결되지 않은 가중치의 합을 정답으로...!
            ans += cost

    print(ans)
