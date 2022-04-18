import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(start, value):
    visited[start] = True
    for i in graph[start]:
        if location[i] == 1:
            value += 1
        elif not visited[i] and location[i] == 0:
            value = dfs(i, value)
    return value


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

hap = 0
for i in range(1, n+1):
    if not visited[i] and location[i] == 0:
        x = dfs(i, 0)
        hap += x*(x-1)

print(cnt + hap)
