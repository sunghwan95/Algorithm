import sys
N, K = map(int, sys.stdin.readline().split())

nums = list(map(str, sys.stdin.readline()))
nums.pop()

stk = []
count = 0
for num in nums:
    while stk and count != K and stk[-1] < num:
        stk.pop()
        count += 1

    if stk and count != K:
        stk.append(num)
    else:
        stk.append(num)

if len(stk) > N-K:
    stk = stk[:N-K]


print("".join(stk))
