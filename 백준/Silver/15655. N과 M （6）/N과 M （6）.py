import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

visited = [0] * N

ans = []


def backtracking(a):
    global ans

    if len(ans) == M:
        print(*ans)
        return

    for i in range(a, N):
        if visited[i] == 0:
            visited[i] = 1
            ans.append(nums[i])
            backtracking(i)
            ans.pop()
            visited[i] = 0


backtracking(0)
