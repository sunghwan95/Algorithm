import sys
input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    a = list(map(int, input().rstrip()))
    graph.append(a)


def div_conq(N, x, y):
    num = graph[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if num != graph[i][j]:
                print("(", end="")
                div_conq(N//2, x,      y)
                div_conq(N//2, x,      y+N//2)
                div_conq(N//2, x+N//2, y)
                div_conq(N//2, x+N//2, y+N//2)
                print(")", end="")
                return

    if num == 0:
        print(0, end="")
        return
    else:
        print(1, end="")
        return


div_conq(N, 0, 0)
