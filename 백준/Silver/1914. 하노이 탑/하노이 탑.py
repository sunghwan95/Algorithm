import sys
N = int(sys.stdin.readline())


def move(N, x, y):
    if N > 0 and N <= 20:
        move(N-1, x, 6-x-y)
        print(f'{x} {y}')
        move(N-1, 6-x-y, y)


print(2**N-1)
move(N, 1, 3)
