import sys

input = sys.stdin.readline

X = int(input())

line_num = 1
cnt = 1
while X > cnt:
    line_num = line_num + 1
    cnt += line_num

cnt -= line_num
sequenceOfLine = X - cnt

if line_num % 2 == 0:
    numerator = sequenceOfLine
    denominator = line_num - sequenceOfLine + 1
else:
    numerator = line_num - sequenceOfLine + 1
    denominator = sequenceOfLine

print(f"{numerator}/{denominator}")
