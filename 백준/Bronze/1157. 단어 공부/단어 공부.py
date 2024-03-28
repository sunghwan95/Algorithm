import sys
from collections import Counter

input = sys.stdin.readline

word = str(input().rstrip())
upperWord = word.upper()

eachCharCnt = Counter(upperWord)

mostCommonChar = []
maxCnt = max(eachCharCnt.values())
for char, count in eachCharCnt.items():
    if count == maxCnt:
        mostCommonChar.append(char)

if len(mostCommonChar) >= 2:
    print("?")
else:
    print(mostCommonChar[0])
