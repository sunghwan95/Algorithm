import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

ans = []


def backtracking(a):
    if len(ans) == M:
        print(*ans)
        return

    for i in range(a, N):
        ans.append(nums[i])
        backtracking(i)
        ans.pop()


backtracking(0)
