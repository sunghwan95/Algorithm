T = int(input())
arr = []
for _ in range(T):
    a, b = map(int, input().split())
    maximum = max(a, b)
    minimum = min(a, b)
    while True:
        x = maximum % minimum
        try:
            y = minimum % x
        except ZeroDivisionError:
            break
        maximum = minimum
        minimum = x
        if x == 0 or y == 0:
            break
    lcd = minimum*(max(a, b)//minimum)*(min(a, b)//minimum)
    arr.append(lcd)
i = 0
for _ in arr[:]:
    print(arr[i])
    i += 1
