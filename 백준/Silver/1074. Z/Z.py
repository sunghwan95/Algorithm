N, r, c = map(int, input().split())


def recursion(N, r, c):
    if N == 0:
        return 0
    return 4*recursion(N-1, r//2, c//2)+2*(r % 2)+c % 2


print(recursion(N, r, c))
