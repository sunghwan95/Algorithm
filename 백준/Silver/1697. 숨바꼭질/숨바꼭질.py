import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

graph = [0] * 100001
visited = [0] * 100001

queue = deque([])
_len = len(graph)


def can_go_next(now, _next):
    if 0 <= _next < _len and visited[_next] == 0:
        visited[_next] = 1
        queue.append(_next)
        graph[_next] = graph[now] + 1


def bfs(start):
    queue.append(start)
    visited[start] = 1

    while queue:
        now = queue.popleft()

        if now == K:
            return graph[now]

        for i in range(3):
            if i == 0:
                _next = now - 1
                can_go_next(now, _next)

            elif i == 1:
                _next = now + 1
                can_go_next(now, _next)

            else:
                _next = 2 * now
                can_go_next(now, _next)


print(bfs(N))
