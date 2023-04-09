N, M = map(int, input().split())
arr = []


def dfs(x):

    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return

    for i in range(x, N+1):
        arr.append(i)
        dfs(1)
        arr.pop()


dfs(1)
