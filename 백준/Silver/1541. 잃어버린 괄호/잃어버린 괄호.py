import sys
input = sys.stdin.readline

expression = str(input().rstrip())
nums = expression.split("-")

arr = []
arr_2 = []
for num in nums:
    a = num.split("+")
    for i in a:
        if i.startswith("0"):
            i = int(i)
            arr_2.append(i)
        else:
            arr_2.append(int(i))
    arr.append(sum(arr_2))
    arr_2 = []


ans = arr[0]
for i in range(1, len(arr)):
    ans -= arr[i]

print(ans)
