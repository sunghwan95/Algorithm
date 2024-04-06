import sys

input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())

        legos = [int(input()) for _ in range(n)]
        legos.sort()

        start = 0
        end = n - 1

        if start == end:
            print("danger")
            continue

        flag = False
        while start < end:
            selected_lego = legos[start] + legos[end]

            if selected_lego > x:
                end -= 1
            elif selected_lego < x:
                start += 1
            else:
                flag = True
                break

        if flag:
            print("yes", legos[start], legos[end])
        else:
            print("danger")

    except:
        break
