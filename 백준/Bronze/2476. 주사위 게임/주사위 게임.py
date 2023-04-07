N = int(input())
x = 0

for i in range(N):
    a, b, c = map(int, input().split())
    if a == b == c:
        x = max(x, 10000+a*1000)
    elif a == b:
        x = max(x, 1000+a*100)
    elif a == c:
        x = max(x, 1000+a*100)
    elif b == c:
        x = max(x, 1000+b*100)
    else:
        x = max(x, 100*max(a, b, c))
print(x)