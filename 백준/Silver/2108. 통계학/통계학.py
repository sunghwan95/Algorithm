import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]


def get_mean(nums):
    print(round(sum(nums) / N))


def get_median(nums):
    nums.sort()
    print(nums[len(nums) // 2])


def get_mode(nums):
    if len(nums) == 1:
        print(nums[0])
        return

    nums_dict = defaultdict(int)
    for num in nums:
        nums_dict[num] += 1

    # 빈도수는 내림차순, 최빈값은 오름차순
    sorted_nums_dict = sorted(nums_dict.items(), key=lambda x: (-x[1], x[0]))

    if sorted_nums_dict[0][1] == sorted_nums_dict[1][1]:
        print(sorted_nums_dict[1][0])
    else:
        print(sorted_nums_dict[0][0])


def get_range(nums):
    max_val = max(nums)
    min_val = min(nums)
    print(max_val - min_val)


get_mean(nums)
get_median(nums)
get_mode(nums)
get_range(nums)
