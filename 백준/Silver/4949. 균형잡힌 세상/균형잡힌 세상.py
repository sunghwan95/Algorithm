import sys

input = sys.stdin.readline

while True:
    strings = list(map(str, input().rstrip(" ")))

    if strings[0] == ".":
        exit(0)

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

        elif not stk and (string == ")" or string == "]"):
            stk.append(string)

    if stk:
        print("no")
    else:
        print("yes")
