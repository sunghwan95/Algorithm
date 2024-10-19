import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    docs = deque(list(map(int, input().split())))

    q = deque([(idx, priority) for idx, priority in enumerate(docs)])

    want_print = q[M]

    cnt = 0
    while q:
        cur_doc = q[0]
        if any(cur_doc[1] < elem[1] for elem in q):
            q.append(q.popleft())
        else:
            if cur_doc[0] != want_print[0]:
                q.popleft()
                cnt += 1
            else:
                cnt += 1
                print(cnt)
                break
