N, M = map(int, input().split())
nums = list(map(int, input().split()))


nums.sort()

ans = []
visited = [0]*N
prev_dupl = 0


def dfs(x):
    prev_dupl = 0
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return

    for i in range(0, N):
        if visited[i] == 0 and nums[i] != prev_dupl:
            ans.append(nums[i])
            prev_dupl = nums[i]
            visited[i] = 1
            dfs(x+1)
            ans.pop()
            visited[i] = 0


dfs(0)
