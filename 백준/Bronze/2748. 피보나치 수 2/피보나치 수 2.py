import sys
input = sys.stdin.readline

n = int(input())
memo = [0 for _ in range(n+1)]
memo[0] = 0
memo[1] = 1

for i in range(2, len(memo)):
    memo[i] = memo[i-1]+memo[i-2]


print(memo[n])
