import sys

input = sys.stdin.readline

N = int(input())
words = []
for _ in range(N):
    word = str(input().rstrip())
    words.append(word)

M = int(input())
sub_words = []
for _ in range(M):
    sub_word = str(input().rstrip())
    sub_words.append(sub_word)

if N == 1:
    print(sub_words[0])
    exit(0)

ans = ""
if "?" == words[0]:
    lastChar = words[1][0]
    for a in sub_words:
        if a not in words and a[-1] == lastChar:
            ans = a

elif "?" == words[-1]:
    firstChar = words[-2][-1]
    for a in sub_words:
        if a not in words and a[0] == firstChar:
            ans = a
else:
    findIdx = words.index("?")
    firstChar = words[findIdx - 1][-1]
    lastChar = words[findIdx + 1][0]
    for a in sub_words:
        if a not in words and a[0] == firstChar and a[-1] == lastChar:
            ans = a

print(ans)
