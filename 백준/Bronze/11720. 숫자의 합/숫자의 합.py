import sys
input = sys.stdin.readline

N = str(input())
nums = list(map(int, (input().rstrip())))

ans = 0
for num in nums:
    ans += num

print(ans)
