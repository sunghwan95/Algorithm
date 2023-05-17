import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

res = []


def dfs(x):
    prev_dupl = 0
    if len(res) == M:
        print(" ".join(map(str, res)))
        return
    for i in range(x, N):
        if prev_dupl != nums[i]:
            res.append(nums[i])
            dfs(i)
            prev_dupl = nums[i]
            res.pop()


dfs(0)
