import sys

input = sys.stdin.readline

N = int(input())

squares = {}
idxs = []
for _ in range(N):
    idx, height = map(int, input().split())
    idxs.append(idx)
    squares[idx] = height

idxs.sort()

stk = []
for idx in idxs:
    if not stk:
        stk.append((idx, squares[idx]))
        continue

    while True:
        if len(stk) >= 2 and stk[-2][1] >= stk[-1][1] and stk[-1][1] <= squares[idx]:
            stk.pop()
            continue
        else:
            stk.append((idx, squares[idx]))
            break

ans = 0
for i in range(len(stk) - 1):
    if stk[i][1] < stk[i + 1][1]:
        ans += (stk[i + 1][0] - stk[i][0]) * (stk[i][1])
    else:
        ans += (stk[i + 1][0] - stk[i][0]) * (stk[i + 1][1])

ans += max(squares.values())

print(ans)
