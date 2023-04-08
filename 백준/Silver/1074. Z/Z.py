N, r, c = map(int, input().split())


def recursion(N, r, c):
    if N == 0:
        return 0
    # 행과 열이 서로 같고 2배가 될 때 값이 4배가 되는 것을 역으로 이용.
    # 만약 행과 열이 2로 나누어 떨어지지 않아도 행과 열이 짝수,홀수로 반복되기 때문에 몫만 신경쓰면됨.
    # 가장 기본 단위의 Z모양이 0,1,2,3이기 떄문에 이를 이용하여 위치 조정.
    return 4*recursion(N-1, r//2, c//2)+(2*(r % 2))+c % 2


print(recursion(N, r, c))
