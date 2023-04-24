import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
in_out = [" "] + list(map(str, input().rstrip()))
visited = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


count = 0


def dfs(x, start):
    global count
    if in_out[x] == "1":
        count += 2
        return
    for _next in graph[x]:
        if visited[_next] == 0:
            visited[_next] = 1
            dfs(_next, start)
            visited[_next] = 0


for i in range(1, N+1):
    if in_out[i] == "1":
        visited[i] = 1
        for _next in graph[i]:
            if in_out[_next] == "1":
                if visited[_next] == 0:
                    count += 2
            else:
                visited[_next] = 1
                dfs(_next, i)
                visited[_next] = 0

print(count)
