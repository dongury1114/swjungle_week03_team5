import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(start):
    global cnt
    visited[start] = True
    for i in graph[start]:
        if not visited[i] and graph[i] == 1:
            cnt += 1


n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
location = [0]+list(map(int, input().strip()))
cnt = 0

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    if location[a] == 1 and location[b] == 1:
        cnt += 2

for i in range(1, n+1):
    if not visited[i] and location[i] == 0:
        dfs(i)

print(cnt)
