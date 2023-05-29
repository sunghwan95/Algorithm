import sys
input = sys.stdin.readline

N = int(input())

res = 0
while N >= 0:
    if N % 5 == 0:
        res += N//5
        print(res)
        break
    N -= 3
    res += 1
else:
    print(-1)
