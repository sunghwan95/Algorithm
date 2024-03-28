import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

ans = defaultdict(int)
for _ in range(N):
    file = str(input().rstrip())
    fileExtension = file.split(".")[1]
    ans[fileExtension] += 1

_ans = sorted(ans.keys())
for elem in _ans:
    print(elem, ans[elem])
