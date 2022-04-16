import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
visited = [False] * (N+1)
count = 0

def dfs(v):
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for j in range(1, N +1 ):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)