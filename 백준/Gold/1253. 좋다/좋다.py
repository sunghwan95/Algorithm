import sys
N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))


nums.sort()
count = 0

for i in range(len(nums)):
    target = nums[i]
    new_nums = nums[:i]+nums[i+1:]
    start = 0
    end = len(new_nums)-1
    while start < end:
        add_num = new_nums[start]+new_nums[end]
        if target == add_num:
            count += 1
            break
        elif target < add_num:
            end -= 1
        else:
            start += 1
print(count)
