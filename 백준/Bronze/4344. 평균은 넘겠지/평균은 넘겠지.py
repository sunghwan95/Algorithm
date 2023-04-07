C = int(input())
per_arr = []
for _ in range(C):
    scores = list(map(int, input().split()))
    count = scores.pop(0)
    sum_score = sum(scores)
    avg_score = sum_score / count
    arr = []
    for score in scores:
        if score > avg_score:
            arr.append(score)
        per = round((len(arr)/len(scores))*100, 3)
    per_arr.append(per)
for i in per_arr:
    print(f'{format(i, ".3f")}%')
