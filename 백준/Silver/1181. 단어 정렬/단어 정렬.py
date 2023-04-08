N = int(input())
words = []

for _ in range(N):
    word = input()
    words.append((word, len(word)))

remove_dup = set(words)

sorted_by_length = sorted(remove_dup, key=lambda word: (word[1], word))

for ele in sorted_by_length:
    print(ele[0])