import sys

N = int(input())

values = list(map(int, input().split()))
values.sort()

start = 0
end = len(values) - 1

min_value = sys.maxsize
while start < end:
    sum_value = values[start] + values[end]

    if abs(sum_value) <= min_value:
        min_value = abs(sum_value)
        ans = [values[start], values[end]]

    if sum_value < 0:
        start += 1
    elif sum_value > 0:
        end -= 1
    else:
        break

print(*ans)
