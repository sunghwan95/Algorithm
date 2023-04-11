import sys
input = sys.stdin.readline
def isPrime(n):
    if n == 1:
        return 0
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return 0
        return 1
for _ in range(int(input())):
    n = int(input())
    for a in range(n//2,1,-1):
        if isPrime(a) and isPrime(n-a):
            print(a,n-a)
            break
