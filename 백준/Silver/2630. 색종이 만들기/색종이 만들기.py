import sys

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    arr.append(a)

blue = 1
white = 0

count_blue = 0
count_white = 0


def recursion(size, x, y):
    global count_blue
    global count_white
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
        count_white += 1
    elif color == blue:
        count_blue += 1


recursion(N, 0, 0)

print(count_white)
print(count_blue)
