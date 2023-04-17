import sys
from collections import deque

N = int(sys.stdin.readline())
arr = deque([])

for _ in range(N):
    string = list(map(str, sys.stdin.readline().split()))

    if string[0] == "push":
        arr.append(string[1])

    elif string[0] == "pop":
        if not arr:
            print(-1)
        else:
            print(arr.popleft())

    elif string[0] == "size":
        print(len(arr))

    elif string[0] == "empty":
        if not arr:
            print(1)
        else:
            print(0)

    elif string[0] == "front":
        if not arr:
            print(-1)
        else:
            print(arr[0])

    elif string[0] == "back":
        if not arr:
            print(-1)
        else:
            print(arr[-1])
