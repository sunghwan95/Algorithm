import sys
input = sys.stdin.readline

V, E = map(int, input().split())
E_arr = []
for _ in range(E):
    E_arr.append(list(map(int, input().split())))

E_arr.sort(key=lambda x: x[2])

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
        parent[b] = a
    else:
        parent[a] = b


answer = 0
for a, b, c in E_arr:
    if find(a) != find(b):
        union(a, b)
        answer += c

print(answer)
