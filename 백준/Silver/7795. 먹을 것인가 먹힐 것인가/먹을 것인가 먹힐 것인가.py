import sys
input = sys.stdin.readline

T = int(input())


def binarySearch(i, B):
    start = 0
    end = len(B)-1
    result = 0
    while start <= end:
        mid = (start+end) // 2
        if B[mid] < i:
            start = mid + 1
            result = mid
        else:
            end = mid-1
    return result + 1


for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    answer = 0
    for i in A:
        if i > B[0]:
            answer += binarySearch(i, B)
    print(answer)
