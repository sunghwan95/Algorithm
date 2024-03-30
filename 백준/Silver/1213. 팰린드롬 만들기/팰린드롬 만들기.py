import sys
from collections import Counter

input = sys.stdin.readline

name = str(input().rstrip())
name_counter = Counter(name)

count = 0
center = ""
even_keys = []
for key, value in name_counter.items():
    if value % 2 != 0:
        if value == 1:
            count += 1
            center = key
        else:
            value -= 1
            count += 1
            center = key
            even_keys.append(key)

    else:
        even_keys.append(key)

    if count >= 2:
        print("I'm Sorry Hansoo")
        exit(0)

ans = []
for key, value in name_counter.items():
    if key in even_keys:
        for _ in range(value // 2):
            ans.append(key)

ans.sort()
print("".join(ans) + center + "".join(ans[::-1]))
