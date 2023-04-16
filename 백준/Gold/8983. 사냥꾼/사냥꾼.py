import sys

M, N, L = map(int, sys.stdin.readline().split())

hunting_zones = list(map(int, sys.stdin.readline().split()))

animals = []
for _ in range(N):
    b = tuple(map(int, sys.stdin.readline().split()))
    animals.append(b)

count = 0
arr = []


for hunting_zone in hunting_zones:
    for animal in animals:
        distance = abs(animal[0]-hunting_zone)+animal[1]
        if distance <= L:
            count += 1
            arr.append(animal)
    for i in arr:
        if i in animals:
            animals.remove(i)


print(count)
