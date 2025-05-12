T = int(input())

for i in range(1, T + 1):
    nums = list(map(int, input().split()))

    avg_nums = sum(nums) / len(nums)
    ans = round(avg_nums)

    print(f"#{i} {ans}")