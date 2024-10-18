import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

nums = []
for i in range(1, N + 1):
    nums.append(i)

nums_q = deque(nums)

while len(nums_q) > 1:
    nums_q.popleft()
    nums_q.append(nums_q.popleft())

print(nums_q[0])
