import sys

input = sys.stdin.readline

T = int(input())

arr_ps = []
for _ in range(T):
    ps = input().rstrip()
    arr_ps.append(ps)

for ps in arr_ps:
    stk = []

    for string in ps:
        if string == "(":
            stk.append(string)
        else:
            if stk and stk[-1] == "(":
                stk.pop()
            else:
                stk.append(string)

    if stk:
        print("NO")
    else:
        print("YES")
