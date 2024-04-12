import sys

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

ans = []
stk = []

now_num = 1
for num in nums:
    if stk and stk[-1] == num:
        ans.append("-")
        stk.pop()
        continue

    for i in range(now_num, n + 1):
        stk.append(i)
        ans.append("+")
        if i == num:
            stk.pop()
            ans.append("-")
            now_num = i + 1
            break

if stk:
    print("NO")
else:
    print(*ans, sep="\n")
