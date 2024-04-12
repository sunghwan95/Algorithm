import sys

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

M = int(sys.stdin.readline())

cards = list(map(int, sys.stdin.readline().split()))
answer = []
for card in cards:
    start = 0
    end = N-1
    while start <= end:
        mid = (start+end)//2
        if card > nums[mid]:
            start = mid+1
        elif card < nums[mid]:
            end = mid-1
        else:
            answer.append(1)
            break

    if nums[mid] != card:
        answer.append(0)


print(" ".join(map(str, answer)))
