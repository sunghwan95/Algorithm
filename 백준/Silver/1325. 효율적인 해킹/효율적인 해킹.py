import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)


def bfs(a):
    queue = deque([a])
    is_hacked = [0] * (N + 1)
    is_hacked[a] = 1

    cnt = 0
    while queue:
        i = queue.popleft()

        for j in graph[i]:
            if is_hacked[j] == 0:
                is_hacked[j] = 1
                cnt += 1
                queue.append(j)

    return cnt


ans = []
for start in range(1, len(graph)):
    ans.append(bfs(start))

max_cnt = max(ans)
for i in range(len(ans)):
    if ans[i] == max_cnt:
        print(i + 1)
