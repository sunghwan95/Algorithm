N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

ans = []


def dfs():
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return

    for i in range(0, N):
        ans.append(nums[i])
        dfs()
        ans.pop()


dfs()
