def check(x):
    for i in range(x):
        if (col[x] == col[i]) or (abs(col[x]-col[i]) == x-i):
            return False
    return True


def recursion(x):
    global count

    if x == N:
        count += 1
    else:
        for i in range(N):
            col[x] = i
            if check(x):
                recursion(x+1)


N = int(input())
col = [0]*N
count = 0

recursion(0)
print(count)
