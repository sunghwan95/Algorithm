import sys

N = int(sys.stdin.readline())
row = [0]*N
count = 0


def check(x):
    for i in range(x):
        # 같은 열에 퀸이 존재하거나 대각선에 퀸이 있는 경우 False 반환.
        if (row[x] == row[i]) or (abs(row[x]-row[i]) == abs(x-i)):
            return False
    return True


def recursion(x):
    global count

    if x == N:
        count += 1
    else:
        for i in range(N):
            # (x,i)좌표에 퀸을 놓는다.
            row[x] = i
            # 퀸을 해당위치에 넣을 수 있는지 없는지 확인
            if check(x):
                recursion(x+1)


recursion(0)
print(count)
