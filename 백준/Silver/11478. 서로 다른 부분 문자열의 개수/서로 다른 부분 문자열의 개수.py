import sys

input = sys.stdin.readline

word = str(input().rstrip())

ans = set()
for i in range(len(word)):
    for j in range(i, len(word)):
        ans.add(word[i : j + 1])

print(len(ans))
