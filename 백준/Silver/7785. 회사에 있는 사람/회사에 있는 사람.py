import sys

input = sys.stdin.readline

n = int(input())

ans = dict()
for _ in range(n):
    name, enterOrLeave = map(str, input().split())
    if enterOrLeave == "enter":
        ans[name] = 1
    else:
        del ans[name]

print(*sorted(ans.keys(), reverse=True), sep="\n")
