T = int(input())


def recursion(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return recursion(n-1)+recursion(n-2)+recursion(n-3)


for _ in range(T):
    n = int(input())
    print(recursion(n))
