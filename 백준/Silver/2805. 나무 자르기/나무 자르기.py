import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()

min_h = 1
max_h = max(trees)

while min_h <= max_h:
    cut_h = (min_h + max_h) // 2

    ans = 0
    for tree in trees:
        if tree > cut_h:
            ans += tree - cut_h

    if ans >= M:
        min_h = cut_h + 1
    else:
        max_h = cut_h - 1

print(max_h)
