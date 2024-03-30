import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = str(input().rstrip())


def IO(N):
    return "IO" * N + "I"


ans = 0

i = 0
while i < M:
    if S[i] == "O":
        i += 1
        continue
    else:
        if S[i : (2 * N + 1) + i] == IO(N):
            a = S[i : (2 * N + 1) + i]
            ans += 1
            i += 2
        else:
            i += 1

print(ans)
