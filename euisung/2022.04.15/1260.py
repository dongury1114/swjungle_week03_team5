def dfs(V):
    visited[V] = 1

    print(V, end=' ')

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)


def bfs(V):

    queue = [V]

    visited[V] = 0

    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, n+1):
            if(visited[i] == 1 and graph[V][i] == 1):
                queue.append(i)
                visited[i] = 0


n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


dfs(v)
print()
bfs(v)
