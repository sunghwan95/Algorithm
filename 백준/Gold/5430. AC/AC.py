from collections import deque
import sys
import ast

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    nums = deque(ast.literal_eval(input().rstrip()))

    reversed = False
    error = False

    for func in p:
        if func == "R":
            reversed = not reversed
        elif func == "D":
            if nums:
                if reversed:
                    nums.pop()
                else:
                    nums.popleft()
            else:
                print("error")
                error = True
                break

    if not error:
        if reversed:
            nums.reverse()
        result = "[" + ",".join(map(str, nums)) + "]"
        print(result)
