import sys
T = int(sys.stdin.readline())
arr = []
for _ in range(T):
    n = int(sys.stdin.readline())
    arr.append(n)


def isPrime(partition):
    for x in range(2, int(partition**0.5)+1):
        if partition % x == 0:
            return False
    return True


for num in arr:
    partition1, partition2 = num//2, num//2
    while partition1 > 0:
        if isPrime(partition1) and isPrime(partition2):
            print(partition1, partition2)
            break
        else:
            partition1 -= 1
            partition2 += 1
