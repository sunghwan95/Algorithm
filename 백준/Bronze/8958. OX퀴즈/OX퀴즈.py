N = int(input())
ox_sum = []
for _ in range(N):
    ox_list = list(input())
    a = 1
    arr = []
    for listItem in ox_list:
        if listItem == "O":
            arr.append(a)
            a += 1
        else:
            a = 1
    ox_sum.append(sum(arr))
for _ in ox_sum:
    print(_)
