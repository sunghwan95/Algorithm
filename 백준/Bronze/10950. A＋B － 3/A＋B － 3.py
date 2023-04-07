T = int(input())
arr = []
for _ in range(T):
    a, b = map(int, input().split())
    arr.append([a, b])
i = 0
for _ in arr[:]:
    print(arr[i][0]+arr[i][1])
    i += 1
