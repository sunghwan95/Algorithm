import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
operations = list(map(int, input().split()))
max_num = -1e9
min_num = 1e9
answer = nums[0]


def dfs(x):
    global answer
    global max_num, min_num

    if x == N:
        max_num = max(max_num, answer)
        min_num = min(min_num, answer)
        return

    for i in range(4):
        tmp = answer
        if operations[i] > 0:
            if i == 0:
                answer += nums[x]
            elif i == 1:
                answer -= nums[x]
            elif i == 2:
                answer *= nums[x]
            else:
                if answer >= 0:
                    answer = answer//nums[x]
                else:
                    answer = (-answer//nums[x])*-1

            operations[i] -= 1
            dfs(x+1)
            answer = tmp
            operations[i] += 1


dfs(1)
print(max_num)
print(min_num)
