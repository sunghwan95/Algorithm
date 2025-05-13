T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    ans = [[1], [1, 1]]

    if N >= 3:
        for i in range(3, N + 1):
            a = []
            for j in range(0, N):
                if j == 0:
                    a.append(1)
                    continue
                elif len(a) == i - 1:
                    a.append(1)
                    break
                else:
                    k = 0
                    nums = ans[i - 2]
                    while True:
                        if k == len(nums) - 1:
                            break
                        a.append(sum(nums[k : k + 2]))
                        k += 1

            ans.append(a)

    print(f"#{tc}")
    for a in ans:
        print(*a)
