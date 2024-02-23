import sys
from collections import deque

input = sys.stdin.readline()

N, K = map(int, (input.split()))
queue = deque(list(range(1, N + 1)))

ans = []

temp = 1
while len(queue) >= 1:
    if temp != K:
        queue.append(queue.popleft())
        temp += 1
    else:
        ans.append(queue.popleft())
        temp = 1

res = ans + list(queue)

print("<" + ", ".join(map(str, res)) + ">")
