import sys

input = sys.stdin.readline

T = int(input())

_ps = []
for _ in range(T):
    a = input().rstrip()
    _ps.append(a)


for ps in _ps:
    stk = []
    for parenthesis in ps:
        if parenthesis == "(":
            stk.append(parenthesis)
        else:
            if stk and stk[-1] == "(":
                stk.pop()
            else:
                stk.append(parenthesis)

    if stk:
        print("NO")
    else:
        print("YES")
