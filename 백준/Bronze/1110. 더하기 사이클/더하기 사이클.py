N = int(input())
cycle_num = 0
i = 0
add_num = 0
stringify_num = str(N)
while True:
    for _ in range(len(stringify_num)):
        add_num += int(stringify_num[i])
        i += 1
    cycle_num += 1
    stringify_num = stringify_num[-1]+str(add_num)[-1]
    i = 0
    add_num = 0
    if N == int(stringify_num):
        print(cycle_num)
        break
