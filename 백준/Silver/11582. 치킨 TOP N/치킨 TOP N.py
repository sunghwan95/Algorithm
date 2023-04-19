import sys
input = sys.stdin.readline

N = int(input())
figures = list(map(int, input().split()))
k = int(input())


def list_chunk(arr, n):
    return [arr[i:i+n] for i in range(0, len(arr), n)]


chunked_arrs = list_chunk(figures, N//k)
new_arr = []
for chunked_arr in chunked_arrs:
    a = " ".join(map(str, sorted(chunked_arr)))
    new_arr.append(a)

for i in new_arr:
    print(i, end=" ")
