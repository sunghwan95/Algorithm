import sys
N = int(sys.stdin.readline())

stk = []
for _ in range(N):
    arr = list(map(str, sys.stdin.readline().split()))
    if arr[0] == "push":
        stk.append(arr[1])
    elif arr[0] == "top":
        try:
            print(stk[-1])
        except IndexError:
            print(-1)
            continue
    elif arr[0] == "size":
        print(len(stk))
    elif arr[0] == "pop":
        try:
            print(stk.pop())
        except IndexError:
            print(-1)
            continue
    elif arr[0] == "empty":
        if len(stk) == 0:
            print(1)
        else:
            print(0)
