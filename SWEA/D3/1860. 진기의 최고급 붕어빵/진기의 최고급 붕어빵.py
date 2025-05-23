T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()

    canServe = True
    fishbun = 0
    i = 0

    for time in range(max(nums) + 1):
        if time != 0 and time % M == 0:
            fishbun += K

        while i < N and nums[i] == time:
            if fishbun > 0:
                fishbun -= 1
                i += 1
            else:
                canServe = False
                break

        if not canServe:
            break

    if canServe:
        print(f"#{tc} Possible")
    else:
        print(f"#{tc} Impossible")
