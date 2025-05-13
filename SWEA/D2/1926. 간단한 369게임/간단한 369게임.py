N = int(input())

nums = [i for i in range(1, N + 1)]

clap = ["3", "6", "9"]

for j in nums:
    num = str(j)

    cnt = 0
    ans = ""
    for _num in num:
        if _num in clap:
            cnt += 1
        ans = "-" * cnt

    if cnt >= 1:
        print(ans, end=" ")
    else:
        print(num, end=" ")
