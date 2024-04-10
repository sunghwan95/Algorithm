import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums_dict = defaultdict(int)
for num in nums:
    nums_dict[num] += 1

ans = [-1] * N

idx_stk = []
for i, num in enumerate(nums):
    while idx_stk and nums_dict[nums[idx_stk[-1]]] < nums_dict[num]:
        ans[idx_stk.pop()] = num

    idx_stk.append(i)

print(*ans)
