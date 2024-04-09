import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

graph = [0] * 100001
visited = [0] * 100001


def bfs(a):
    queue = deque()
    queue.append(a)
    visited[a] = 1

    while queue:
        location = queue.popleft()

        if location == K:
            return graph[location]

        for i in range(3):
            if i == 0:
                n_location = location + 1

                if 0 <= n_location < 100001 and visited[n_location] == 0:
                    visited[n_location] = 1
                    queue.append(n_location)
                    graph[n_location] = graph[location] + 1

            elif i == 1:
                n_location = location - 1

                if 0 <= n_location < 100001 and visited[n_location] == 0:
                    visited[n_location] = 1
                    queue.append(n_location)
                    graph[n_location] = graph[location] + 1

            else:
                n_location = location * 2

                if 0 <= n_location < 100001 and visited[n_location] == 0:
                    visited[n_location] = 1
                    queue.append(n_location)
                    graph[n_location] = graph[location] + 1


print(bfs(N))
