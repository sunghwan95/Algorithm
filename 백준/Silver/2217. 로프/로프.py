import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    a = int(input())
    arr.append(a)

arr.sort(reverse=True)
result = []
for i in range(N):
    result.append(arr[i]*(i+1))

print(max(result))
