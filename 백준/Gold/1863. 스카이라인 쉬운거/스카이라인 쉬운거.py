import sys

input = sys.stdin.readline

n = int(input())
skylines = []
for _ in range(n):
    x, y = map(int, input().split())
    skylines.append(y)
skylines.append(0)

ans = 0

stk = [0]
for y in skylines:
    height = y
    while stk[-1] > y:
        if stk[-1] != height:
            height = stk[-1]
            ans += 1
        stk.pop()

    stk.append(y)

print(ans)
