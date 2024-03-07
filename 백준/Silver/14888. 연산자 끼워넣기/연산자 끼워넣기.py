import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
operationSymbols = list(map(int, input().split()))
maxValue = -1e9 + 1
minvalue = 1e9 + 1


def dfs(x, indexOfSymbols, ans):
    global maxValue, minvalue

    if indexOfSymbols == 0:
        ans += numbers[x + 1]
    elif indexOfSymbols == 1:
        ans -= numbers[x + 1]
    elif indexOfSymbols == 2:
        ans *= numbers[x + 1]
    else:
        if ans < 0 and numbers[x + 1] > 0:
            ans = (abs(ans) // numbers[x + 1]) * -1
        else:
            ans = ans // numbers[x + 1]

    if sum(operationSymbols) == 0:
        maxValue = max(maxValue, ans)
        minvalue = min(minvalue, ans)
        return

    for i in range(4):
        if operationSymbols[i] > 0:
            operationSymbols[i] -= 1
            dfs(x + 1, i, ans)
            operationSymbols[i] += 1


for i in range(4):
    ans = numbers[0]
    if operationSymbols[i] > 0:
        operationSymbols[i] -= 1
        dfs(0, i, ans)
        operationSymbols[i] += 1

print(maxValue)
print(minvalue)
