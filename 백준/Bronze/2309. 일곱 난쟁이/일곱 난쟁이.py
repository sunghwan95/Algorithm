import random
shorts = []
for _ in range(9):
    height = int(input())
    shorts.append(height)

while True:
    random_height = random.sample(shorts, 7)
    if sum(random_height) == 100:
        random_height.sort()
        for height in random_height:
            print(height)
        break
    else:
        continue
