import sys
input = sys.stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
budgets.sort()
M = int(input())

if sum(budgets) <= M:
    print(max(budgets))
else:
    start = 0
    end = max(budgets)
    while start <= end:
        mid = (start+end)//2
        total = 0

        for budget in budgets:
            if budget > mid:
                total += mid
            else:
                total += budget

        if total <= M:
            start = mid+1
        else:
            end = mid-1

    print(end)
