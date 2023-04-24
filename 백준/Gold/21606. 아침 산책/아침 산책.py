import sys
input = sys.stdin.readline

N = int(input())
string = list(map(str, input().rstrip()))
in_out = ["-1"]
for i in string:
    in_out.append(i)

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(N+1)
res = [0]*(N+1)


def dfs(x, start):
    if in_out[x] == "1":
        res[x] += 1
        res[start] += 1
        return

    for _next in graph[x]:
        if visited[_next] == 0:
            visited[_next] = 1
            dfs(_next, start)
            visited[_next] = 0


count = 0
for i in range(1, N+1):
    if in_out[i] == "1":
        visited[i] = 1
        for _next in graph[i]:
            if in_out[_next] == "1":
                if visited[_next] == 0:
                    res[_next] += 1
                    res[i] += 1
            else:
                visited[_next] = 1
                dfs(_next, i)
                visited[_next] = 0

print(sum(res))
