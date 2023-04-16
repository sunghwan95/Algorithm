N = int(input())

towers = list(map(int, input().split()))

stk = []
result = [0]*N
for i, tower in enumerate(towers):
    while stk and stk[-1][1] <= tower:
        stk.pop()
    if stk:
        result[i] = stk[-1][0]
    stk.append([i+1, tower])

print(" ".join(map(str, result)))
