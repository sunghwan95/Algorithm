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
print(minimum, minimum*(max(a, b)//minimum)
      * (min(a, b)//minimum), sep="\n")