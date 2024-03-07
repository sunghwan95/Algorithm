import sys

input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    _list = list(map(int, input().split()))
    graph.append(_list)
visited = [0 for _ in range(N)]
res = sys.maxsize


def dfs(teamMembers, indexOfVisited):
    global res
    if teamMembers == N // 2:
        startTeam = 0
        linkTeam = 0

        for x in range(N):
            for y in range(x, N):
                if visited[x] == 1 and visited[y] == 1:
                    startTeam += graph[x][y] + graph[y][x]
                elif visited[x] == 0 and visited[y] == 0:
                    linkTeam += graph[x][y] + graph[y][x]

        res = min(res, abs(startTeam - linkTeam))

        if res == 0:
            print(res)
            exit(0)

        return

    for i in range(indexOfVisited, N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(teamMembers + 1, i + 1)
            visited[i] = 0


dfs(0, 0)
print(res)
