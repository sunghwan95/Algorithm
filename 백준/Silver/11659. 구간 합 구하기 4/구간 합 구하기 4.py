import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))

prefixSum = [0] * (N + 1)
for i in range(1, N + 1):
    prefixSum[i] = nums[i - 1] + prefixSum[i - 1]

for _ in range(M):
    i, j = map(int, input().split())
    ans = prefixSum[j] - prefixSum[i - 1]
    print(ans)
