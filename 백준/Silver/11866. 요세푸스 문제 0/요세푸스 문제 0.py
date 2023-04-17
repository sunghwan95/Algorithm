import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
nums = deque()
answer = []

for i in range(1, N+1):
    nums.append(i)

while nums:
    for i in range(K-1):
        nums.append(nums.popleft())
    answer.append(nums.popleft())

print("<"+", ".join(map(str, answer))+">")
