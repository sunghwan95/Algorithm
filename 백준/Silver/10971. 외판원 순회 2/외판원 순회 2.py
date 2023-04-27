N = int(input())

visited = [0]*N
city = []  # 각각의 index가 시작위치.([0]=a도시...etc)
answer = 1e9


for _ in range(N):
    # 시작위치에서 다음 도시로 이동하는데 생기는 비용.
    a = list(map(int, input().split()))
    city.append(a)


def dfs(x, start, cost):
    global answer
    # visited[0]=1이라고 못 박았기 때문에 x==N-1 임.
    # 모든 순회를 마치고 도착지점에서 출발지점으로 가는게 0이 아니라면
    if (x == N-1) and (city[start][0] != 0):
        # answer값과 (총 cost+(도착지점~출발지점 비용))중 작은 것 추출.
        answer = min(answer, cost+city[start][0])
        return
    for i in range(N):
        # 방문한 적이 없고 같은 도시로 이동하는게 아니라면
        if (visited[i] == 0) and (city[start][i] != 0):
            # 방문 체크
            visited[i] = 1
            """ start인자 자리에 i를 넣는 이유 -> 같은도시로는 이동할 수 없기 때문.
            이 로직이 실행된 i값이 곧 도착하는 도시(=city의 인덱스 값)"""
            dfs(x+1, i, cost+city[start][i])
            # 계속 나머지 루트들을 순회하기 위해 방문x 처리.
            visited[i] = 0


# 시작 위치 고정.(어디서 시작하든 상관없기 때문에.)
visited[0] = 1
dfs(0, 0, 0)
print(answer)
