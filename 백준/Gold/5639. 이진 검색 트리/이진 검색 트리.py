import sys
sys.setrecursionlimit(10**6)
nums = []

while True:
    try:
        num = int(input())
        nums.append(num)
    except:
        break


def binary_search_tree(arr):
    sub_left = []
    sub_right = []
    if arr:
        root = arr.pop(0)
        for node in arr:
            if node < root:
                sub_left.append(node)
            else:
                sub_right.append(node)
        binary_search_tree(sub_left)
        binary_search_tree(sub_right)
        print(root)
    else:
        return


binary_search_tree(nums)
