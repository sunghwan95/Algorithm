import sys
from collections import deque

N = int(sys.stdin.readline())
nums = deque([])

for i in range(1, N+1):
    nums.append(i)

while True:
    if len(nums) == 1:
        print(nums[0])
        break
    else:
        nums.popleft()
        nums.append(nums.popleft())
