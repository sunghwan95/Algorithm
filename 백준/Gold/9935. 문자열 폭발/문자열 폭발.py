import sys
input = sys.stdin.readline

strings = input().rstrip()
boom = input().rstrip()

stk = []

for string in strings:
    stk.append(string)
    if "".join(stk[-len(boom):]) == boom:
        for _ in range(len(boom)):
            stk.pop()

if stk:
    print(''.join(stk))
else:
    print('FRULA')
