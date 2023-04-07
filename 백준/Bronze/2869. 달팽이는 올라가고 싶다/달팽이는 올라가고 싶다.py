import sys
A, B, V = map(int, sys.stdin.readline().split())
# V-A의 값이 A-B의 값보다 작으면 무조건 2일
# 만약 V-A값이 더 크다면 A-B의 값으로 나눈 몫에서 +1
if A == V:
    print(1)
elif V-A <= A-B:
    print(2)
elif V-A > A-B:
    if (V-A) % (A-B) == 0:
        print((V-A) // (A-B)+1)
    else:
        print((V-A) // (A-B)+2)
