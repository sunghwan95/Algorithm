import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    docs = list(map(int, input().split()))

    queue = deque([(idx, priority) for idx, priority in enumerate(docs)])

    ans = 0
    while queue:
        current_doc = queue.popleft()

        if any(current_doc[1] < elem[1] for elem in queue):
            queue.append(current_doc)
        else:
            ans += 1
            if current_doc[0] == M:
                print(ans)
                break
