import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

sorted_unique_nums = sorted(list(set(nums)))

nums_index = defaultdict(int)
for i, num in enumerate(sorted_unique_nums):
    nums_index[num] = i

compressed_nums = []
for num in nums:
    compressed_nums.append(nums_index[num])

print(*compressed_nums)
