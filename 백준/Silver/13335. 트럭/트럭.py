import sys
from collections import deque

input = sys.stdin.readline

n, w, L = map(int, (input().split()))
trucks = deque(list(map(int, input().split())))
bridge = deque([0] * w)

moveCnt = 0
while bridge:
    bridge.popleft()
    moveCnt += 1

    if trucks:
        if sum(bridge) + trucks[0] <= L:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)


print(moveCnt)
