import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for j in range(1, n + 1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)

# graph = [[0] * (n+1) for _ in range(n+1)]
# visited = [0] * (n+1)
