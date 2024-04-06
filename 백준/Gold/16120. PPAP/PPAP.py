import sys

input = sys.stdin.readline

strings = input().rstrip()

stk = []
for i in range(len(strings)):
    stk.append(strings[i])
    if stk[-4:] == ["P", "P", "A", "P"]:
        for _ in range(3):
            stk.pop()


if stk == ["P", "P", "A", "P"] or stk == ["P"]:
    print("PPAP")
else:
    print("NP")
