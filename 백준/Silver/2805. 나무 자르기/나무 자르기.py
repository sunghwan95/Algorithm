N, M = map(int, input().split())
trees = list(map(int, input().split()))

min_height, max_height = 1, max(trees)

while min_height <= max_height:
    cut_height = (min_height+max_height)//2
    answer = 0

    for tree in trees:
        if tree > cut_height:
            answer += tree-cut_height

    if answer >= M:
        min_height = cut_height+1
    else:
        max_height = cut_height-1

print(max_height)
