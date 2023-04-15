import sys

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    arr.append(a)

blue = 1
white = 0

answer = []


def recursion(size, x, y):
    color = arr[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if color != arr[i][j]:
                recursion(size//2, x,         y)
                recursion(size//2, x+size//2, y)
                recursion(size//2, x,         y+size//2)
                recursion(size//2, x+size//2, y+size//2)
                return
    if color == white:
        answer.append(0)
    elif color == blue:
        answer.append(1)


recursion(N, 0, 0)

print(answer.count(0))
print(answer.count(1))
