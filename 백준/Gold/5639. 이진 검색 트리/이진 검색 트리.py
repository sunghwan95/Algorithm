import sys
sys.setrecursionlimit(10**6)
nums = []

while True:
    try:
        num = int(input())
        nums.append(num)
    except:
        break


def divide_tree(arr):
    left_side = []
    right_side = []
    if arr:
        parent = arr.pop(0)
        for num in arr:
            if num < parent:
                left_side.append(num)
            else:
                right_side.append(num)
        divide_tree(left_side)
        divide_tree(right_side)
        print(parent)
    else:
        return


divide_tree(nums)
