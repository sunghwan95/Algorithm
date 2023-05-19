import sys
input = sys.stdin.readline

n = int(input())

board = []
for _ in range(n):
    a = list(map(int, input().split()))
    board.append(a)

for i in range(1, len(board)):
    for j in range(0, len(board[i])):
        if j == 0:
            board[i][j] += board[i-1][0]
            continue
        else:
            try:
                board[i][j] = max(board[i][j]+board[i-1][j-1],
                                  board[i][j]+board[i-1][j])
            except IndexError:
                board[i][j] += board[i-1][-1]

print(max(board[-1]))
