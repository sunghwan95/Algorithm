T=int(input())
for _ in range(T):
    case=list(map(str,input().split()))
    num=float(case[0])
    for i in case[1:]:
        if i=="@":
            num*=3
        elif i=="%":
            num+=5
        else :
            num-=7
    print(f'{num:0.2f}')
            
        