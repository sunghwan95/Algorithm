import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [0] * 101
visited = [0] * 101

ladders = {}
for _ in range(N):
    a, b = map(int, input().split())
    ladders[a] = b

snakes = {}
for _ in range(M):
    a, b = map(int, input().split())
    snakes[a] = b


def bfs(a):
    queue = deque()
    queue.append(a)

    while queue:
        location = queue.popleft()

        if location == 100:
            return graph[location]

        for i in range(1, 7):
            n_location = location + i

            if n_location <= 100:
                if n_location in ladders.keys():
                    n_location = ladders[n_location]
                elif n_location in snakes.keys():
                    n_location = snakes[n_location]

                if visited[n_location] == 0:
                    visited[n_location] = 1
                    queue.append(n_location)
                    graph[n_location] = graph[location] + 1


print(bfs(1))
