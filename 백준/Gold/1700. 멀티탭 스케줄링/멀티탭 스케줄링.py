import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
plugs = []


count = 0
for i, num in enumerate(nums):
    if num in plugs:
        continue
    if len(plugs) < N:
        plugs.append(num)
        continue
    else:
        temp = []
        for j in range(N):
            try:
                idx = nums[i:].index(plugs[j])
            except ValueError:
                idx = 101
            temp.append(idx)
        select = temp.index(max(temp))
        plugs[select] = nums[i]
        count += 1

print(count)
