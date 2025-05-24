def backtracking(arr, canExchange):
    global ans

    if canExchange == 0:
        res = int("".join(arr))
        ans = max(ans, res)
        return

    key = (tuple(arr), canExchange)
    if key in visited:
        return
    visited.add(key)

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            backtracking(arr, canExchange - 1)
            arr[i], arr[j] = arr[j], arr[i]


T = int(input())

for tc in range(1, T + 1):
    num, canExchange = map(int, input().split())
    nums = []
    for _num in str(num):
        nums.append(_num)

    visited = set()

    ans = 0
    backtracking(nums, canExchange)

    print(f"#{tc} {ans}")
