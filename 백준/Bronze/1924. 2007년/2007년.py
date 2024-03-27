import sys

input = sys.stdin.readline

x, y = map(int, input().split())
dayList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
monthToDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


totalDays = 0
if x > 1:

    for i in monthToDays[: x - 1]:
        totalDays += i

    totalDays += y
    ans = dayList[totalDays % 7]
else:
    ans = dayList[y % 7]

print(ans)
