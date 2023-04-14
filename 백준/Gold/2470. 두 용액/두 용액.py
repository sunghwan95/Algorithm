import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

start = 0
end = N-1
min_value = sys.maxsize

while start < end:
    # 특성값 초기 설정.
    property_val = arr[start]+arr[end]

    # 만약 특성값의 절대값이 기존의 최소값 보다 작다면
    if abs(property_val) < min_value:
        min_value = abs(property_val)
        answer = [arr[start], arr[end]]

    if property_val < 0:
        start += 1
    elif property_val > 0:
        end -= 1
    else:
        break

print(answer[0], answer[1])
