N = int(input())
visited = [0]*(N+1)

root = []


def dfs():
    if len(root) == N:
        print(" ".join(map(str, root)))
        return
    for i in range(1, N+1):
        if (visited[i] == 0):
            root.append(i)
            visited[i] = 1
            # print(f'visited: {visited}')
            dfs()
            visited[i] = 0
            # print(f'visited: {visited}')
            root.pop()
            # print(f'root: {root}')


dfs()
