import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

nums = deque([])
for _ in range(N):
    a = input().split()

    cmd = a[0]
    if cmd == "push":
        nums.append(a[1])
    elif cmd == "pop":
        if nums:
            print(nums.popleft())
        else:
            print(-1)
    elif cmd == "size":
        print(len(nums))
    elif cmd == "empty":
        if nums:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if nums:
            print(nums[0])
        else:
            print(-1)
    else:
        if nums:
            print(nums[-1])
        else:
            print(-1)
