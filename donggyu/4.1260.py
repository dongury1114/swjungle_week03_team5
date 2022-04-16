import sys
from collections import deque

sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = []

for i in range(N+1):
    graph.append([])

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

# print(graph)
visited = [False] * (N+1)
# for i in range(N+1):
#     visited.append(False) 

def bfs(V):
    
    que = deque([])
    visited[V] = True
    que.append(V)
    print(V, end = " ")
    while que:
        V = que.popleft()
        
        for i in graph[V]:
            if  visited[i]== False:
                visited[i] = True
                print(i, end = " ")
                que.append(i)

def dfs(V):

    visited[V] = True
    print(V ,end = " ")

    for i in graph[V]:
        if visited [i] == False:
            dfs(i)
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)