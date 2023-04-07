A,B,C=map(int,input().split())
D=int(input())
print(((A+(B+((C+D)//60))//60))%24, (B+((C+D)//60))%60, (C+D)%60)