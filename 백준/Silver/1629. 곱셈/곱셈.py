import sys

A, B, C = map(int, sys.stdin.readline().split())


def recursion(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (recursion(a, b//2, c)**2) % c
    else:
        return ((recursion(a, b//2, c)**2) * a) % c


print(recursion(A, B, C))
