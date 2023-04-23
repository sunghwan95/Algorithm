import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x):
    global isBipartite
    for i in graph[x]:
        if visited[i][0] == 0:
            if visited[x][1] == 1:
                visited[i][0] = 1
                visited[i][1] = -1
            if visited[x][1] == -1:
                visited[i][0] = 1
                visited[i][1] = 1
            dfs(i)
        else:
            if visited[x][1] == visited[i][1]:
                isBipartite = False
                return


K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    visited = [[0, 0] for _ in range(a+1)]
    graph = [[] for _ in range(a+1)]
    for _ in range(b):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    isBipartite = True
    for i in range(1, a+1):
        if visited[i][0] == 0:
            visited[i][0] = 1
            visited[i][1] = 1
            dfs(i)
            if isBipartite == False:
                break

    if isBipartite == False:
        print("NO")
    else:
        print("YES")
