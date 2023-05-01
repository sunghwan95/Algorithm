import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    a = list(map(int, input().split()))
    graph.append(a)
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1, N):
    for j in range(N-i):
        x = j+i
        dp[j][x] = 2**31-1
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k]+dp[k+1][x] +
                           graph[j][0]*graph[k][1]*graph[x][1])

print(dp[0][N-1])
