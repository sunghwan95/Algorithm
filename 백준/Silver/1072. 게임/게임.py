import sys

input = sys.stdin.readline

X, Y = map(int, input().split())
Z = int((Y * 100 / X))

if Z >= 99:
    print(-1)
    exit(0)

start = 1
end = sys.maxsize

ans = sys.maxsize
while start <= end:
    mid = (start + end) // 2
    new_win_rate = int(((Y + mid) * 100 / (X + mid)))

    if new_win_rate > Z:
        ans = min(ans, mid)
        end = mid - 1
    else:
        start = mid + 1

print(ans)
