import sys
sys.setrecursionlimit(10 ** 4)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(v):
    global cnt
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)


n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, n+1):
    arr[i].sort()

dfs(1)
print(cnt)
