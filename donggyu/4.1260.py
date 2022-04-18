import sys
from collections import deque

sys.stdin = open("input.txt")


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
# for i in range(N+1):
#     graph.append([])

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

# print(N, M, V)
# print(graph)

def dfs(V):

    visited[V] = True #실수한 부분
    print(V, end=" ")
    for i in graph[V]:
        if visited[i] == False:
            dfs(i)

# print(graph)
def bfs(V):
    que = deque([])
    visited[V] = True
    que.append(V)
    print(V, end=" ")
    while que:
        v = que.popleft()
        
        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                print(i, end=" ")
                que.append(i)

dfs(V)
print()
visited = [False] *(N+1)
bfs(V)