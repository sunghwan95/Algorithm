import sys

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
numsDict = dict()

for num in nums:
    if num not in numsDict:
        numsDict[num] = 1
    else:
        numsDict[num] += 1

M = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
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
            break
    if card == nums[mid]:
        print(numsDict[card], end=" ")
    else:
        print(0, end=" ")
