import sys

sys.stdin = open("input.txt")

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

def dfs(V):

    visited[V] = True #실수한 부분

    for i in graph[V]:
        if visited[i] == False:
            dfs(i)

result = 0
for i in range(1, N+1):
    if visited[i] == False: #항상 신경쓰기
        dfs(i)
        result += 1

print(result)