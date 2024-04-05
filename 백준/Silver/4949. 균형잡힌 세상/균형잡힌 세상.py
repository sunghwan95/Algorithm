import sys

input = sys.stdin.readline

while True:
    strings = input().rstrip()
    if strings == ".":
        break

    stk = []
    for string in strings:
        if string == "(" or string == "[":
            stk.append(string)
            continue

        if stk and (string == ")" or string == "]"):
            if string == ")" and stk[-1] == "(":
                stk.pop()
            elif string == "]" and stk[-1] == "[":
                stk.pop()
            else:
                stk.append(string)
        elif not stk and string == ")" or string == "]":
            stk.append(string)

    if not stk:
        print("yes")
    else:
        print("no")
