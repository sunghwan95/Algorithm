N = int(input())
queue = []
for i in range(1, N + 1):
    queue.append(i)
temp = []
isRemoved = False

while len(queue) > 1:
    if isRemoved == False:
        temp.append(queue.pop(0))
        isRemoved = True
    else:
        a = queue.pop(0)
        queue.append(a)
        isRemoved = False

ans = temp + queue

for j in ans:
    print(j, end=" ")
