T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    graph = []
    for _ in range(N):
        a = list(map(int, input().split()))
        graph.append(a)

    prefixSum = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(N):
        for j in range(N):
            prefixSum[i + 1][j + 1] = (
                graph[i][j]
                + prefixSum[i + 1][j]
                + prefixSum[i][j + 1]
                - prefixSum[i][j]
            )

    ans = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            x1, y1 = i, j
            x2, y2 = i + M, j + M

            total = (
                prefixSum[x2][y2]
                - prefixSum[x1][y2]
                - prefixSum[x2][y1]
                + prefixSum[x1][y1]
            )

            ans = max(ans, total)

    print(f"#{tc} {ans}")