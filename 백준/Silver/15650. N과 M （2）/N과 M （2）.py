N, M = map(int, input().split())
arr = []


def dfs(x):

    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return

    for i in range(x, N+1):
        if i not in arr:
            arr.append(i)
            dfs(i+1)
            arr.pop()


dfs(1)
