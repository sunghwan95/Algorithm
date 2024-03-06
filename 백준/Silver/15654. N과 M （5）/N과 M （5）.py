N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

ans = []


def dfs():
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return

    for num in nums:
        if num not in ans:
            ans.append(num)
            dfs()
            ans.pop()


dfs()
