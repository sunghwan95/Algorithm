import sys
import bisect
sys.setrecursionlimit(3*10**5)

N = int(sys.stdin.readline())


coordinate = []
for _ in range(N):
    x, r = map(int, sys.stdin.readline().split())
    coordinate.append((x-r, x+r))

coordinate = sorted(coordinate, key=lambda x: (x[0], -x[1]))
count = 0

# 두 원의 오른쪽 좌표가 겹쳐지는 원이 나올때까지 재귀적으로 조사하는 함수.
def recursion(current, _next):
    global count
    # 현재 좌표의 끝 점과 다음 좌표의 끝 점이 같다면 조사를 마쳤으니 함수 종료.
    if coordinate[current][1] == coordinate[_next][1]:
        count += 1
        return
    
    # 조사하고 있는 원의 끝 점을 시작 좌표로 가지는 원이 없다면 함수종료.
    tmp = bisect.bisect_left(coordinate, (coordinate[_next][1],))
    if tmp == len(coordinate):
        return
    
    # 조사하고 있는 원의 끝 점을 시작 좌표로 공유하는 모든 원들에 대해서 재귀조사.
    if coordinate[tmp][0] == coordinate[_next][1]:
        recursion(current, tmp)


for i in range(N-1):
    # 만약 두 원의 왼쪽좌표가 같다면
    if coordinate[i][0] == coordinate[i+1][0]:
        # 오른쪽 좌표가 같은 원이 나올때까지 재귀적으로 조사.
        recursion(i, i+1)

print(N+count+1)
