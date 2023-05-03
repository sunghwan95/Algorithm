import sys
input = sys.stdin.readline

N = int(input())
positive = []
negative = []
ans = 0
for i in range(N):
    a = int(input())
    if a == 1:
        ans += 1
    elif a > 0:
        positive.append(a)
    else:
        negative.append(a)

positive.sort()
negative.sort(reverse=True)

while len(positive) != 0:
    if len(positive) == 1:
        ans += positive.pop()
    else:
        ans += positive.pop() * positive.pop()

while len(negative) != 0:
    if len(negative) == 1:
        ans += negative.pop()
    else:
        ans += negative.pop() * negative.pop()

print(ans)
