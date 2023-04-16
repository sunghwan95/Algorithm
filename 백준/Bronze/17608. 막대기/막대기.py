import sys

N = int(sys.stdin.readline())

stk = []
for _ in range(N):
    h = int(sys.stdin.readline())
    stk.append(h)

count = 1

for i in range(len(stk)-1, -1, -1):
    if stk[i] > stk[-1]:
        count += 1
        stk[-1] = stk[i]


print(count)
