import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

res = []


def bfs(startingNode):
    queue = []
    queue.append(startingNode)
    visited[startingNode] = 1

    while queue:
        visitedNode = queue.pop(0)

        for visitingNode in range(1, N + 1):
            if graph[visitedNode][visitingNode] == 1 and visited[visitingNode] == 0:
                visited[visitingNode] = 1
                queue.append(visitingNode)
                res.append(visitingNode)


bfs(1)
print(len(res))
