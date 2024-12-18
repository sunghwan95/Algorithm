import sys

input = sys.stdin.readline

N, M = map(int, input().split())

visited = [0] * (N + 1)

ans = []


def backtracking(start):
    if len(ans) == M:
        print(*ans)
        return

    for i in range(start, N + 1):
        if visited[i] == 0:
            visited[i] = 1
            ans.append(i)
            backtracking(i)
            ans.pop()
            visited[i] = 0


backtracking(1)
