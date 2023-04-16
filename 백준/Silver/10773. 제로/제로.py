import sys
K = int(sys.stdin.readline())

stk = []
for _ in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        stk.pop()
    else:
        stk.append(num)

print(sum(stk))
