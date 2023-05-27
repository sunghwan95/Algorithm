import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

res = []


def dfs():
    if len(res) == M:
        print(" ".join(map(str, res)))
        return

    prev_dupl = 0
    for num in nums:
        if prev_dupl != num:
            res.append(num)
            dfs()
            prev_dupl = num
            res.pop()


dfs()
