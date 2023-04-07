arr = []
while True:
    a, b = map(int, input().split())
    arr.append([a, b])
    if a == 0 and b == 0:
        break
n = 0
for _ in arr[:-1]:
    if arr[n][1] % arr[n][0] == 0:
        print("factor")
        n += 1
    elif arr[n][0] % arr[n][1] == 0:
        print("multiple")
        n += 1
    else:
        print("neither")
        n += 1