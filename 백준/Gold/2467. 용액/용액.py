import sys
input = sys.stdin.readline

N = int(input())

solutions = list(map(int, input().split()))

value = 2000000000
start = 0
end = N-1

a, b = 0, 0

while start < end:
    cur_value = solutions[start]+solutions[end]

    if abs(cur_value) < value:
        a = solutions[start]
        b = solutions[end]
        value = abs(cur_value)

    if cur_value > 0:
        end -= 1
    elif cur_value < 0:
        start += 1
    else:
        print(a, b)
        exit(0)

print(a, b)
