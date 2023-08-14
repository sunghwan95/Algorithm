import sys
input = sys.stdin.readline

N = int(input())

papers = []
for _ in range(N):
    row = list(map(int, input().split()))
    papers.append(row)

ans = []


def recursion(x, y, size):
    color = papers[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if color != papers[i][j]:
                recursion(x,         y,         size//2)
                recursion(x+size//2, y,         size//2)
                recursion(x,         y+size//2, size//2)
                recursion(x+size//2, y+size//2, size//2)
                return

    if color == 1:
        ans.append(1)
    else:
        ans.append(0)


recursion(0, 0, N)

print(ans.count(0), ans.count(1), sep="\n")
