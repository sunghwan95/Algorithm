import sys
input = sys.stdin.readline

N, M = map(int, input().split())

beads_heavy = [[] for _ in range(N+1)]
beads_light = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    beads_heavy[b].append(a)
    beads_light[a].append(b)


def dfs(arr, n):
    global count
    for i in arr[n]:
        if visited[i] == 0:
            visited[i] = 1
            count += 1
            dfs(arr, i)


res = 0
for i in range(1, (N+1)):
    visited = [0 for _ in range(N+1)]
    count = 0
    dfs(beads_heavy, i)
    if count >= (N+1)//2:
        res += 1
        
    visited = [0 for _ in range(N+1)]
    count = 0
    dfs(beads_light, i)
    if count >= (N+1)//2:
        res += 1

print(res)
