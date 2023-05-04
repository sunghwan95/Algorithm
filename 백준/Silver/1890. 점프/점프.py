import sys
input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    a = list(map(int, input().split()))
    graph.append(a)

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1


for i in range(N):
    for j in range(N):
        if graph[i][j] != 0 and dp[i][j] != 0:
            right = j+graph[i][j]
            down = i+graph[i][j]
            if down < N:
                dp[down][j] += dp[i][j]
            if right < N:
                dp[i][right] += dp[i][j]

print(dp[-1][-1])
