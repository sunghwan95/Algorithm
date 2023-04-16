import sys

T = int(sys.stdin.readline())


for _ in range(T):
    stk = list(map(str, sys.stdin.readline()))
    stk.pop()

    if len(stk) % 2 == 1:
        print("NO")
    else:
        i = 0
        while True:
            try:
                if len(stk) == 0:
                    print("YES")
                    break
                elif len(stk) == 1:
                    print("NO")
                    break

                if stk[0] == ")":
                    print("NO")
                    break
            except IndexError:
                break

            else:
                try:
                    if stk[i] != stk[i+1]:
                        stk.pop(i)
                        stk.pop(i)
                        i = 0
                    else:
                        i += 1
                except IndexError:
                    if stk[0] != stk[-1]:
                        print("YES")
                        break
                    else:
                        print("NO")
                        break
