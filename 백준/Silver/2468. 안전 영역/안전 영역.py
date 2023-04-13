import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
safeZone = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
count = 1

precipitation = []
for i in range(N):
    for j in range(N):
        precipitation.append(safeZone[i][j])

min_precipitation = min(precipitation)
max_precipitation = max(precipitation)

# 상,하,좌,우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, precipitation):
    # 상,하,좌,우 순으로 인접지역 탐색
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        # 인접지역의 유효성 검사
        if (0 <= nx < N) and (0 <= ny < N) and (safeZone[nx][ny] > precipitation) and (visited[nx][ny] == 0):
            visited[nx][ny] = 1
            dfs(nx, ny, precipitation)


for precipitation in range(min_precipitation, max_precipitation):
    _count = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 안전지역의 높이가 강수량보다 높고 한번도 방문하지 않았다면
            if (safeZone[i][j] > precipitation) and visited[i][j] == 0:
                dfs(i, j, precipitation)
                _count += 1
    count = max(count, _count)

print(count)
