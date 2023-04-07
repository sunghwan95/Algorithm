N = int(input())
nums = list(map(int, input().split()))
count = 0

for num in nums:
    for x in range(2, num+1):
        if num % x == 0:
            if num == x:
                count += 1
            break
print(count)
