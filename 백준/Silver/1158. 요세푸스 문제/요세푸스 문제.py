import sys
from collections import deque

input = sys.stdin.readline()

N, K = map(int, (input.split()))
queue = list(range(1, N + 1))

ans = []

i = 0
while queue:
    i = (i + K - 1) % len(queue)
    ans.append(queue.pop(i))

print("<" + ", ".join(map(str, ans)) + ">")
