import sys
sys.setrecursionlimit(10 ** 4)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(v):
    visited[v] = True

    for i in arr[v]:
        if not visited[i]:
            dfs(i)


n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, n+1):
    arr[i].sort()

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
