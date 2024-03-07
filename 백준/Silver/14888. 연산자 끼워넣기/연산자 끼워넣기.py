import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
operationSymbols = list(map(int, input().split()))
maxValue = -1e9 + 1
minvalue = 1e9 + 1


def calculateAccordingToIndex(x, indexOfSymbols, num):
    if indexOfSymbols == 0:
        num += numbers[x + 1]
    elif indexOfSymbols == 1:
        num -= numbers[x + 1]
    elif indexOfSymbols == 2:
        num *= numbers[x + 1]
    else:
        if num < 0 and numbers[x + 1] > 0:
            num = (abs(num) // numbers[x + 1]) * -1
        else:
            num = num // numbers[x + 1]

    return num


def dfs(indexOfNumbers, indexOfSymbols, operand):
    global maxValue, minvalue

    res = calculateAccordingToIndex(indexOfNumbers, indexOfSymbols, operand)

    if sum(operationSymbols) == 0:
        maxValue = max(maxValue, res)
        minvalue = min(minvalue, res)
        return

    for i in range(4):
        if operationSymbols[i] > 0:
            operationSymbols[i] -= 1
            dfs(indexOfNumbers + 1, i, res)
            operationSymbols[i] += 1


initNum = numbers[0]
for i in range(4):
    if operationSymbols[i] > 0:
        operationSymbols[i] -= 1
        dfs(0, i, initNum)
        operationSymbols[i] += 1

print(maxValue, minvalue, sep="\n")
