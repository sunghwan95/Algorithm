import sys
K, N = map(int, sys.stdin.readline().split())

lines = []
for _ in range(K):
    line = int(sys.stdin.readline())
    lines.append(line)

lines.sort()
start = 1
end = lines[-1]

while start <= end:
    mid = (start+end)//2
    count = 0

    for line in lines:
        count += line//mid

    if count >= N:
        start = mid+1
    else:
        end = mid-1
print(end)
