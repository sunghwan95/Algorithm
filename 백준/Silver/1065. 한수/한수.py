N = str(input())

if len(N) <= 2:
    print(int(N))
elif len(N) >= 3:
    count = 0
    for num in range(100, int(N)+1):
        if (int(str(num)[1])*2 == int(str(num)[0])+int(str(num)[2])):
            count += 1
    print(99+count)
