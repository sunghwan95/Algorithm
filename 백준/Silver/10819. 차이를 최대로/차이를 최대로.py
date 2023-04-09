N = int(input())
nums = list(map(int, input().split()))
ans = []
integers = []
visited = [0]*N


def backTracking(x):
    if x == N:
        ans.append(sum(abs(integers[i]-integers[i+1]) for i in range(N-1)))
        return
    for i in range(N):
        # visited[i]가 0이면
        if not visited[i]:
            integers.append(nums[i])
            visited[i] = 1
            backTracking(x+1)
            visited[i] = 0
            integers.pop()


backTracking(0)
print(max(ans))
