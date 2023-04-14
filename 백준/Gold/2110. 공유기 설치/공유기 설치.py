import sys
N, C = map(int, sys.stdin.readline().split())

home = []
for _ in range(N):
    a = int(sys.stdin.readline())
    home.append(a)

home.sort()
start, end = 1, max(home)-min(home)
answer = 0


def binary(home, start, end):
    while start <= end:
        mid = (start+end)//2
        current = home[0]
        count = 1

        for i in range(1, len(home)):
            if home[i] >= current+mid:
                count += 1
                current = home[i]

        if count >= C:
            global answer
            start = mid+1
            answer = mid
        else:
            end = mid-1


binary(home, start, end)
print(answer)
