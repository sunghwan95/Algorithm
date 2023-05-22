import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)
B = []
for _ in range(N):
    b = list(map(int, input().split()))
    B.append(b)

ans = []
for i in range(N):
    temp = []
    for j in range(M):
        temp.append(A[i][j]+B[i][j])
    ans.append(temp)

for k in ans:
    for l in k:
        print(l, end=" ")
    print()
