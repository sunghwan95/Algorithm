import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

T = int(input())


def dijkstra(start):
    visisted = [0] * (n + 1)
    hacked_times = [INF] * (n + 1)

    queue = []
    heapq.heappush(queue, (0, start))
    hacked_times[start] = 0
    visisted[start] = 1

    while queue:
        current_time, hacked_com = heapq.heappop(queue)

        for i in graph[hacked_com]:
            linked_com = i[0]
            hacked_time = i[1]

            new_time = current_time + hacked_time

            if new_time < hacked_times[linked_com]:
                visisted[linked_com] = 1
                hacked_times[linked_com] = new_time
                heapq.heappush(queue, (new_time, linked_com))

    return (sum(visisted), max(i for i in hacked_times if i != INF))


for _ in range(T):
    n, d, c = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    ans = dijkstra(c)
    print(ans[0], ans[1])
