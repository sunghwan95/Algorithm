num = str(input().rstrip())

ans = [0]
for i in num:
    ans.append(ans[-1] + int(i))

print(ans[-1])