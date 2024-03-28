# # 1
# import sys
# from collections import Counter

# input = sys.stdin.readline

# word = str(input().rstrip())
# upperWord = word.upper()

# eachCharCnt = Counter(upperWord)

# mostCommonChar = []
# maxCnt = max(eachCharCnt.values())
# for char, count in eachCharCnt.items():
#     if count == maxCnt:
#         mostCommonChar.append(char)

# if len(mostCommonChar) >= 2:
#     print("?")
# else:
#     print(mostCommonChar[0])

import sys

input = sys.stdin.readline

word = str(input().rstrip())
upperWord = word.upper()

wordCnt = []
setWord = set(upperWord)
for i in setWord:
    a = upperWord.count(i)
    wordCnt.append(a)

if wordCnt.count(max(wordCnt)) >= 2:
    print("?")
else:
    for j in setWord:
        if upperWord.count(j) == max(wordCnt):
            print(j)
