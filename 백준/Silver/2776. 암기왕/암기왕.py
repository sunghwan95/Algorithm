import sys

input = sys.stdin.readline

T = int(input())


def binary_search(num, note_1):
    start = 0
    end = len(note_1) - 1

    while start <= end:
        mid = (start + end) // 2

        if note_1[mid] == num:
            print(1)
            return
        elif note_1[mid] > num:
            end = mid - 1
        else:
            start = mid + 1

    print(0)
    return


for _ in range(T):
    N = int(input())
    note_1 = list(map(int, input().split()))
    note_1.sort()

    M = int(input())
    note_2 = list(map(int, input().split()))

    for num in note_2:
        binary_search(num, note_1)
