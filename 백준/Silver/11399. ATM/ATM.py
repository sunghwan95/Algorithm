import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

nums.sort()
answer = 0

for i in range(1, N + 1):
    answer += sum(nums[0:i])
print(answer)
