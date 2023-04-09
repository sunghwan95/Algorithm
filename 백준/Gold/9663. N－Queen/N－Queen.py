N = int(input())
row = [0]*N
count = 0


def recursion(x):
    global count
    if x == N:
        count += 1
    else:
        for y in range(N):
            row[x] = y
            if check(x):
                recursion(x+1)


def check(x):
    for i in range(x):
        if (row[x] == row[i]) or (abs(row[x]-row[i]) == abs(x-i)):
            return False
    return True


recursion(0)
print(count)
