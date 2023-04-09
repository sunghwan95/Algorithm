N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

ans = []


def dfs(x):
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return

    for i in range(x, N):
        if nums[i] not in ans:
            ans.append(nums[i])
            dfs(i)
            ans.pop()


dfs(0)
