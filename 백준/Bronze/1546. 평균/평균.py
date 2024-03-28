import sys

input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))

maxScore = max(scores)

ans = []
for score in scores:
    modifiedScore = score / maxScore * 100
    ans.append(modifiedScore)

print(float(sum(ans) / len(ans)))
