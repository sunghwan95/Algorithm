N, M = map(int, input().split())
arr = []


def dfs():
    sorted_arr = sorted(arr)
    if arr != sorted_arr:
        return

    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, N+1):
        if i not in arr:
            arr.append(i)
            if arr[0] <= i:
                dfs()
            arr.pop()


dfs()
