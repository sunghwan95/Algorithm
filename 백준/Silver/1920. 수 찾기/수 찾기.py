import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

M = int(input())
check_nums = list(map(int, input().split()))

nums.sort()


def binary_search(target):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return False


for check_num in check_nums:
    if binary_search(check_num):
        print(1)
    else:
        print(0)
