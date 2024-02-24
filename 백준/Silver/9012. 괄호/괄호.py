import sys

input = sys.stdin.readline

T = int(input())

ans = []
for _ in range(T):
    stk = []
    strings = input().rstrip()

    for string in strings:
        if string == "(":
            stk.append(string)
        else:
            if stk:
                stk.pop()
            else:
                stk.append(string)
                break

    if len(stk) == 0:
        ans.append("YES")
    else:
        ans.append("NO")

print(*ans, sep="\n")
