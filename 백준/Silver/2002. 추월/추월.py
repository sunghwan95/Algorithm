import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

queue = deque()

ans = 0
for i in range(N * 2):
    if i < N:
        enter_car = str(input().rstrip())
        queue.append(enter_car)
    else:
        exit_car = str(input().rstrip())
        if queue[0] != exit_car:
            ans += 1
            del queue[queue.index(exit_car)]
        else:
            queue.popleft()

print(ans)
