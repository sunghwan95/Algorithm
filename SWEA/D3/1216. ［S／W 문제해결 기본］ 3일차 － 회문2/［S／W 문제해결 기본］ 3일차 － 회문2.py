def isPalindrome(arr: list):
    max_len = 1
    n = len(arr)

    for i in range(n, 0, -1):
        for start in range(n - i + 1):
            end = start + i
            segment = arr[start:end]
            if segment == segment[::-1]:
                return i

    return max_len


for _ in range(10):
    tc = int(input())

    graph = []
    for _ in range(100):
        a = input().strip()
        graph.append(list(a))

    rotated_graph = list(list(col) for col in zip(*graph))

    ans = 0

    for arr in graph:
        ans = max(ans, isPalindrome(arr))

    for arr in rotated_graph:
        ans = max(ans, isPalindrome(arr))

    print(f"#{tc} {ans}")
