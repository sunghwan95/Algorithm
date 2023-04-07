N = int(input())
arr = []
for _ in range(N):
    a = int(input())
    arr.append(a)
b = "".join(str(i) for i in arr)
if b.count("1") > b.count("0"):
    print("Junhee is cute!")
elif b.count("1") < b.count("0"):
    print("Junhee is not cute!")