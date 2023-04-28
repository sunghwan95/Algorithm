import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)]
queue = deque()

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 진입차수 + 1
    inDegree[b] += 1

for i in range(1, N+1):
    # 진입차수가 0인 원소들을 큐에 삽입.
    if inDegree[i] == 0:
        queue.append(i)

ans = []
while queue:
    x = queue.popleft()
    ans.append(x)
    for i in graph[x]:
        # x와 연결된 간선들을 하나씩 제거
        inDegree[i] -= 1
        # 간선 제거 후 인접차수가 0이 되면 큐에 삽입
        if inDegree[i] == 0:
            queue.append(i)

for i in ans:
    print(i, end=" ")
