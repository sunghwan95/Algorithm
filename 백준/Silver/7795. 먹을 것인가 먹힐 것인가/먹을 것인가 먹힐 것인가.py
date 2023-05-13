import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    idx = 0
    res = 0
    for i in A:
        while idx < M:
            if i > B[idx]:
                idx += 1
            else:
                break
        res += idx
    print(res)
