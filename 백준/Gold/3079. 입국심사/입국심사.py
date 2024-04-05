"""
0. 특정 시간내의 모든 사람이 심사를 받아야 하므로, 시간을 기준으로 범위를 좁히거나 늘려 탐색
1. 최소시간 = 1, 최대시간 = 가장오래걸리는심사대 * 사람수
2. 최소시간과 최대시간의 평균시간을 구해 각 심사대에서 평균시간동안 몇명의 사람이 심사를 받을 수 있는지 확인
3. 만약, 평균시간동안 심사를 받을 수 있는 사람의 수 >= M이면 최대시간을 줄여(평균시간을 줄임, 최소심사시간을 구하기 위해)
   최소심사시간 도출
4. 그렇지 않다면 심사시간이 널널하지 않으므로 최소시간을 늘려 다시 탐색
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]

min_time = 1
max_time = max(times) * M

result = max_time
while min_time <= max_time:
    mid_time = (min_time + max_time) // 2

    # 각 심사대에서 mid_time동안 심사를 받을 수 있는 사람의 수
    people_examined = 0
    for time in times:
        people_examined += mid_time // time

    if people_examined >= M:
        result = mid_time
        max_time = mid_time - 1
    else:
        min_time = mid_time + 1

print(result)
