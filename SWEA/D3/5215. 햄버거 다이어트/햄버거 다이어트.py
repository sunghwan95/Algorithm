def dfs(idx, total_grades, total_kcal):
    global ans

    if total_kcal > L:
        return

    ans = max(ans, total_grades)

    for i in range(idx, len(ingredients)):
        grade, kcal = ingredients[i]
        dfs(i + 1, total_grades + grade, total_kcal + kcal)


T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())
    ingredients = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    dfs(0, 0, 0)
    print(f"#{tc} {ans}")