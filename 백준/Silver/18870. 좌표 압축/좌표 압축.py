"""
159260KB, 2004ms

0.수를 리스트로 받은 후 , 중복을 제거하고 정렬된 리스트를 새롭게 생성
1.해당 숫자가 정렬된 리스트에서 몇 번째 인덱스인지 해시맵을 이용하여 표시
2.다시 원래 배열을 순회하면서 해당 수가 몇 번째 인덱스인지만 알면 그 수보다 작은 수의 개수를 알 수 있음.
"""

import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

sorted_unique_nums = sorted(list(set(nums)))

nums_index = {}
for i, num in enumerate(sorted_unique_nums):
    nums_index[num] = i

ans = []
for num in nums:
    ans.append(nums_index[num])

print(*ans)
