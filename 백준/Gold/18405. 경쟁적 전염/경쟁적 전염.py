import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
graph = []
for _ in range(N):
    a = list(map(int, input().split()))
    graph.append(a)
S, X, Y = map(int, input().split())


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

heap = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            heapq.heappush(heap, (graph[i][j], i, j))


def bfs():
    for _ in range(S):
        virus = []
        while heap:
            target = heapq.heappop(heap)
            virus_num, x, y = target[0], target[1], target[2]
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus_num
                    virus.append((graph[nx][ny], nx, ny))
        for virus_info in virus:
            heapq.heappush(heap, virus_info)


bfs()

print(graph[X-1][Y-1])
