import sys

input = sys.stdin.readline

N = int(input())

words = []
for _ in range(N):
    a = input().rstrip()
    words.append((a, len(a)))

_words = list(set(words))

_words.sort(key=lambda x: (x[1], x))


for a in _words:
    print(a[0])
