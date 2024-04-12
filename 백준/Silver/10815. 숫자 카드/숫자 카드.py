import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

M = int(input())
check_nums = list(map(int, input().split()))


def binary_search(check_num):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if check_num == nums[mid]:
            print(1, end=" ")
            return
        elif check_num > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1

    print(0, end=" ")


for check_num in check_nums:
    binary_search(check_num)
