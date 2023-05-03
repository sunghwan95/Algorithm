import sys
input=sys.stdin.readline

N = list(input())
N.sort(reverse=True)
num = ""

for i in N:
    num += i

if int(num) % 30 == 0:
    print(num)
else:
    print(-1)