import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = str(input().rstrip())


ans = 0

i = 0
cnt = 0
while i < M:
    if S[i : i + 3] == "IOI":
        cnt += 1
        i += 2
        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        cnt = 0
        i += 1
print(ans)
