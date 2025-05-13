T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ans = []

    for i in range(N):
        if i == 0:
            ans.append([1])
        else:
            prev = ans[-1]
            row = [1]
            for j in range(1, len(prev)):
                row.append(prev[j - 1] + prev[j])
            row.append(1)
            ans.append(row)

    print(f"#{tc}")
    for row in ans:
        print(*row)