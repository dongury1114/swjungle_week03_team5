import sys
from collections import deque

sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
count = 0

for i in range(N+1):
    graph.append([])

# print(graph)

visited = [False] * (N+1)
# print(visited)
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)