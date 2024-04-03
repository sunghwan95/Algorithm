import sys

input = sys.stdin.readline

A = int(input())
nums = list(map(int, input().split()))

idx_stk = []
ans = [-1] * A

for i, num in enumerate(nums):
    while idx_stk and nums[idx_stk[-1]] < num:
        ans[idx_stk.pop()] = num
    idx_stk.append(i)

print(*ans)
