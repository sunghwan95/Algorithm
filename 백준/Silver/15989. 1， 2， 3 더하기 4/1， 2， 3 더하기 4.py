T = int(input())
arr = []
for _ in range(T):
    a = int(input())
    arr.append(a)

for i in arr:
    dp = [1]*(i+1)
    for j in range(2, i+1):
        dp[j] += dp[j-2]
    for j in range(3, i+1):
        dp[j] += dp[j-3]

    print(dp[i])
