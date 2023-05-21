import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()
visited = [0]*N

res = []


def dfs(x):
    prev_dupl = 0
    if len(res) == M:
        print(" ".join(map(str, res)))
        return
    for i in range(x, N):
        if visited[i] == 0 and prev_dupl != nums[i]:
            visited[i] = 1
            prev_dupl = nums[i]
            res.append(nums[i])
            dfs(i)
            visited[i] = 0
            res.pop()


dfs(0)
