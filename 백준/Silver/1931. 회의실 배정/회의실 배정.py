import sys
input = sys.stdin.readline

N = int(input())

meetings = []
for _ in range(N):
    a = list(map(int, input().split()))
    meetings.append(a)

meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

res = []
start = 0
end = 0
for meeting in meetings:
    if not res:
        res.append(meeting)
        start = meeting[0]
        end = meeting[1]
        continue
    if meeting[0] < end:
        continue
    else:
        res.append(meeting)
        start = meeting[0]
        end = meeting[1]

print(len(res))
