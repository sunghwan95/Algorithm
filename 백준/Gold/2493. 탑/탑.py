import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

stk = []
ans = [0] * len(nums)
for idx, num in enumerate(nums):
    while stk and stk[-1][1] < num:
        stk.pop()

    if stk:
        ans[idx] = stk[-1][0] + 1

    stk.append((idx, num))

print(*ans)
