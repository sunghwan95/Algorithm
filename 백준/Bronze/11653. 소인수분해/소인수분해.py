N=int(input())
a=2
while N!=1:
    if N%a==0:
        print(a)
        N=N//a
    else : a+=1