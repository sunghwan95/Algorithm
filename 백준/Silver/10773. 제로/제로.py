import sys

input = sys.stdin.readline

K = int(input())

stk = []
for _ in range(K):
    num = int(input())
    if num == 0:
        stk.pop()
    else:
        stk.append(num)

print(sum(stk))
