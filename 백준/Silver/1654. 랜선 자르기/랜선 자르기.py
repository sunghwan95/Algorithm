import sys

input = sys.stdin.readline

K, N = map(int, input().split())

cables = []
for _ in range(K):
    a = int(input())
    cables.append(a)

start = 1
end = max(cables)

ans = 0
while start <= end:
    mid = (start + end) // 2

    curr_ans = 0
    for cable in cables:
        curr_ans += cable // mid

    if curr_ans < N:
        end = mid - 1
    elif curr_ans >= N:
        ans = max(ans, mid)
        start = mid + 1


print(ans)
