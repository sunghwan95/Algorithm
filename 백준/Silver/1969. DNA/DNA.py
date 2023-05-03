import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dna = []
for _ in range(N):
    a = str(input())
    dna.append(a)


count = 0
result = []
for i in range(M):
    arr = [0, 0, 0, 0]
    for j in range(N):
        if dna[j][i] == 'A':
            arr[0] += 1
        elif dna[j][i] == 'C':
            arr[1] += 1
        elif dna[j][i] == 'G':
            arr[2] += 1
        elif dna[j][i] == 'T':
            arr[3] += 1

    idx = arr.index(max(arr))
    if idx == 0:
        result.append('A')
    elif idx == 1:
        result.append('C')
    elif idx == 2:
        result.append('G')
    elif idx == 3:
        result.append('T')
    count += N - max(arr)

print("".join(map(str, result)))
print(count)
