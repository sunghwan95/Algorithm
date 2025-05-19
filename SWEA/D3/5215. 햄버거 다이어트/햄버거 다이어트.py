T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())

    arr = [tuple(map(int, input().split())) for _ in range(N)]

    dp = [[0] * (L + 1) for _ in range(N + 1)]
    # dp[i][j] = i번째 재료까지 고려했을 떄, j칼로리에서의 최대 점수

    for i, (score, kcal) in enumerate(arr):
        for j in range(L + 1):
            dp[i + 1][j] = dp[i][j]

            if kcal <= j:
                dp[i + 1][j] = max(dp[i][j], score + dp[i][j - kcal])

    print(f"#{tc} {max(dp[N])}")
