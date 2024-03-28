import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = []


def dfs(a):
    if len(nums) == M:
        print(*nums)
        return

    for i in range(a, N + 1):
        if i not in nums:
            nums.append(i)
            dfs(i)
            nums.pop()


dfs(1)
