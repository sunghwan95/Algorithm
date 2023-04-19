import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
answer = [nums[0]]


def binary(answer, num):
    start = 0
    end = len(answer)-1
    while start <= end:
        mid = (start+end)//2
        if num < answer[mid]:
            end = mid-1
        elif num > answer[mid]:
            start = mid+1
        else:
            return mid
    return end+1


for num in nums:
    if num > answer[-1]:
        answer.append(num)
    else:
        answer[binary(answer, num)] = num

print(len(answer))
