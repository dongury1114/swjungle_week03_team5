import sys
from collections import deque

sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = []
visited = [False] * (N + 1)

for i in range(N+1):
    graph.append([])

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N + 1):
    graph[i].sort()

def dfs(v):
    visited[v] = True
    print(v, end = " ")

    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

def bfs(v):
    que = deque([])
    visited[v] = True
    que.append(v)
    print(v, end = " ")
    while que:
        v = que.popleft()

        for i in graph[v]:
            if  visited[i] == False:
                visited[i] = True
                print(i, end = " ")
                que.append(i)

dfs(V)
print()
visited = [False] * (N+1)
bfs(V)
