import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    max = 0
    val = 0
    for i in range(len(stock)-1, -1, -1):
        if (stock[i] >= max):
            max = stock[i]
        else:
            val += max-stock[i]
    print(val)
