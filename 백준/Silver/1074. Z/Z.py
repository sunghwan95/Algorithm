N, r, c = map(int, input().split())

answer = 0


def recursion(N, x, y):
    global answer

    if x == r and y == c:
        print(int(answer))
        return

    if N == 1:
        answer += 1
        return

    if not ((x <= r < x+N) and (y <= c < y+N)):
        answer += N*N
        return

    recursion(N/2, x, y)
    recursion(N/2, x, y+N/2)
    recursion(N/2, x+N/2, y)
    recursion(N/2, x+N/2, y+N/2)


recursion(2**N, 0, 0)
