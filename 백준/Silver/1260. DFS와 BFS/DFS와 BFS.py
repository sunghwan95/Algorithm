import sys

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
visitedDFS = [0 for _ in range(N + 1)]
visitedBFS = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


def dfs(v):
    visitedDFS[v] = 1
    print(v, end=" ")

    for i in range(1, N + 1):
        if graph[v][i] == 1 and visitedDFS[i] == 0:
            dfs(i)


def bfs(v):
    queue = []
    queue.append(v)
    visitedBFS[v] = 1

    while queue:
        visitedNode = queue.pop(0)

        print(visitedNode, end=" ")
        for visitingNode in range(1, N + 1):
            if graph[visitedNode][visitingNode] == 1 and visitedBFS[visitingNode] == 0:
                visitedBFS[visitingNode] = 1
                queue.append(visitingNode)


dfs(V)
print()
bfs(V)
