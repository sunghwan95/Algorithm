import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

a = defaultdict(int)
for _ in range(N):
    not_listen = str(input().rstrip())
    a[not_listen] += 1

for _ in range(M):
    not_see = str(input().rstrip())
    a[not_see] += 1

ans = []
for key, value in a.items():
    if value == 2:
        ans.append(key)

ans.sort()
print(len(ans))
print(*ans, sep="\n")
