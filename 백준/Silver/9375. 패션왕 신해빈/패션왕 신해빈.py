import sys
from collections import Counter

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    clothes = []
    for _ in range(N):
        cloth, type = input().rstrip().split()
        clothes.append(type)
    clothes_counter = Counter(clothes)

    count = 1
    for key in clothes_counter.keys():
        count *= clothes_counter[key] + 1

    print(count - 1)
