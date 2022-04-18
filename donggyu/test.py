import sys
from collections import deque

sys.stdin = open("input.txt")

N = int(input())

#부모를 구한다? dfs로 한번 파고 들어가볼수 있지 않을까?
#루트는 1로 고정

graph =[[] for _ in range(N+1)]

visited = [False] * (N+1)

for i in range(N-1): #반복횟수 생각하며 작성하자
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    graph[i].sort()

#이부분 이해가 어려웜...
answer = [0] * (N+1)


def dfs(V):
    visited[V] = True
    for i in graph[V]:
        if visited[i] == False:
            answer[i] = V
            dfs(i)


dfs(1)
for i in range(2, len(answer)):
    print(answer[i])