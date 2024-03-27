import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    R, S = input().split()
    ans = ""
    for i in S:
        ans += int(R) * i
    print(ans)
