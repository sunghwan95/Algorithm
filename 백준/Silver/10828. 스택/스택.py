import sys

input = sys.stdin.readline

N = int(input())
stk = []
ans = []


def push(stk: list, arg: int):
    stk.append(arg)
    return


def popArg(stk: list):
    if stk:
        ans.append(stk.pop())
    else:
        ans.append(-1)
    return


def sizeStk(stk: list):
    ans.append(len(stk))
    return


def isEmpty(stk: list):
    if stk:
        ans.append(0)
    else:
        ans.append(1)
    return


def topArg(stk: list):
    if stk:
        ans.append(stk[-1])
    else:
        ans.append(-1)
    return


for _ in range(N):
    cmd = input().split()
    keyWord = cmd[0]

    if keyWord == "push":
        push(stk, int(cmd[1]))
    elif keyWord == "top":
        topArg(stk)
    elif keyWord == "size":
        sizeStk(stk)
    elif keyWord == "pop":
        popArg(stk)
    else:
        isEmpty(stk)

print(*ans, sep="\n")
