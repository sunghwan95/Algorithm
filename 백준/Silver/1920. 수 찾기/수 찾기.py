import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

arr.sort()


def binary(target):
    start_index = 0
    end_index = N-1

    while start_index <= end_index:
        mid_index = (start_index+end_index)//2

        if arr[mid_index] == target:
            return True
        if target < arr[mid_index]:
            end_index = mid_index-1
        elif arr[mid_index] < target :
            start_index = mid_index+1
        else:
            return False


for i in range(M):
    if binary(nums[i]):
        print(1)
    else:
        print(0)
