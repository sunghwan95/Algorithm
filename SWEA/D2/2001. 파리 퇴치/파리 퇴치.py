T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    pSum = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            pSum[i][j] = (
                graph[i - 1][j - 1]
                + pSum[i][j - 1]
                + pSum[i - 1][j]
                - pSum[i - 1][j - 1]
            )

    ans = 0
    for i in range(1, N - M + 2):
        for j in range(1, N - M + 2):
            total = (
                pSum[i + M - 1][j + M - 1]
                - pSum[i + M - 1][j - 1]
                - pSum[i - 1][j + M - 1]
                + pSum[i - 1][j - 1]
            )
            ans = max(ans, total)

    print(f"#{tc} {ans}")
