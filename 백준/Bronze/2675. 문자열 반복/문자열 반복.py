T = int(input())
for _ in range(T):
    R, S = input().split()
    p = ""
    for i in S:
        p += int(R)*i
    print(p)
