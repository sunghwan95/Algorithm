import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    f_sizes = list(map(int, input().split()))
    heapq.heapify(f_sizes)

    ans = 0
    while len(f_sizes) > 1:
        a = heapq.heappop(f_sizes)
        b = heapq.heappop(f_sizes)

        sum_two_files = a + b
        ans += sum_two_files

        heapq.heappush(f_sizes, sum_two_files)

    print(ans)
