import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        a = list(map(int, input().split()))
        arr.append(a)
    arr = sorted(arr, key=lambda x: x[0])

    i = 0
    ans = 1
    for j in range(i, N):
        if arr[j][1] < arr[i][1]:
            i = j
            ans += 1

    print(ans)
