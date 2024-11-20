import sys

input = sys.stdin.readline

N = int(input())
given = list(map(int, input().split()))

M = int(input())
check = list(map(int, input().split()))

given.sort()


def bst(target):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if target == given[mid]:
            return True
        elif target < given[mid]:
            end = mid - 1
        elif target > given[mid]:
            start = mid + 1

    return False


for i in check:
    if bst(i):
        print(1)
    else:
        print(0)
