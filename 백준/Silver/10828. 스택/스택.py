import sys

input = sys.stdin.readline

N = int(input())

stk = []
for _ in range(N):
    a = input().split()
    cmd = a[0]

    if cmd == "push":
        num = int(a[1])
        stk.append(num)

    elif cmd == "pop":
        if stk:
            print(stk.pop())
        else:
            print(-1)

    elif cmd == "size":
        print(len(stk))

    elif cmd == "empty":
        if stk:
            print(0)
        else:
            print(1)

    elif cmd == "top":
        if stk:
            print(stk[-1])
        else:
            print(-1)
