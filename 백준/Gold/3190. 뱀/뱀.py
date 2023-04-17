from collections import deque

N = int(input())
K = int(input())

graph = []
for _ in range(N):
    a = [0]*N
    graph.append(a)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(K):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 2

L = int(input())
dirDict = dict()
snake = deque()
snake.append((0, 0))

for i in range(L):
    X, C = input().split()
    dirDict[int(X)] = C

x, y = 0, 0
graph[x][y] = 1
count = 0
direction = 0


def turn(a):
    global direction
    if a == "L":
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4


while True:
    count += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= N or y < 0 or y >= N:
        break

    if graph[x][y] == 2:
        graph[x][y] = 1
        snake.append((x, y))
        if count in dirDict:
            turn(dirDict[count])

    elif graph[x][y] == 0:
        graph[x][y] = 1
        snake.append((x, y))
        tx, ty = snake.popleft()
        graph[tx][ty] = 0
        if count in dirDict:
            turn(dirDict[count])

    else:
        break

print(count)
