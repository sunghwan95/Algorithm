import sys
input=sys.stdin.readline

N, M, K=map(int, input().split())
team = 0
while True :
    N-=2
    M-=1
    if N<0 or M<0 or (N+M)<K:
        break
    team+=1
print(team)