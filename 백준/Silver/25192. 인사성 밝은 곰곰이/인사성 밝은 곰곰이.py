import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

ans = 0
chatters = defaultdict(int)
for _ in range(N):
    chattingLog = str(input().rstrip())
    if chattingLog != "ENTER":
        chatters[chattingLog] += 1
    else:
        ans += len(chatters)
        chatters.clear()

ans += len(chatters)
print(ans)
