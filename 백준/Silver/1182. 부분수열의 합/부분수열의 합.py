import sys
N, S = map(int, sys.stdin.readline().split())
integers = list(map(int, sys.stdin.readline().split()))
ans = []
count = 0


def dfs(x):
    global count
    if sum(ans) == S and len(ans) > 0:
        count += 1
    for i in range(x, N):
        ans.append(integers[i])
        dfs(i+1)
        ans.pop()


dfs(0)
print(count)
