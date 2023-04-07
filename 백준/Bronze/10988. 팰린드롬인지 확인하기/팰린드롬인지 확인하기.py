word = str(input())
a = []
for n in range(len(word)):
    if word[n] == word[-(n+1)]:
        a.append(1)
    else:
        a.append(0)

b = ''.join(map(str, a))
if b.find("0") == -1:
    print(1)
else:
    print(0)
