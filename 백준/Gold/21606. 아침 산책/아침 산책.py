import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
in_out = [" "] + list(map(str, input().rstrip()))
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0


def dfs(x):
    global count
    for i in graph[x]:
        if in_out[i] == "1" and visited[i] == 0:
            visited[i] = 1
            count += 1
        elif in_out[i] == "0" and visited[i] == 0:
            visited[i] = 1
            dfs(i)
            visited[i] = 0


for i in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    if in_out[i] == "1":
        visited[i] = 1
        dfs(i)

print(count)
