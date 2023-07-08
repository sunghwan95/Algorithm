n = int(input())
arr = input()
num = ''
val = 0

for i in arr:
    if '0' <= i and i <= '9':
        num += i
    elif num != '':
        val += int(num)
        num = ''
if num != '':
    val += int(num)

print(val)
