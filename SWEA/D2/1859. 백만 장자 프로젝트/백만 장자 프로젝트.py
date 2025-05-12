T = int(input())

for i in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    max_price = 0
    profit = 0

    for num in reversed(nums):
        if num > max_price:
            max_price = num
        else:
            profit += max_price - num

    print(f"#{i} {profit}")