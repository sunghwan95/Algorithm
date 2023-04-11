N = int(input())

visited = [0]*N
city = []
answer = 1e9


for _ in range(N):
    a = list(map(int, input().split()))
    city.append(a)


def dfs(x, start, cost):
    global answer
    if (x == N-1) and (city[start][0] != 0):
        answer = min(answer, cost+city[start][0])
        return
    for i in range(N):
        if (visited[i] == 0) and (city[start][i] != 0):
            visited[i] = 1
            dfs(x+1, i, cost+city[start][i])
            visited[i] = 0


visited[0] = 1
dfs(0, 0, 0)
print(answer)
