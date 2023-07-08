import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = A+B
for i in sorted(ans):
    print(i, end=" ")
