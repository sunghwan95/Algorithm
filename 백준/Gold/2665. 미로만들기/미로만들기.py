import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    a = list(map(int, input().rstrip()))
    graph.append(a)
change=[[-1]*(n) for _ in range(n)]
change[0][0]=0
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    coordinate=deque()
    coordinate.append((0,0))
    while coordinate:
        x,y=coordinate.popleft()
        if (x,y)==(n-1,n-1):
            print(change[n-1][n-1])
            return

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if change[nx][ny]==-1:
                    if graph[nx][ny]==0:
                        change[nx][ny]=change[x][y]+1
                        coordinate.append((nx,ny))
                    elif graph[nx][ny]==1:
                        change[nx][ny]=change[x][y]
                        coordinate.appendleft((nx,ny))

                

bfs()

