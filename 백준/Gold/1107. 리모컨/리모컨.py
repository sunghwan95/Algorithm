import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
if M != 0:
    broken_nums = list(map(int, input().split()))
else:
    broken_nums = []

if N == 100:
    print(0)
    exit(0)


def is_possible_to_move(channel):
    while channel:
        channel = int(channel)
        if (channel % 10) in broken_nums:
            return False
        channel //= 10

    return True


ans = abs(N - 100)

if len(broken_nums) == 10:
    print(ans)
    exit(0)
else:
    diff = 0
    while True:
        under_movable_channel = str(N - diff)
        above_movable_channel = str(N + diff)

        if int(under_movable_channel) >= 0 and is_possible_to_move(
            under_movable_channel
        ):
            ans = min(ans, len(under_movable_channel) + diff)
            break

        elif is_possible_to_move(above_movable_channel):
            ans = min(ans, len(above_movable_channel) + diff)
            break

        diff += 1

print(ans)
