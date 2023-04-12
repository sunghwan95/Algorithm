N, r, c = map(int, input().split())

answer = 0


def recursion(length, x, y):
    global answer

    # 찾는 행과 열에 도달했을 때
    if x == r and y == c:
        print(int(answer))
        return
    
    # 더 쪼갤 수 없을만큼 쪼갰을때 하나씩 탐색하기(1씩 더하기.)
    if length == 1:
        answer += 1
        return
    
    # r과 c중 하나라도 범위 밖에 있다면 넓이더해주기.
    if not ((x <= r < x+length) and (y <= c < y+length)):
        answer += length**2
        return
    
    # 1 사분면
    recursion(length/2, x, y)
    # 2 사분면
    recursion(length/2, x, y+length/2)
    # 3 사분면
    recursion(length/2, x+length/2, y)
    # 4 사분면
    recursion(length/2, x+length/2, y+length/2)


recursion(2**N, 0, 0)
