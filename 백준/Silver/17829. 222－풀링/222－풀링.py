import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    a = list(map(int, input().split()))
    graph.append(a)


def div_conq(size, x, y):
    if size == 2:
        ans = [graph[x][y], graph[x][y+1], graph[x+1][y], graph[x+1][y+1]]
        ans.sort()
        return ans[-2]
    quadrant_1 = div_conq(size//2, x,         y)
    quadrant_2 = div_conq(size//2, x,         y+size//2)
    quadrant_3 = div_conq(size//2, x+size//2, y)
    quadrant_4 = div_conq(size//2, x+size//2, y+size//2)
    ans = [quadrant_1, quadrant_2, quadrant_3, quadrant_4]
    ans.sort()
    return ans[-2]


print(div_conq(N, 0, 0))
