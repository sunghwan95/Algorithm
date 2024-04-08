import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for arr in graph:
    arr.sort()

visited = [0] * (N + 1)
ans = [0] * N
count = 1


def bfs(R):
    global count
    queue = deque()
    queue.append(R)
    visited[R] = 1

    while queue:
        node = queue.popleft()
        ans[node - 1] = count
        count += 1

        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)


bfs(R)
print(*ans, sep="\n")
