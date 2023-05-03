import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
answer = 0

for x in range(1, N+1):
    answer += sum(arr[0:x])
print(answer)
