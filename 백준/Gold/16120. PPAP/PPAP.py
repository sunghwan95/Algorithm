import sys
input = sys.stdin.readline

string = list(map(str, input()))
string.pop()
check_ppap = ["P", "P", "A", "P"]


stk = []
for i in range(len(string)):
    stk.append(string[i])
    if stk[-4:] == check_ppap:
        for _ in range(4):
            stk.pop()
        stk.append("P")

if stk == ["P", "P", "A", "P"] or stk == ["P"]:
    print("PPAP")
else:
    print("NP")
