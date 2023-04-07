coordinate=list(map(int,input().split()))
x=coordinate[0]
y=coordinate[1]
w=coordinate[2]
h=coordinate[-1]
arr=[x,y,w-x,h-y]
print(min(arr))