

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())

graph = []
visited = [False] * (N+1)
for i in range(N+1):
    graph.append([])

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N-1):
    graph[i].sort()


def dfs(v):
    visited[v] = True

    for i in graph(v):
        if visited[v] == False:
            dfs(i)