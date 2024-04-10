import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 인접해있는 칸 수 확인하기
# 인접해있는 칸 수 만큼 녹이기
# 덩어리가 몇개인지 확인하기
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def melt(x,y): # 인접해있는 칸 수 확인하기
    for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]
        if nx<0 or ny<0 or nx>=N or ny>=M:
            continue
        if sea[nx][ny]==0:
            around_sea[x][y]+=1


def bfs(i,j): # 덩어리가 몇 개인지 확인하기
    q = deque()
    global temp
    q.append((i,j))
    temp += 1
    while q:
        x,y = q.popleft()
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if sea[nx][ny]!=0 and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny] = temp
around_sea = [[0 for _ in range(M)] for _ in range(N)]
year = 0
while True:
    temp = 0
    count = 0
    year += 1
    visited = [[0 for _ in range(M)] for i in range(N)]
    
    for i in range(N): # 바닷물 인접 개수 구하기
        for j in range(M):
            if sea[i][j] > 0:
                count += 1 # 남아있는 얼음 개수 확인
                melt(i,j) # i,j의 인접한 칸수 확인
    if count == 0: # 다 녹을때까지 반복문 벗어나지 못했으므로 0 출력
        print(0)
        break
    for i in range(N): # 인접 개수만큼 녹이기
        for j in range(M):
            if sea[i][j] > around_sea[i][j]:
                sea[i][j]-=around_sea[i][j]
                around_sea[i][j] = 0 # 녹이고 다시 초기화
            else:
                sea[i][j] = 0
                around_sea[i][j] = 0 # 녹이고 다시 초기화


    for i in range(N): # 덩어리의 개수 구하기
        for j in range(M):
            if sea[i][j]>0 and visited[i][j]==0: # 방문한적 없고, 얼음이 있으면 bfs실행하여 덩어리 확인
                bfs(i,j) # 덩어리 개수 확인 temp에
    if temp>=2:
        print(year)
        break