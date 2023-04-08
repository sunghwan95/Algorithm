rows = [0]
cols = [0]

x, y = map(int, input().split())
rows.append(x)
cols.append(y)

n = int(input())
for _ in range(n):
    axis, cut_line = map(int, input().split())
    if axis == 0:
        cols.append(cut_line)
    else:
        rows.append(cut_line)

rows.sort(reverse=True)
cols.sort(reverse=True)

widths = []
heights = []

# 사각형 조각의 가로길이 구하기
i = 0
for _ in rows:
    try:
        width = rows[i]-rows[i+1]
        widths.append(width)
        i += 1
    except IndexError:
        break

# 사각형 조각의 높이 구하기
i = 0
for _ in cols:
    try:
        height = cols[i]-cols[i+1]
        heights.append(height)
        i += 1
    except IndexError:
        break

print(max(widths)*max(heights))
