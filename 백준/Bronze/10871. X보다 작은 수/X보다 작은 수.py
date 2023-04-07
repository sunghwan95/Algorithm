N, X= map(int,input().split())
A=list(map(int,input().split()))
i=0
arr=[]
for _ in A:
    num=A[i]
    if X>num:
        arr.append(str(num))
    i+=1
print(" ".join(arr))
