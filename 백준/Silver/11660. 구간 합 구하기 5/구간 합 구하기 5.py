import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

prefixSum = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefixSum[i][j] = (
            graph[i - 1][j - 1]
            + prefixSum[i - 1][j]
            + prefixSum[i][j - 1]
            - prefixSum[i - 1][j - 1]
        )

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = (
        prefixSum[x2][y2]
        - prefixSum[x2][y1 - 1]
        - prefixSum[x1 - 1][y2]
        + prefixSum[x1 - 1][y1 - 1]
    )
    print(ans)
