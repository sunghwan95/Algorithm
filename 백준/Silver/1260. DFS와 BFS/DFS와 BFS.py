N, M, V = list(map(int, input().split()))

visited_dfs = [0]*(N+1)
visited_bfs = [0]*(N+1)

# 각 노드들의 연결을 행렬로 표시하기 위해 리스트 사용.
matrix = []
for _ in range(N+1):
    ele = [0]*(N+1)
    matrix.append(ele)

# 문제에서 주어진 조건에 맞게 연결된 노드들을 1로 표시.
for _ in range(M):
    i, j = map(int, input().split())
    matrix[i][j] = matrix[j][i] = 1


def dfs(V):
    visited_dfs[V] = 1
    print(V, end=" ")
    for i in range(1, N+1):
        # i노드를 방문한 적이 없고, V노드에서 i노드가 연결이 되어 있다면,
        if (visited_dfs[i] == 0) and (matrix[V][i] == 1):
            dfs(i)


def bfs(V):
    # 방문할 V노드를 순서대로 담을 큐.
    queue = [V]
    # 방문했으니 체크(1로 체크표시)
    visited_bfs[V] = 1
    # queue에 노드가 남아있는 동안 아래 코드 실행.
    while queue:
        a = queue.pop(0)
        print(a, end=" ")
        for i in range(1, N+1):
            if (visited_bfs[i] == 0) and (matrix[a][i] == 1):
                queue.append(i)
                visited_bfs[i] = 1


dfs(V)
print()
bfs(V)
