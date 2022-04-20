import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt")

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
count = 0
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

for i in range (1, N+1):
    if visited[i] == False:
        count += 1
        dfs(i)

print(count)