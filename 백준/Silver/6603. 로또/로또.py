import sys
 
while True:
    nums = list(map(int, sys.stdin.readline().split()))
    if nums[0] == 0:
       break

    nums.pop(0)
    V = 6
    stack = []


    def dfs():
        if len(stack) == V:
            print(*stack)
            return

        if len(stack) == 0:
            for i in nums:
                stack.append(i)
                dfs()
                stack.pop()
            return

        for i in nums:
            if i > stack[len(stack) - 1]:
                stack.append(i)
                dfs()
                stack.pop()

    dfs()
    print()