import sys

input = sys.stdin.readline

n = int(input())

nums = []
for _ in range(n):
    a = int(input())
    nums.append(a)

stk = []
ans = []

now = 1
for num in nums:
    if stk and stk[-1] == num:
        stk.pop()
        ans.append("-")
        continue

    for i in range(now, n + 1):
        stk.append(i)
        ans.append("+")
        if i == num:
            stk.pop()
            ans.append("-")
            now = i + 1
            break

if stk:
    print("NO")
else:
    print(*ans, sep="\n")
