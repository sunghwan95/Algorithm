import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited_DFS = [0] * (N + 1)
visited_BFS = [0] * (N + 1)


def dfs(start):
    visited_DFS[start] = 1
    print(start, end=" ")

    for i in range(1, N + 1):
        if graph[start][i] == 1 and visited_DFS[i] == 0:
            dfs(i)


def bfs(start):
    queue = deque([])
    queue.append(start)

    while queue:
        _start = queue.popleft()
        visited_BFS[_start] = 1
        print(_start, end=" ")

        for i in range(1, N + 1):
            if graph[_start][i] == 1 and visited_BFS[i] == 0:
                visited_BFS[i] = 1
                queue.append(i)


dfs(V)
print()
bfs(V)
