import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
answer = [nums[0]]

# answer와 새로 들어갈 숫자를 인자로 받아서
# 어느 인덱스에 끼워넣을지 판단하는 함수.
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
    # 새로 들어갈 숫자가 answer의 마지막 요소보다 크다면
    if num > answer[-1]:
        # answers에 숫자 추가.
        answer.append(num)
    # 새로 들어갈 숫자가 answer의 마지막 요소보다 작거나 같다면
    else:
        # answer의 어느 인덱스에 들어가야 할 지 판단.
        answer[binary(answer, num)] = num

print(len(answer))
