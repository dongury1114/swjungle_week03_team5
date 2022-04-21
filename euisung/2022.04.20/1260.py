from collections import deque
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(v):
    visited[v] = True
    print(v, end=" ")

    for i in arr[v]:
        if not visited[i]:
            dfs(i)


def bfs(v):
    que = deque([v])
    visited[v] = True

    while que:
        x = que.popleft()
        print(x, end=" ")
        for i in arr[x]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


n, m, v = map(int, input().split())

arr = [[]for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, n+1):
    arr[i].sort()

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)
