import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range(N):
    a = list(map(str, input().rstrip()))
    graph.append(a)


def count_repainted_tiles(sub_graph):
    repainted_tiles = []
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if sub_graph[i][j] != "W":
                    repainted_tiles.append((i, j))
            else:
                if sub_graph[i][j] != "B":
                    repainted_tiles.append((i, j))

    return len(repainted_tiles)


def min_repaints(N, M):
    ans = sys.maxsize

    for i in range(N - 7):
        for j in range(M - 7):
            sub_graph = [row[j : j + 8] for row in graph[i : i + 8]]
            repaints = count_repainted_tiles(sub_graph)
            ans = min(ans, repaints, 64 - repaints)

    return ans


print(min_repaints(N, M))
