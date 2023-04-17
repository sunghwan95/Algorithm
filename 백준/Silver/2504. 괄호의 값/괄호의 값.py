strings = list(map(str, input()))
stk = []
answer = 0
tmp = 1

for i in range(len(strings)):
    if strings[i] == "(":
        stk.append("(")
        tmp *= 2
    elif strings[i] == "[":
        stk.append("[")
        tmp *= 3
    elif strings[i] == ")":
        if not stk or stk[-1] == "[":
            answer = 0
            break
        if strings[i-1] == "(":
            answer += tmp
        stk.pop()
        tmp //= 2
    else:
        if not stk or stk[-1] == "(":
            answer = 0
            break
        if strings[i-1] == "[":
            answer += tmp
        stk.pop()
        tmp //= 3

if stk:
    print(0)
else:
    print(answer)
