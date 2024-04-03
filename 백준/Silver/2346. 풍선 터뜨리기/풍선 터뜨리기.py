import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
balloons = list(map(int, input().split()))

queue = deque([(idx + 1, balloons[idx]) for idx in range(N)])

while queue:
    idx, num = queue.popleft()
    print(idx, end=" ")
    if not queue:
        break

    if num > 0:
        num -= 1

    for _ in range(abs(num)):
        if num > 0:
            queue.append(queue.popleft())
        else:
            queue.appendleft(queue.pop())
