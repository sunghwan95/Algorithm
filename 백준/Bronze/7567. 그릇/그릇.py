a = input()
b = 10
n = 0
for _ in a:
    if len(a) == 1:
        b = b
    elif a[n] == a[n+1]:
        b += 5
        n += 1
        try:
            a[n+1]
        except IndexError:
            break
    elif a[n] != a[n+1]:
        b += 10
        n += 1
        try:
            a[n+1]
        except IndexError:
            break
print(b)