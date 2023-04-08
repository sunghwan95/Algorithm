N = int(input())
arr = []
for n in range(1, N+1):
    arr.append(n)


def multiply(arr):
    ans = 1
    for n in arr:
        if n == 0:
            return 0
        ans *= n
    return print(ans)


multiply(arr)
