from collections import deque
import sys

input = sys.stdin.readline

N = int(input())  # 게임 보드의 크기 N*N
K = int(input())  # 과일의 개수

# 게임보드 생성
graph = []
for _ in range(N):
    a = [0] * N
    graph.append(a)

# 과일이 있는 위치를 게임 보드에 표시
for i in range(K):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 2

L = int(input())  # 뱀의 방향 변환 횟수
direction_dict = dict()  # 뱀의 방향 변환 정보를 저장하는 딕셔너리
snake = deque()  # 뱀의 위치를 저장하는 deque
snake.append((0, 0))  # 뱀의 초기 위치 설정

# 뱀의 방향 변환 정보 입력
for i in range(L):
    X, C = input().split()
    direction_dict[int(X)] = C


# 뱀을 이동시키기 위한 x,y축 방향 벡터 (인덱스 순서대로 우,하,좌,상)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 뱀의 초기 방향 (오른쪽)
direction = 0

x, y = 0, 0  # 뱀의 초기 위치
graph[x][y] = 1  # 뱀이 있는 위치를 1로 표시
count = 0  # 시간(턴) 카운트

while True:
    count += 1

    # 입력받은 방향으로 쭉 직진
    x += dx[direction]
    y += dy[direction]

    # 게임 보드를 벗어나면 게임 종료
    if (not 0 <= x < N) or (not 0 <= y < N):
        break

    # 과일을 먹는 경우
    if graph[x][y] == 2:
        graph[x][y] = 1
        snake.append((x, y))
        # 방향 전환 시점이면 방향 전환
        if count in direction_dict:
            C = direction_dict[count]
            if C == "L":  # 왼쪽으로 회전
                direction = (direction - 1) % 4
            else:  # 오른쪽으로 회전
                direction = (direction + 1) % 4

    # 빈 칸을 이동하는 경우
    elif graph[x][y] == 0:
        graph[x][y] = 1
        snake.append((x, y))
        tale_x, tale_y = (
            snake.popleft()
        )  # 뱀의 꼬리 부분을 비워준다고 문제에서 그랬으니 popleft
        graph[tale_x][tale_y] = 0
        # 방향 전환 시점이면 방향 전환
        if count in direction_dict:
            C = direction_dict[count]
            if C == "L":  # 왼쪽으로 회전
                direction = (direction - 1) % 4
            else:  # 오른쪽으로 회전
                direction = (direction + 1) % 4

    # 자기 자신의 몸과 부딪히는 경우 게임 종료
    else:
        break

print(count)
