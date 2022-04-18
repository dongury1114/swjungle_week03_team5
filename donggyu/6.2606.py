import sys
from collections import deque

sys.stdin = open("input.txt")


N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
ans = 0
def dfs(V):
    visited[V] = True
    for i in graph[V]:
        if visited[i] == False:
            dfs(i)

#sol.01 (덩어리 문제 응용)
for i in range(1, N+1):

    if count < 1:
        if visited[i] == False:
            count += 1
            dfs(i)
    else:
        ans=visited.count(True)
print(ans-1)

#sol.02 (코드 간소화)
dfs(1)
print(visited.count(True)-1)

# graph[1]의 원소들의 수? (x) -> 간접적으로 연결된 친구들 까지
# 덩어리 문제 처럼 접근?
# 덩어리 2일때 종료 후 Visited에서 true 값 갯수?