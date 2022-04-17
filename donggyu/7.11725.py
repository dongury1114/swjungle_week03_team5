import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())

graph = []
visited = [False] * (N+1)
answer = []
for i in range(N+1):
    graph.append([])

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N-1):
    graph[i].sort()

for i in range(N+1):
    answer.append(1)

def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            answer[i] = v
            dfs(i)

#부모 노드만 찾아서 출력하면 된다! // 어떻게 ?
#answer라는 리스트를 만들어서, 해결을 해야한다 -> 기존 dfs 에서 수정 
dfs(1)

for i in range(2, len(answer)):
    print(answer[i])
