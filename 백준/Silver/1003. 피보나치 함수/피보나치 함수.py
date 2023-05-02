T = int(input())

zero = [1, 0, 1]
one = [0, 1, 1]


def fibonacci(x):
    a = len(zero)
    if a <= x:
        for i in range(a, x+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(f'{zero[x]} {one[x]}')


for i in range(T):
    k = int(input())
    fibonacci(k)