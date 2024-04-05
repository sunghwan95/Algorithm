import sys

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

ans = []
sequence = []

i = 1
for num in nums:
    if sequence and sequence[-1] == num:
        sequence.pop()
        ans.append("-")
        continue

    for a in range(i, n + 1):
        sequence.append(a)
        ans.append("+")
        if a == num:
            sequence.pop()
            ans.append("-")
            i = a + 1
            break

if not sequence:
    print(*ans, sep="\n")
else:
    print("NO")
