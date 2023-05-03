import sys
input = sys.stdin.readline

i = 1
while True:
    L, P, V = map(int, input().split())
    if P == 0 and L == 0 and V == 0:
        break
    camping = (L * (V // P)) + min((V % P), L)
    print(f'Case {i}: {camping}')
    i += 1
