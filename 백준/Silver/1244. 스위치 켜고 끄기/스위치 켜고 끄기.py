import sys

N = int(sys.stdin.readline())
switchs = [-1] + list(map(int, sys.stdin.readline().split()))
students = int(sys.stdin.readline())

for _ in range(students):
    gender, switch_num = map(int, sys.stdin.readline().split())
    if gender == 1:
        i = 1
        while switch_num * i <= N:
            switchs[switch_num * i] = 1 - switchs[switch_num * i]
            i += 1
    else:
        switchs[switch_num] = 1 - switchs[switch_num]
        i = 1
        while (
            switch_num - i >= 1
            and switch_num + i <= N
            and switchs[switch_num - i] == switchs[switch_num + i]
        ):
            switchs[switch_num - i] = 1 - switchs[switch_num - i]
            switchs[switch_num + i] = 1 - switchs[switch_num + i]
            i += 1

for i in range(1, N + 1):
    print(switchs[i], end=" ")
    if i % 20 == 0 or i == N:
        print()
