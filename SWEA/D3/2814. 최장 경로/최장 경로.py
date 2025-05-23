def dfs(node, depth):
    global max_length
    max_length = max(max_length, depth)

    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            dfs(neighbor, depth + 1)
            visited[neighbor] = False


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    max_length = 0

    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        visited[i] = True
        dfs(i, 1)

    print(f"#{tc} {max_length}")
