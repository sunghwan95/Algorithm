import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

if N <= K:
    print(0)
    exit(0)

sensors = list(map(int, input().split()))
sensors.sort()

dist_between_sensors = []
for i in range(N - 1):
    dist_between_sensors.append(sensors[i + 1] - sensors[i])

dist_between_sensors.sort(reverse=True)

ans = sum(dist_between_sensors[K - 1 :])
print(ans)
