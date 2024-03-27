import sys

input = sys.stdin.readline

gradePoint = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0,
}


multipledByGpa = 0
totalPoint = 0
for _ in range(20):
    subject, point, grade = input().split()

    if grade == "P":
        continue

    multipledByGpa += float(point) * gradePoint[grade]
    totalPoint += float(point)

print(f"{(multipledByGpa / totalPoint) : .6f}")
