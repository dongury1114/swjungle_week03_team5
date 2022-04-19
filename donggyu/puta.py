import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt")

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N + 1):
    graph[i].sort()

visited = [False] * (N + 1)
count = 0
def dfs(v):
    visited[v] = True
    global count
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

for i in range (1, N+1):
    if visited[i] == False:
        count += 1
        dfs(i)

print(count)