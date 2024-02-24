import sys

input = sys.stdin.readline

strings = input().rstrip()
stk = []

count = 0
for i in range(len(strings)):
    if strings[i] == "(":
        stk.append("(")
    elif strings[i] == ")":
        if strings[i - 1] == "(":
            stk.pop()
            count += len(stk)
        else:
            stk.pop()
            count += 1

print(count)
