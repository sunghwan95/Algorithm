import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())
count = 0
for i in range(N):
    arr[i] -= B
    count += 1
    if arr[i] > 0:
        if arr[i] % C == 0:
            count += arr[i]//C
        else:
            count += arr[i]//C+1

print(count)
