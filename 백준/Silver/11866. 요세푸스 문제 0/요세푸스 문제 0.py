import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

nums = deque([])
for i in range(1, N + 1):
    nums.append(f"{i}")

ans = []
while nums:
    for i in range(1, K + 1):
        if i == K:
            ans.append(nums.popleft())
            break

        nums.append(nums.popleft())

print("<" + ", ".join(ans) + ">")
